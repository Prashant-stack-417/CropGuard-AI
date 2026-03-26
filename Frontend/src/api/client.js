/**
 * Axios API Client
 * -----------------
 * Centralised HTTP client with JWT interceptor.
 */

import axios from "axios";
import { runtimeLogger } from "../utils/runtimeLogger";

const API_BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

const client = axios.create({
    baseURL: API_BASE_URL,
    timeout: 30000,
    headers: {
        "Content-Type": "application/json",
    },
});

// ── Request interceptor: attach JWT ──────────────────────────────────
client.interceptors.request.use((config) => {
    config.headers = config.headers || {};
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
    getHistory: (page = 1, limit = 20) => client.get(`/api/history?page=${page}&limit=${limit}`),

    // Diseases
    getDiseases: (crop) => client.get(`/api/diseases${crop ? `?crop=${crop}` : ""}`),
    getDiseaseDetail: (classKey) => client.get(`/api/diseases/${classKey}`),
    getCrops: () => client.get("/api/crops"),

    // Status
    getStatus: () => client.get("/api/status"),
};

export const getApiErrorMessage = (error, fallbackMessage) => {
    const apiDetail = error?.response?.data?.detail || error?.response?.data?.message;
    if (apiDetail) {
        return apiDetail;
    }

    if (error?.code === "ERR_NETWORK" || !error?.response) {
        return "Backend service is unavailable. Start the backend server and try again.";
    }

    if (typeof error?.message === "string" && error.message.trim()) {
        return error.message;
    }

    return fallbackMessage;
};

export const getClientRelease = () => {
    return import.meta.env.VITE_APP_RELEASE || "local-dev";
};

export default client;
