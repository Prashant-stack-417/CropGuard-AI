import { useState } from "react";
import { useNavigate, Link as RouterLink } from "react-router-dom";
import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import Paper from "@mui/material/Paper";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import Stack from "@mui/material/Stack";
import Alert from "@mui/material/Alert";
import Link from "@mui/material/Link";
import CircularProgress from "@mui/material/CircularProgress";
import Spa from "@mui/icons-material/Spa";
import { useAuth } from "../context/AuthContext";

const Register = () => {
    const { register } = useAuth();
    const navigate = useNavigate();
    const [name, setName] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");
    const [error, setError] = useState("");
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError("");

        if (password !== confirmPassword) {
            setError("Passwords don't match");
            return;
        }
        if (password.length < 6) {
            setError("Password must be at least 6 characters");
            return;
        }

        setLoading(true);
        try {
            await register(name, email, password);
            navigate("/");
        } catch (err) {
            setError(err.response?.data?.detail || "Registration failed. Please try again.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <Box sx={{ minHeight: "100vh", bgcolor: "#fafaf7", pt: 12, pb: 6 }}>
            <Container maxWidth="sm">
                <Stack spacing={4} alignItems="center">
                    <Stack direction="row" spacing={1} alignItems="center">
                        <Spa sx={{ fontSize: 32, color: "#4a7c59" }} />
                        <Typography variant="h4" fontWeight={800} sx={{ color: "#2d3a2d" }}>
                            CropGuard
                        </Typography>
                    </Stack>

                    <Paper
                        elevation={0}
                        sx={{
                            width: "100%",
                            p: { xs: 3, sm: 5 },
                            border: "1px solid rgba(0,0,0,0.08)",
                            borderRadius: 3,
                        }}
                    >
                        <Stack spacing={3}>
                            <Box textAlign="center">
                                <Typography variant="h5" fontWeight={700} gutterBottom>
                                    Create your account
                                </Typography>
                                <Typography variant="body2" color="text.secondary">
                                    Join CropGuard to save your prediction history
                                </Typography>
                            </Box>

                            {error && <Alert severity="error">{error}</Alert>}

                            <form onSubmit={handleSubmit}>
                                <Stack spacing={2.5}>
                                    <TextField
                                        label="Full Name"
                                        value={name}
                                        onChange={(e) => setName(e.target.value)}
                                        required
                                        fullWidth
                                        autoComplete="name"
                                    />
                                    <TextField
                                        label="Email Address"
                                        type="email"
                                        value={email}
                                        onChange={(e) => setEmail(e.target.value)}
                                        required
                                        fullWidth
                                        autoComplete="email"
                                    />
                                    <TextField
                                        label="Password"
                                        type="password"
                                        value={password}
                                        onChange={(e) => setPassword(e.target.value)}
                                        required
                                        fullWidth
                                        autoComplete="new-password"
                                        helperText="At least 6 characters"
                                    />
                                    <TextField
                                        label="Confirm Password"
                                        type="password"
                                        value={confirmPassword}
                                        onChange={(e) => setConfirmPassword(e.target.value)}
                                        required
                                        fullWidth
                                        autoComplete="new-password"
                                    />
                                    <Button
                                        type="submit"
                                        variant="contained"
                                        size="large"
                                        disabled={loading}
                                        fullWidth
                                        sx={{ py: 1.5 }}
                                    >
                                        {loading ? <CircularProgress size={24} color="inherit" /> : "Create Account"}
                                    </Button>
                                </Stack>
                            </form>

                            <Typography variant="body2" color="text.secondary" textAlign="center">
                                Already have an account?{" "}
                                <Link component={RouterLink} to="/login" sx={{ color: "#4a7c59", fontWeight: 600 }}>
                                    Sign in
                                </Link>
                            </Typography>
                        </Stack>
                    </Paper>
                </Stack>
            </Container>
        </Box>
    );
};

export default Register;
