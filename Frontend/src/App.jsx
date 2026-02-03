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

  // Simulated AI disease detection (replace with actual API call)
  const simulateDetection = () => {
    const diseases = [
      {
        diseaseName: "Late Blight",
        cropName: "Tomato",
        confidence: 94,
        status: "Diseased",
        description:
          "Late blight is a devastating disease that affects tomato plants, causing dark lesions on leaves and stems. It spreads rapidly in humid conditions and can destroy entire crops if left untreated.",
        treatments: [
          "Remove and destroy infected plant parts immediately",
          "Apply copper-based fungicides every 7-10 days",
          "Ensure proper plant spacing for air circulation",
          "Avoid overhead watering to reduce leaf wetness",
          "Use disease-resistant tomato varieties in future plantings",
        ],
      },
      {
        diseaseName: "Powdery Mildew",
        cropName: "Cucumber",
        confidence: 89,
        status: "Diseased",
        description:
          "Powdery mildew appears as white, powdery spots on leaves and stems. It thrives in warm, dry conditions with high humidity and can reduce crop yield significantly.",
        treatments: [
          "Apply sulfur or potassium bicarbonate fungicides",
          "Remove heavily infected leaves",
          "Improve air circulation around plants",
          "Water plants at the base, not from above",
          "Apply neem oil spray as a natural alternative",
        ],
      },
      {
        diseaseName: "Leaf Rust",
        cropName: "Wheat",
        confidence: 91,
        status: "Diseased",
        description:
          "Leaf rust causes orange-brown pustules on wheat leaves, reducing photosynthesis and grain quality. It spreads through wind-borne spores.",
        treatments: [
          "Apply triazole fungicides at early infection stages",
          "Use rust-resistant wheat varieties",
          "Practice crop rotation",
          "Remove volunteer wheat plants that harbor spores",
          "Monitor fields regularly for early detection",
        ],
      },
      {
        diseaseName: "Healthy",
        cropName: "Rice",
        confidence: 97,
        status: "Healthy",
        description:
          "The plant appears healthy with no visible signs of disease. Continue regular monitoring and maintain good agricultural practices.",
        treatments: [
          "Continue regular monitoring for any changes",
          "Maintain proper irrigation and drainage",
          "Apply balanced fertilizers as per soil test",
          "Practice preventive pest management",
          "Ensure proper plant spacing",
        ],
      },
    ];

    // Randomly select a disease for demo
    const randomDisease = diseases[Math.floor(Math.random() * diseases.length)];

    setIsLoading(true);
    setDetectionResult(null);

    // Simulate API delay
    setTimeout(() => {
      setDetectionResult(randomDisease);
      setIsLoading(false);

      // Scroll to results
      setTimeout(() => {
        const resultsSection = document.getElementById("results");
        if (resultsSection) {
          resultsSection.scrollIntoView({ behavior: "smooth", block: "start" });
        }
      }, 100);
    }, 2500);
  };

  const handleImageUpload = (imageData) => {
    setUploadedImage(imageData);
    setDetectionResult(null);

    if (imageData) {
      // Automatically start detection when image is uploaded
      simulateDetection();
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
