import { useState, useRef } from "react";
import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import Paper from "@mui/material/Paper";
import Button from "@mui/material/Button";
import Grid from "@mui/material/Grid";
import Stack from "@mui/material/Stack";
import { alpha } from "@mui/material/styles";
import CloudUploadOutlined from "@mui/icons-material/CloudUploadOutlined";
import CheckCircleOutline from "@mui/icons-material/CheckCircleOutline";
import LocalFloristOutlined from "@mui/icons-material/LocalFloristOutlined";
import PhotoCameraOutlined from "@mui/icons-material/PhotoCameraOutlined";

const Upload = ({ onImageUpload, uploadedImage }) => {
  const [isDragging, setIsDragging] = useState(false);
  const fileInputRef = useRef(null);

  const handleDragOver = (e) => {
    e.preventDefault();
    setIsDragging(true);
  };

  const handleDragLeave = (e) => {
    e.preventDefault();
    setIsDragging(false);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    setIsDragging(false);

    const files = e.dataTransfer.files;
    if (files.length > 0) {
      handleFileSelect(files[0]);
    }
  };

  const handleFileSelect = (file) => {
    if (file && file.type.startsWith("image/")) {
      const reader = new FileReader();
      reader.onload = (e) => {
        onImageUpload(e.target.result);
      };
      reader.readAsDataURL(file);
    } else {
      alert("Please upload a valid image file (JPG, PNG)");
    }
  };

  const handleFileInput = (e) => {
    const file = e.target.files[0];
    if (file) {
      handleFileSelect(file);
    }
  };

  return (
    <Box
      id="upload"
      sx={{ py: { xs: 8, sm: 12 }, bgcolor: "background.paper" }}
    >
      <Container maxWidth="lg">
        <Stack spacing={6} alignItems="center">
          <Box textAlign="center">
            <Typography variant="h2" fontWeight={700} gutterBottom>
              Upload Crop Image
            </Typography>
            <Typography variant="h6" color="text.secondary">
              Drag and drop or click to upload a clear image of the crop leaf
            </Typography>
          </Box>

          <Paper
            elevation={isDragging ? 8 : 2}
            onDragOver={handleDragOver}
            onDragLeave={handleDragLeave}
            onDrop={handleDrop}
            onClick={() => fileInputRef.current?.click()}
            sx={{
              width: "100%",
              maxWidth: 800,
              p: 6,
              border: "3px dashed",
              borderColor: isDragging ? "primary.main" : "divider",
              bgcolor: isDragging
                ? (theme) => alpha(theme.palette.primary.main, 0.05)
                : "background.paper",
              cursor: "pointer",
              transition: "all 0.3s",
              "&:hover": {
                borderColor: "primary.main",
                bgcolor: (theme) => alpha(theme.palette.primary.main, 0.02),
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
              <Stack spacing={3} alignItems="center">
                <CloudUploadOutlined
                  sx={{ fontSize: 80, color: "primary.main" }}
                />
                <Typography variant="h5" fontWeight={600}>
                  {isDragging
                    ? "Drop your image here"
                    : "Drag & Drop your image here"}
                </Typography>
                <Typography color="text.secondary">
                  or click to browse
                </Typography>
                <Button variant="contained" size="large" sx={{ mt: 2 }}>
                  Select Image
                </Button>
                <Typography variant="body2" color="text.secondary">
                  Supported formats: JPG, PNG (Max 5MB)
                </Typography>
              </Stack>
            ) : (
              <Stack spacing={3} alignItems="center">
                <Box
                  component="img"
                  src={uploadedImage}
                  alt="Uploaded crop"
                  sx={{
                    maxHeight: 400,
                    maxWidth: "100%",
                    borderRadius: 2,
                    boxShadow: 3,
                  }}
                />
                <Button
                  variant="contained"
                  color="error"
                  onClick={(e) => {
                    e.stopPropagation();
                    onImageUpload(null);
                  }}
                >
                  Remove Image
                </Button>
              </Stack>
            )}
          </Paper>

          <Grid container spacing={3} maxWidth={800}>
            <Grid item xs={12} md={4}>
              <Paper
                sx={{
                  p: 3,
                  textAlign: "center",
                  bgcolor: "background.default",
                }}
              >
                <CheckCircleOutline
                  sx={{ fontSize: 40, color: "primary.main", mb: 1 }}
                />
                <Typography variant="h6" fontWeight={600} gutterBottom>
                  Clear Image
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  Ensure good lighting and focus
                </Typography>
              </Paper>
            </Grid>
            <Grid item xs={12} md={4}>
              <Paper
                sx={{
                  p: 3,
                  textAlign: "center",
                  bgcolor: "background.default",
                }}
              >
                <LocalFloristOutlined
                  sx={{ fontSize: 40, color: "primary.main", mb: 1 }}
                />
                <Typography variant="h6" fontWeight={600} gutterBottom>
                  Single Leaf
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  One leaf per image works best
                </Typography>
              </Paper>
            </Grid>
            <Grid item xs={12} md={4}>
              <Paper
                sx={{
                  p: 3,
                  textAlign: "center",
                  bgcolor: "background.default",
                }}
              >
                <PhotoCameraOutlined
                  sx={{ fontSize: 40, color: "primary.main", mb: 1 }}
                />
                <Typography variant="h6" fontWeight={600} gutterBottom>
                  Close-up Shot
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  Capture leaf details clearly
                </Typography>
              </Paper>
            </Grid>
          </Grid>
        </Stack>
      </Container>
    </Box>
  );
};

export default Upload;
