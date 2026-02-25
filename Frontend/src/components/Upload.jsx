import { useState, useRef } from "react";
import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import Paper from "@mui/material/Paper";
import Button from "@mui/material/Button";
import Grid from "@mui/material/Grid";
import Stack from "@mui/material/Stack";
import CloudUploadOutlined from "@mui/icons-material/CloudUploadOutlined";
import CheckCircleOutline from "@mui/icons-material/CheckCircleOutline";
import LocalFloristOutlined from "@mui/icons-material/LocalFloristOutlined";
import PhotoCameraOutlined from "@mui/icons-material/PhotoCameraOutlined";
import DeleteOutlineOutlined from "@mui/icons-material/DeleteOutlineOutlined";

const Upload = ({ onImageUpload, uploadedImage }) => {
  const [isDragging, setIsDragging] = useState(false);
  const fileInputRef = useRef(null);

  const handleDragOver = (e) => { e.preventDefault(); setIsDragging(true); };
  const handleDragLeave = (e) => { e.preventDefault(); setIsDragging(false); };

  const handleDrop = (e) => {
    e.preventDefault();
    setIsDragging(false);
    const files = e.dataTransfer.files;
    if (files.length > 0) handleFileSelect(files[0]);
  };

  const handleFileSelect = (file) => {
    if (file && file.type.startsWith("image/")) {
      const reader = new FileReader();
      reader.onload = (e) => onImageUpload(e.target.result, file);
      reader.readAsDataURL(file);
    } else {
      alert("Please upload a valid image file (JPG, PNG, WEBP)");
    }
  };

  const handleFileInput = (e) => {
    const file = e.target.files[0];
    if (file) handleFileSelect(file);
  };

  const tips = [
    { icon: CheckCircleOutline, title: "Good Lighting", desc: "Natural daylight works best", color: "#4a7c59" },
    { icon: LocalFloristOutlined, title: "Single Leaf", desc: "One leaf at a time for accuracy", color: "#6a9b5e" },
    { icon: PhotoCameraOutlined, title: "Close-Up", desc: "Get close to capture details", color: "#8db580" },
  ];

  return (
    <Box id="upload" sx={{ py: { xs: 8, sm: 12 }, bgcolor: "#fff" }}>
      <Container maxWidth="lg">
        <Stack spacing={6} alignItems="center">
          {/* Header */}
          <Box textAlign="center" className="animate-fade-in-up">
            <Typography variant="h2" sx={{ fontSize: { xs: "1.8rem", sm: "2.2rem" }, mb: 1.5 }}>
              Upload Your Crop Photo
            </Typography>
            <Typography variant="body1" color="text.secondary">
              Drop an image here or click to browse — we'll take it from there
            </Typography>
          </Box>

          {/* Upload zone */}
          <Paper
            elevation={0}
            onDragOver={handleDragOver}
            onDragLeave={handleDragLeave}
            onDrop={handleDrop}
            onClick={() => fileInputRef.current?.click()}
            className="animate-fade-in-up"
            sx={{
              width: "100%",
              maxWidth: 640,
              p: { xs: 4, sm: 5 },
              border: "2px dashed",
              borderColor: isDragging ? "#4a7c59" : "#d4ddd0",
              bgcolor: isDragging ? "rgba(74, 124, 89, 0.04)" : "#fafaf7",
              borderRadius: 3,
              cursor: "pointer",
              transition: "all 0.25s ease",
              "&:hover": {
                borderColor: "#8db580",
                bgcolor: "rgba(74, 124, 89, 0.02)",
              },
            }}
          >
            <input
              ref={fileInputRef}
              type="file"
              accept="image/*"
              onChange={handleFileInput}
              style={{ display: "none" }}
            />

            {!uploadedImage ? (
              <Stack spacing={2.5} alignItems="center" sx={{ py: 3 }}>
                <Box
                  sx={{
                    width: 72,
                    height: 72,
                    borderRadius: "50%",
                    bgcolor: "rgba(74, 124, 89, 0.08)",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <CloudUploadOutlined sx={{ fontSize: 36, color: "#4a7c59" }} />
                </Box>
                <Typography variant="h6" fontWeight={600} color="text.primary">
                  {isDragging ? "Drop it right here!" : "Drag & drop your image"}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  or click anywhere to browse your files
                </Typography>
                <Button
                  variant="contained"
                  size="large"
                  onClick={(e) => {
                    e.stopPropagation();
                    fileInputRef.current?.click();
                  }}
                >
                  Choose File
                </Button>
                <Typography variant="caption" color="text.secondary">
                  Supports JPG, PNG, WEBP · Max 10 MB
                </Typography>
              </Stack>
            ) : (
              <Stack spacing={3} alignItems="center" className="animate-scale-in">
                <Box
                  component="img"
                  src={uploadedImage}
                  alt="Uploaded crop leaf"
                  sx={{
                    maxHeight: 340,
                    maxWidth: "100%",
                    borderRadius: 2,
                    boxShadow: "0 4px 16px rgba(0,0,0,0.08)",
                  }}
                />
                <Button
                  variant="outlined"
                  color="error"
                  startIcon={<DeleteOutlineOutlined />}
                  onClick={(e) => {
                    e.stopPropagation();
                    onImageUpload(null);
                  }}
                >
                  Remove & Try Another
                </Button>
              </Stack>
            )}
          </Paper>

          {/* Tip cards */}
          <Grid container spacing={3} maxWidth={640} className="stagger-children">
            {tips.map((tip, i) => {
              const Icon = tip.icon;
              return (
                <Grid item xs={12} md={4} key={i}>
                  <Paper
                    className="animate-fade-in-up hover-lift"
                    elevation={0}
                    sx={{
                      p: 2.5,
                      textAlign: "center",
                      bgcolor: "#fafaf7",
                      border: "1px solid rgba(0,0,0,0.06)",
                      height: "100%",
                    }}
                  >
                    <Icon sx={{ fontSize: 32, color: tip.color, mb: 1 }} />
                    <Typography variant="subtitle2" fontWeight={700} gutterBottom>
                      {tip.title}
                    </Typography>
                    <Typography variant="caption" color="text.secondary">
                      {tip.desc}
                    </Typography>
                  </Paper>
                </Grid>
              );
            })}
          </Grid>
        </Stack>
      </Container>
    </Box>
  );
};

export default Upload;
