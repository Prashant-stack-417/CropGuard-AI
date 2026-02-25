import { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import Paper from "@mui/material/Paper";
import Stack from "@mui/material/Stack";
import Chip from "@mui/material/Chip";
import Button from "@mui/material/Button";
import Grid from "@mui/material/Grid";
import CircularProgress from "@mui/material/CircularProgress";
import Alert from "@mui/material/Alert";
import ArrowBackOutlined from "@mui/icons-material/ArrowBackOutlined";
import LocalFloristOutlined from "@mui/icons-material/LocalFloristOutlined";
import ScienceOutlined from "@mui/icons-material/ScienceOutlined";
import { api } from "../api/client";

const DiseaseDetail = () => {
    const { classKey } = useParams();
    const navigate = useNavigate();
    const [disease, setDisease] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    useEffect(() => {
        if (classKey) fetchDisease();
    }, [classKey]);

    const fetchDisease = async () => {
        setLoading(true);
        try {
            const res = await api.getDiseaseDetail(classKey);
            setDisease(res.data);
        } catch (err) {
            setError("Disease not found or server unavailable.");
        } finally {
            setLoading(false);
        }
    };

    const severityColors = {
        None: "#5a9a3c",
        Low: "#5a9a3c",
        Medium: "#d4953a",
        High: "#c25a4a",
    };

    if (loading) {
        return (
            <Box sx={{ minHeight: "100vh", bgcolor: "#fafaf7", pt: 12, textAlign: "center" }}>
                <CircularProgress sx={{ color: "#4a7c59" }} />
            </Box>
        );
    }

    if (error || !disease) {
        return (
            <Box sx={{ minHeight: "100vh", bgcolor: "#fafaf7", pt: 12 }}>
                <Container maxWidth="md">
                    <Alert severity="error" sx={{ mb: 2 }}>{error || "Disease not found"}</Alert>
                    <Button startIcon={<ArrowBackOutlined />} onClick={() => navigate(-1)}>
                        Go Back
                    </Button>
                </Container>
            </Box>
        );
    }

    return (
        <Box sx={{ minHeight: "100vh", bgcolor: "#fafaf7", pt: 10, pb: 6 }}>
            <Container maxWidth="md">
                <Stack spacing={4}>
                    {/* Back button */}
                    <Button
                        startIcon={<ArrowBackOutlined />}
                        onClick={() => navigate(-1)}
                        sx={{ color: "#4a7c59", alignSelf: "flex-start" }}
                    >
                        Back
                    </Button>

                    {/* Header */}
                    <Stack spacing={1.5}>
                        <Stack direction="row" spacing={1.5} alignItems="center" flexWrap="wrap" useFlexGap>
                            <Chip label={disease.crop} sx={{ bgcolor: "rgba(74,124,89,0.08)", color: "#4a7c59", fontWeight: 600 }} />
                            {disease.severity !== "None" && (
                                <Chip
                                    label={`Severity: ${disease.severity}`}
                                    sx={{
                                        bgcolor: `${severityColors[disease.severity]}18`,
                                        color: severityColors[disease.severity],
                                        fontWeight: 600,
                                    }}
                                />
                            )}
                            {disease.spread_risk !== "None" && (
                                <Chip
                                    label={`Spread Risk: ${disease.spread_risk}`}
                                    sx={{
                                        bgcolor: `${severityColors[disease.spread_risk]}18`,
                                        color: severityColors[disease.spread_risk],
                                        fontWeight: 600,
                                    }}
                                />
                            )}
                        </Stack>
                        <Typography variant="h3" fontWeight={800}>
                            {disease.disease_name}
                        </Typography>
                    </Stack>

                    {/* Description */}
                    <Paper elevation={0} sx={{ p: 3, border: "1px solid rgba(0,0,0,0.06)" }}>
                        <Typography variant="body1" lineHeight={1.8} color="text.primary">
                            {disease.description}
                        </Typography>
                    </Paper>

                    {/* Cause */}
                    <Paper elevation={0} sx={{ p: 3, bgcolor: "#f5f7f3", borderLeft: "3px solid #4a7c59" }}>
                        <Typography variant="overline" color="text.secondary" fontWeight={600}>Cause</Typography>
                        <Typography variant="body2" sx={{ mt: 0.5 }}>{disease.cause}</Typography>
                    </Paper>

                    {/* Symptoms */}
                    {disease.symptoms?.length > 0 && (
                        <Box>
                            <Typography variant="h6" fontWeight={700} gutterBottom>Symptoms</Typography>
                            <Stack spacing={1}>
                                {disease.symptoms.map((s, i) => (
                                    <Paper key={i} elevation={0} sx={{ p: 2, bgcolor: "#fafaf7", border: "1px solid rgba(0,0,0,0.04)", display: "flex", gap: 1.5, alignItems: "center" }}>
                                        <Box sx={{ width: 6, height: 6, borderRadius: "50%", bgcolor: "#c25a4a", flexShrink: 0 }} />
                                        <Typography variant="body2">{s}</Typography>
                                    </Paper>
                                ))}
                            </Stack>
                        </Box>
                    )}

                    {/* Treatments — Two columns */}
                    <Grid container spacing={3}>
                        {/* Organic */}
                        <Grid item xs={12} md={6}>
                            <Paper elevation={0} sx={{ p: 3, border: "1px solid rgba(0,0,0,0.06)", height: "100%" }}>
                                <Stack direction="row" spacing={1} alignItems="center" sx={{ mb: 2 }}>
                                    <LocalFloristOutlined sx={{ color: "#5a9a3c" }} />
                                    <Typography variant="h6" fontWeight={700}>Organic Treatment</Typography>
                                </Stack>
                                <Stack spacing={1.5}>
                                    {disease.organic_treatment?.map((t, i) => (
                                        <Box key={i} sx={{ display: "flex", gap: 1.5, alignItems: "flex-start" }}>
                                            <Box sx={{ width: 24, height: 24, bgcolor: "#eaf5ea", borderRadius: "50%", display: "flex", alignItems: "center", justifyContent: "center", fontWeight: 700, fontSize: "0.75rem", color: "#5a9a3c", flexShrink: 0, mt: 0.25 }}>
                                                {i + 1}
                                            </Box>
                                            <Typography variant="body2" lineHeight={1.6}>{t}</Typography>
                                        </Box>
                                    ))}
                                </Stack>
                            </Paper>
                        </Grid>

                        {/* Chemical */}
                        <Grid item xs={12} md={6}>
                            <Paper elevation={0} sx={{ p: 3, border: "1px solid rgba(0,0,0,0.06)", height: "100%" }}>
                                <Stack direction="row" spacing={1} alignItems="center" sx={{ mb: 2 }}>
                                    <ScienceOutlined sx={{ color: "#6d84a0" }} />
                                    <Typography variant="h6" fontWeight={700}>Chemical Treatment</Typography>
                                </Stack>
                                <Stack spacing={1.5}>
                                    {disease.chemical_treatment?.map((t, i) => (
                                        <Box key={i} sx={{ display: "flex", gap: 1.5, alignItems: "flex-start" }}>
                                            <Box sx={{ width: 24, height: 24, bgcolor: "#ecf0f5", borderRadius: "50%", display: "flex", alignItems: "center", justifyContent: "center", fontWeight: 700, fontSize: "0.75rem", color: "#6d84a0", flexShrink: 0, mt: 0.25 }}>
                                                {i + 1}
                                            </Box>
                                            <Typography variant="body2" lineHeight={1.6}>{t}</Typography>
                                        </Box>
                                    ))}
                                </Stack>
                            </Paper>
                        </Grid>
                    </Grid>

                    {/* Dosage */}
                    <Paper elevation={0} sx={{ p: 3, bgcolor: "#f8f3ea", border: "1px solid rgba(155,125,74,0.12)" }}>
                        <Typography variant="overline" color="text.secondary" fontWeight={600}>Dosage per Acre</Typography>
                        <Typography variant="body2" sx={{ mt: 0.5 }} lineHeight={1.7}>{disease.dosage}</Typography>
                    </Paper>

                    {/* Prevention */}
                    {disease.prevention?.length > 0 && (
                        <Box>
                            <Typography variant="h6" fontWeight={700} gutterBottom>Prevention Tips</Typography>
                            <Stack spacing={1}>
                                {disease.prevention.map((p, i) => (
                                    <Paper key={i} elevation={0} sx={{ p: 2, bgcolor: "#fafaf7", border: "1px solid rgba(0,0,0,0.04)", display: "flex", gap: 1.5, alignItems: "center" }}>
                                        <Box sx={{ width: 24, height: 24, bgcolor: "#eaf5ea", borderRadius: "50%", display: "flex", alignItems: "center", justifyContent: "center", fontWeight: 700, fontSize: "0.75rem", color: "#4a7c59", flexShrink: 0 }}>
                                            {i + 1}
                                        </Box>
                                        <Typography variant="body2">{p}</Typography>
                                    </Paper>
                                ))}
                            </Stack>
                        </Box>
                    )}
                </Stack>
            </Container>
        </Box>
    );
};

export default DiseaseDetail;
