import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import Paper from "@mui/material/Paper";
import Stack from "@mui/material/Stack";
import Chip from "@mui/material/Chip";
import Button from "@mui/material/Button";
import CircularProgress from "@mui/material/CircularProgress";
import Alert from "@mui/material/Alert";
import ArrowBackOutlined from "@mui/icons-material/ArrowBackOutlined";
import { api } from "../api/client";
import { useAuth } from "../context/AuthContext";

const severityColors = {
    None: { bg: "#eaf5ea", color: "#3a7a3a" },
    Low: { bg: "#eaf5ea", color: "#5a9a3c" },
    Medium: { bg: "#fdf5e6", color: "#9b7d4a" },
    High: { bg: "#fde0db", color: "#c25a4a" },
};

const History = () => {
    const { isAuthenticated } = useAuth();
    const navigate = useNavigate();
    const [predictions, setPredictions] = useState([]);
    const [total, setTotal] = useState(0);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");
    const [page, setPage] = useState(1);

    useEffect(() => {
        if (!isAuthenticated) {
            navigate("/login");
            return;
        }
        fetchHistory();
    }, [page, isAuthenticated]);

    const fetchHistory = async () => {
        setLoading(true);
        try {
            const res = await api.getHistory(page, 10);
            setPredictions(res.data.predictions);
            setTotal(res.data.total);
        } catch (err) {
            setError("Failed to load history. Please try again.");
        } finally {
            setLoading(false);
        }
    };

    const formatDate = (dateStr) => {
        try {
            return new Date(dateStr).toLocaleDateString("en-IN", {
                day: "numeric",
                month: "short",
                year: "numeric",
                hour: "2-digit",
                minute: "2-digit",
            });
        } catch {
            return dateStr;
        }
    };

    return (
        <Box sx={{ minHeight: "100vh", bgcolor: "#fafaf7", pt: 10, pb: 6 }}>
            <Container maxWidth="md">
                <Stack spacing={4}>
                    {/* Header */}
                    <Stack direction="row" alignItems="center" spacing={2}>
                        <Button
                            startIcon={<ArrowBackOutlined />}
                            onClick={() => navigate("/")}
                            sx={{ color: "#4a7c59" }}
                        >
                            Back
                        </Button>
                        <Typography variant="h4" fontWeight={700} sx={{ flex: 1 }}>
                            Prediction History
                        </Typography>
                        <Chip label={`${total} total`} sx={{ bgcolor: "rgba(74,124,89,0.08)", color: "#4a7c59", fontWeight: 600 }} />
                    </Stack>

                    {error && <Alert severity="error">{error}</Alert>}

                    {loading ? (
                        <Box textAlign="center" py={6}>
                            <CircularProgress sx={{ color: "#4a7c59" }} />
                        </Box>
                    ) : predictions.length === 0 ? (
                        <Paper
                            elevation={0}
                            sx={{
                                p: 6,
                                textAlign: "center",
                                border: "1px solid rgba(0,0,0,0.06)",
                            }}
                        >
                            <Typography variant="h6" color="text.secondary" gutterBottom>
                                No predictions yet
                            </Typography>
                            <Typography variant="body2" color="text.secondary" sx={{ mb: 3 }}>
                                Upload a crop leaf image to get started
                            </Typography>
                            <Button variant="contained" onClick={() => navigate("/")}>
                                Upload Image
                            </Button>
                        </Paper>
                    ) : (
                        <Stack spacing={2} className="stagger-children">
                            {predictions.map((pred) => {
                                const sv = severityColors[pred.severity] || severityColors.Medium;
                                return (
                                    <Paper
                                        key={pred.prediction_id}
                                        elevation={0}
                                        className="animate-fade-in-up hover-lift"
                                        sx={{
                                            p: 3,
                                            border: "1px solid rgba(0,0,0,0.06)",
                                            cursor: "pointer",
                                        }}
                                        onClick={() => {/* could navigate to detail */ }}
                                    >
                                        <Stack
                                            direction={{ xs: "column", sm: "row" }}
                                            justifyContent="space-between"
                                            alignItems={{ sm: "center" }}
                                            spacing={2}
                                        >
                                            <Stack spacing={0.5}>
                                                <Typography variant="subtitle1" fontWeight={700}>
                                                    {pred.disease_name}
                                                </Typography>
                                                <Typography variant="body2" color="text.secondary">
                                                    {pred.crop_name} • {formatDate(pred.created_at)}
                                                </Typography>
                                            </Stack>
                                            <Stack direction="row" spacing={1} alignItems="center">
                                                <Chip
                                                    label={pred.status}
                                                    size="small"
                                                    sx={{
                                                        bgcolor: pred.status === "Healthy" ? "#eaf5ea" : "#fde0db",
                                                        color: pred.status === "Healthy" ? "#3a7a3a" : "#c25a4a",
                                                        fontWeight: 600,
                                                    }}
                                                />
                                                <Chip
                                                    label={`${pred.confidence}%`}
                                                    size="small"
                                                    sx={{
                                                        bgcolor: "rgba(74,124,89,0.08)",
                                                        color: "#4a7c59",
                                                        fontWeight: 700,
                                                    }}
                                                />
                                                {pred.severity && pred.severity !== "None" && (
                                                    <Chip
                                                        label={pred.severity}
                                                        size="small"
                                                        sx={{
                                                            bgcolor: sv.bg,
                                                            color: sv.color,
                                                            fontWeight: 600,
                                                        }}
                                                    />
                                                )}
                                            </Stack>
                                        </Stack>
                                    </Paper>
                                );
                            })}

                            {/* Pagination */}
                            {total > 10 && (
                                <Stack direction="row" spacing={2} justifyContent="center" pt={2}>
                                    <Button
                                        variant="outlined"
                                        disabled={page <= 1}
                                        onClick={() => setPage((p) => p - 1)}
                                    >
                                        Previous
                                    </Button>
                                    <Button
                                        variant="outlined"
                                        disabled={page * 10 >= total}
                                        onClick={() => setPage((p) => p + 1)}
                                    >
                                        Next
                                    </Button>
                                </Stack>
                            )}
                        </Stack>
                    )}
                </Stack>
            </Container>
        </Box>
    );
};

export default History;
