/**
 * Auth Context — manages user state, login, register, logout
 */

import { createContext, useContext, useState, useEffect, useCallback } from "react";
import { api } from "../api/client";

const AuthContext = createContext(null);

export function AuthProvider({ children }) {
    const [user, setUser] = useState(null);
    const [token, setToken] = useState(null);
    const [loading, setLoading] = useState(true);

    // Hydrate from localStorage on mount
    useEffect(() => {
        const savedToken = localStorage.getItem("cropguard_token");
        const savedUser = localStorage.getItem("cropguard_user");
        if (savedToken && savedUser) {
            setToken(savedToken);
            try {
                setUser(JSON.parse(savedUser));
            } catch {
                localStorage.removeItem("cropguard_user");
            }
        }
        setLoading(false);
    }, []);

    const login = useCallback(async (email, password) => {
        const res = await api.login({ email, password });
        const { token: newToken, user: newUser } = res.data;
        setToken(newToken);
        setUser(newUser);
        localStorage.setItem("cropguard_token", newToken);
        localStorage.setItem("cropguard_user", JSON.stringify(newUser));
        return newUser;
    }, []);

    const register = useCallback(async (name, email, password) => {
        const res = await api.register({ name, email, password });
        const { token: newToken, user: newUser } = res.data;
        setToken(newToken);
        setUser(newUser);
        localStorage.setItem("cropguard_token", newToken);
        localStorage.setItem("cropguard_user", JSON.stringify(newUser));
        return newUser;
    }, []);

    const logout = useCallback(() => {
        setUser(null);
        setToken(null);
        localStorage.removeItem("cropguard_token");
        localStorage.removeItem("cropguard_user");
    }, []);

    const value = {
        user,
        token,
        loading,
        isAuthenticated: !!token,
        login,
        register,
        logout,
    };

    return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth() {
    const ctx = useContext(AuthContext);
    if (!ctx) throw new Error("useAuth must be used within AuthProvider");
    return ctx;
}
