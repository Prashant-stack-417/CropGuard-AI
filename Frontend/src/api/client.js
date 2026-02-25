/**
 * Axios API Client
 * -----------------
 * Centralised HTTP client with JWT interceptor.
 */

import axios from "axios";

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
    predict: (file) => {
        const formData = new FormData();
        formData.append("file", file);
        return client.post("/api/predict", formData, {
            headers: { "Content-Type": "multipart/form-data" },
            timeout: 60000,
        });
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
