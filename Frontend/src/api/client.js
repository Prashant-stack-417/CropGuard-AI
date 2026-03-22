/**
 * Axios API Client
 * -----------------
 * Centralised HTTP client with JWT interceptor.
 */

import axios from "axios";
import { runtimeLogger } from "../utils/runtimeLogger";

const API_BASE_URL = import.meta.env.VITE_API_URL || (import.meta.env.DEV ? "http://localhost:8000" : "");

const isLoopbackHost = (hostname) => {
    const host = (hostname || "").toLowerCase();
    return host === "localhost" || host === "127.0.0.1" || host === "::1";
};

const isPrivateIpv4 = (hostname) => {
    const parts = hostname.split(".").map((segment) => Number(segment));
    if (parts.length !== 4 || parts.some((n) => Number.isNaN(n))) return false;

    if (parts[0] === 10) return true;
    if (parts[0] === 192 && parts[1] === 168) return true;
    if (parts[0] === 172 && parts[1] >= 16 && parts[1] <= 31) return true;
    if (parts[0] === 169 && parts[1] === 254) return true;
    return false;
};

const getTargetAddressSpace = (urlString) => {
    try {
        const parsed = new URL(urlString, typeof window !== "undefined" ? window.location.origin : undefined);
        const host = parsed.hostname.toLowerCase();
        if (isLoopbackHost(host) || host.endsWith(".local")) {
            return "local";
        }

        if (isPrivateIpv4(host)) {
            return "private";
        }

        return null;
    } catch {
        return null;
    }
};

const shouldUsePnaSafeFetch = (path) => {
    const urlString = `${API_BASE_URL}${path}`;
    const addressSpace = getTargetAddressSpace(urlString);
    return Boolean(addressSpace);
};

const predictWithPnaSafeFetch = async (file) => {
    const formData = new FormData();
    formData.append("file", file);

    const path = "/api/predict";
    const requestUrl = `${API_BASE_URL}${path}`;
    const addressSpace = getTargetAddressSpace(requestUrl);
    const token = localStorage.getItem("cropguard_token");

    runtimeLogger.info("predict.request.start", {
        transport: "fetch",
        requestUrl,
        addressSpace,
    });

    const headers = {};
    if (token) {
        headers.Authorization = `Bearer ${token}`;
    }

    const requestOptions = {
        method: "POST",
        mode: "cors",
        headers,
        body: formData,
    };

    // Chrome Private Network Access: explicitly mark local/private targets.
    if (addressSpace) {
        requestOptions.targetAddressSpace = addressSpace;
    }

    let response;
    try {
        response = await fetch(requestUrl, requestOptions);
    } catch (error) {
        runtimeLogger.error("predict.request.network_error", {
            transport: "fetch",
            requestUrl,
            message: error?.message,
        });

        const pnaHint =
            "Request blocked by browser local network policy. Use an HTTPS backend URL in VITE_API_URL for deployed frontend, or grant local network permission for this site.";
        throw new Error(`${pnaHint} (${error?.message || "network request failed"})`);
    }

    let data = null;
    try {
        data = await response.json();
    } catch {
        data = null;
    }

    if (!response.ok) {
        runtimeLogger.warn("predict.request.failed", {
            transport: "fetch",
            requestUrl,
            status: response.status,
            detail: data?.detail || data?.message || null,
        });

        if (response.status === 401) {
            localStorage.removeItem("cropguard_token");
            localStorage.removeItem("cropguard_user");
        }

        const detail = data?.detail || data?.message || `HTTP ${response.status}`;
        const error = new Error(detail);
        error.response = {
            status: response.status,
            data,
        };
        throw error;
    }

    runtimeLogger.info("predict.request.success", {
        transport: "fetch",
        requestUrl,
        status: response.status,
    });

    return {
        data,
        status: response.status,
        statusText: response.statusText,
        headers: {},
        config: { url: requestUrl, method: "post" },
    };
};

const client = axios.create({
    baseURL: API_BASE_URL,
    timeout: 30000,
    headers: {
        "Content-Type": "application/json",
    },
});

// ── Request interceptor: attach JWT ──────────────────────────────────
client.interceptors.request.use((config) => {
    const token = localStorage.getItem("cropguard_token");
    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
});

// ── Response interceptor: handle errors ──────────────────────────────
client.interceptors.response.use(
    (response) => response,
    (error) => {
        if (error.response?.status === 401) {
            localStorage.removeItem("cropguard_token");
            localStorage.removeItem("cropguard_user");
            // optional: redirect to login
        }
        return Promise.reject(error);
    }
);

// ── API functions ────────────────────────────────────────────────────
export const api = {
    // Auth
    register: (data) => client.post("/api/register", data),
    login: (data) => client.post("/api/login", data),

    // Prediction
    predict: async (file) => {
        if (shouldUsePnaSafeFetch("/api/predict")) {
            return predictWithPnaSafeFetch(file);
        }

        const requestPath = "/api/predict";
        runtimeLogger.info("predict.request.start", {
            transport: "axios",
            requestPath,
        });

        const formData = new FormData();
        formData.append("file", file);

        try {
            const response = await client.post(requestPath, formData, {
                headers: { "Content-Type": "multipart/form-data" },
                timeout: 60000,
            });

            runtimeLogger.info("predict.request.success", {
                transport: "axios",
                requestPath,
                status: response.status,
            });

            return response;
        } catch (error) {
            runtimeLogger.error("predict.request.failed", {
                transport: "axios",
                requestPath,
                status: error?.response?.status || null,
                detail: error?.response?.data?.detail || error?.message,
            });
            throw error;
        }
    },

    // History
    getHistory: (page = 1, limit = 20) =>
        client.get(`/api/history?page=${page}&limit=${limit}`),

    // Diseases
    getDiseases: (crop) =>
        client.get(`/api/diseases${crop ? `?crop=${crop}` : ""}`),
    getDiseaseDetail: (classKey) => client.get(`/api/diseases/${classKey}`),
    getCrops: () => client.get("/api/crops"),

    // Status
    getStatus: () => client.get("/api/status"),
};

export default client;
