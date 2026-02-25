import { useState } from "react";
import { ThemeProvider, createTheme } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";
import Box from "@mui/material/Box";
import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import Upload from "./components/Upload";
import Results from "./components/Results";
import HowItWorks from "./components/HowItWorks";
import Features from "./components/Features";
import Footer from "./components/Footer";

const theme = createTheme({
  palette: {
    mode: "light",
    primary: {
      main: "#2E7D32",
      light: "#4CAF50",
      dark: "#1B5E20",
    },
    secondary: {
      main: "#A5D6A7",
      light: "#C8E6C9",
      dark: "#81C784",
    },
    background: {
      default: "#F1F8E9",
      paper: "#FFFFFF",
    },
  },
  typography: {
    fontFamily: [
      "-apple-system",
      "BlinkMacSystemFont",
      '"Segoe UI"',
      "Roboto",
      '"Helvetica Neue"',
      "Arial",
      "sans-serif",
    ].join(","),
  },
  shape: {
    borderRadius: 12,
  },
});

function App() {
  const [uploadedImage, setUploadedImage] = useState(null);
  const [detectionResult, setDetectionResult] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const detectDisease = async (file) => {
    setIsLoading(true);
    setDetectionResult(null);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://localhost:8000/detect", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        const err = await response.json().catch(() => ({}));
        throw new Error(err.detail || `Server error: ${response.status}`);
      }

      const data = await response.json();
      setDetectionResult(data);

      setTimeout(() => {
        document.getElementById("results")?.scrollIntoView({ behavior: "smooth", block: "start" });
      }, 100);
    } catch (error) {
      console.error("Detection failed:", error);
      alert(`Detection failed: ${error.message}`);
    } finally {
      setIsLoading(false);
    }
  };

  const handleImageUpload = (imageData, file) => {
    setUploadedImage(imageData);
    setDetectionResult(null);

    if (file) {
      detectDisease(file);
    }
  };

  const handleUploadClick = () => {
    document.getElementById("upload").scrollIntoView({ behavior: "smooth" });
  };

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Box sx={{ bgcolor: "background.default" }}>
        <Navbar />
        <Hero onUploadClick={handleUploadClick} />
        <Upload
          onImageUpload={handleImageUpload}
          uploadedImage={uploadedImage}
        />
        {(detectionResult || isLoading) && (
          <Box id="results">
            <Results result={detectionResult} isLoading={isLoading} />
          </Box>
        )}
        <HowItWorks />
        <Features />
        <Footer />
      </Box>
    </ThemeProvider>
  );
}

export default App;
