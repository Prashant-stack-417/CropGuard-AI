import { useState, useEffect } from "react";
import { BrowserRouter, Routes, Route, useLocation } from "react-router-dom";
import { ThemeProvider, createTheme } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";
import Box from "@mui/material/Box";
import Fab from "@mui/material/Fab";
import Zoom from "@mui/material/Zoom";
import KeyboardArrowUpOutlined from "@mui/icons-material/KeyboardArrowUpOutlined";
import { AuthProvider } from "./context/AuthContext";
import { api } from "./api/client";
import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import Upload from "./components/Upload";
import Results from "./components/Results";
import HowItWorks from "./components/HowItWorks";
import Features from "./components/Features";
import Footer from "./components/Footer";
import Login from "./pages/Login";
import Register from "./pages/Register";
import History from "./pages/History";
import DiseaseDetail from "./pages/DiseaseDetail";

/* ── Theme — warm, natural, earthy ──────────────────────────────────── */
const theme = createTheme({
  palette: {
    mode: "light",
    primary: { main: "#4a7c59", light: "#6a9b5e", dark: "#365a3f" },
    secondary: { main: "#c9a96e", light: "#dbb98a", dark: "#a88944" },
    background: { default: "#fafaf7", paper: "#ffffff" },
    text: { primary: "#2d3a2d", secondary: "#6b7c6b" },
    success: { main: "#5a9a3c" },
    warning: { main: "#d4953a" },
    error: { main: "#c25a4a" },
    divider: "rgba(0, 0, 0, 0.08)",
  },
  typography: {
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
    h1: { fontWeight: 800, letterSpacing: "-0.02em", color: "#2d3a2d" },
    h2: { fontWeight: 700, letterSpacing: "-0.01em", color: "#2d3a2d" },
    h3: { fontWeight: 700, color: "#2d3a2d" },
    h4: { fontWeight: 700, color: "#2d3a2d" },
    h5: { fontWeight: 600, color: "#2d3a2d" },
    h6: { fontWeight: 600, color: "#2d3a2d" },
    button: { fontWeight: 600, textTransform: "none" },
  },
  shape: { borderRadius: 12 },
  components: {
    MuiButton: {
      styleOverrides: {
        root: { borderRadius: 10, padding: "10px 24px", transition: "all 0.25s ease" },
        contained: {
          backgroundColor: "#4a7c59",
          boxShadow: "0 2px 8px rgba(74, 124, 89, 0.2)",
          "&:hover": {
            backgroundColor: "#3d6a4a",
            boxShadow: "0 4px 16px rgba(74, 124, 89, 0.25)",
            transform: "translateY(-1px)",
          },
        },
        outlined: {
          borderColor: "#4a7c59",
          color: "#4a7c59",
          "&:hover": { borderColor: "#365a3f", backgroundColor: "rgba(74, 124, 89, 0.04)" },
        },
      },
    },
    MuiPaper: {
      styleOverrides: {
        root: {
          backgroundImage: "none",
          boxShadow: "0 1px 3px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04)",
        },
      },
    },
    MuiChip: { styleOverrides: { root: { fontWeight: 600, borderRadius: 8 } } },
  },
});

/* ── Home page — assembles all sections ────────────────────────────── */
function HomePage() {
  const [uploadedImage, setUploadedImage] = useState(null);
  const [detectionResult, setDetectionResult] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const detectDisease = async (file) => {
    setIsLoading(true);
    setDetectionResult(null);
    try {
      const res = await api.predict(file);
      setDetectionResult(res.data);
      setTimeout(() => {
        document.getElementById("results")?.scrollIntoView({ behavior: "smooth", block: "start" });
      }, 100);
    } catch (error) {
      console.error("Detection failed:", error);
      alert(`Detection failed: ${error.response?.data?.detail || error.message}`);
    } finally {
      setIsLoading(false);
    }
  };

  const handleImageUpload = (imageData, file) => {
    setUploadedImage(imageData);
    setDetectionResult(null);
    if (file) detectDisease(file);
  };

  const handleUploadClick = () => {
    document.getElementById("upload")?.scrollIntoView({ behavior: "smooth" });
  };

  return (
    <>
      <Hero onUploadClick={handleUploadClick} />
      <Upload onImageUpload={handleImageUpload} uploadedImage={uploadedImage} />
      {(detectionResult || isLoading) && (
        <Box id="results">
          <Results result={detectionResult} isLoading={isLoading} />
        </Box>
      )}
      <HowItWorks />
      <Features />
    </>
  );
}

/* ── Scroll to top on route change ─────────────────────────────────── */
function ScrollToTop() {
  const { pathname } = useLocation();
  useEffect(() => {
    window.scrollTo(0, 0);
  }, [pathname]);
  return null;
}

/* ── App root ──────────────────────────────────────────────────────── */
function App() {
  const [showScrollTop, setShowScrollTop] = useState(false);

  useEffect(() => {
    const handleScroll = () => setShowScrollTop(window.scrollY > 400);
    window.addEventListener("scroll", handleScroll, { passive: true });
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <AuthProvider>
        <BrowserRouter>
          <ScrollToTop />
          <Box sx={{ bgcolor: "background.default", minHeight: "100vh" }}>
            <Navbar />
            <Routes>
              <Route path="/" element={<HomePage />} />
              <Route path="/login" element={<Login />} />
              <Route path="/register" element={<Register />} />
              <Route path="/history" element={<History />} />
              <Route path="/disease/:classKey" element={<DiseaseDetail />} />
            </Routes>
            <Footer />

            <Zoom in={showScrollTop}>
              <Fab
                size="medium"
                onClick={() => window.scrollTo({ top: 0, behavior: "smooth" })}
                sx={{
                  position: "fixed",
                  bottom: 32,
                  right: 32,
                  bgcolor: "#4a7c59",
                  color: "#fff",
                  boxShadow: "0 4px 12px rgba(74, 124, 89, 0.3)",
                  "&:hover": { bgcolor: "#3d6a4a" },
                }}
              >
                <KeyboardArrowUpOutlined />
              </Fab>
            </Zoom>
          </Box>
        </BrowserRouter>
      </AuthProvider>
    </ThemeProvider>
  );
}

export default App;
