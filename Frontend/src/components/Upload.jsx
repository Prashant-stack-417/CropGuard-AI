import { useCallback, useEffect, useRef, useState } from "react";
import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import Paper from "@mui/material/Paper";
import Button from "@mui/material/Button";
import Grid from "@mui/material/Grid";
import Stack from "@mui/material/Stack";
import Alert from "@mui/material/Alert";
import ToggleButton from "@mui/material/ToggleButton";
import ToggleButtonGroup from "@mui/material/ToggleButtonGroup";
import CloudUploadOutlined from "@mui/icons-material/CloudUploadOutlined";
import CheckCircleOutline from "@mui/icons-material/CheckCircleOutline";
import LocalFloristOutlined from "@mui/icons-material/LocalFloristOutlined";
import PhotoCameraOutlined from "@mui/icons-material/PhotoCameraOutlined";
import DeleteOutlineOutlined from "@mui/icons-material/DeleteOutlineOutlined";
import VideocamOutlined from "@mui/icons-material/VideocamOutlined";
import StopCircleOutlined from "@mui/icons-material/StopCircleOutlined";

const Upload = ({
  onImageUpload,
  uploadedImage,
  onRealtimeFrame,
  onRealtimeStateChange,
  isRealtimeActive,
}) => {
  const [isDragging, setIsDragging] = useState(false);
  const [mode, setMode] = useState("upload");
  const [cameraError, setCameraError] = useState("");
  const fileInputRef = useRef(null);
  const videoRef = useRef(null);
  const streamRef = useRef(null);
  const captureIntervalRef = useRef(null);
  const canvasRef = useRef(null);

  const stopRealtime = useCallback(() => {
    if (captureIntervalRef.current) {
      clearInterval(captureIntervalRef.current);
      captureIntervalRef.current = null;
    }

    if (streamRef.current) {
      streamRef.current.getTracks().forEach((track) => track.stop());
      streamRef.current = null;
    }

    if (videoRef.current) {
      videoRef.current.srcObject = null;
    }

    onRealtimeStateChange(false);
  }, [onRealtimeStateChange]);

  useEffect(() => () => stopRealtime(), [stopRealtime]);

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

  const captureFrameAndPredict = useCallback(() => {
    if (!videoRef.current || !canvasRef.current || !onRealtimeFrame) return;
    if (videoRef.current.videoWidth === 0 || videoRef.current.videoHeight === 0) return;

    const canvas = canvasRef.current;
    const video = videoRef.current;

    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    const ctx = canvas.getContext("2d", { willReadFrequently: true });
    if (!ctx) return;

    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
    canvas.toBlob(
      (blob) => {
        if (!blob) return;
        const frameFile = new File([blob], `realtime-frame-${Date.now()}.jpg`, { type: "image/jpeg" });
        onRealtimeFrame(frameFile);
      },
      "image/jpeg",
      0.88
    );
  }, [onRealtimeFrame]);

  const getCameraErrorMessage = (error) => {
    if (!window.isSecureContext) {
      return "Camera requires a secure context. Use HTTPS or localhost and try again.";
    }

    if (error?.name === "NotAllowedError" || error?.name === "SecurityError") {
      return "Camera access was blocked. Allow camera permission in browser site settings and OS privacy settings for your browser, then retry.";
    }

    if (error?.name === "NotFoundError" || error?.name === "DevicesNotFoundError") {
      return "No camera device was found. Connect a camera and try again.";
    }

    if (error?.name === "NotReadableError" || error?.name === "TrackStartError") {
      return "Camera is in use by another app. Close other apps using the camera and retry.";
    }

    if (error?.name === "OverconstrainedError") {
      return "Camera constraints were not supported on this device. Try another camera or browser.";
    }

    return "Unable to access the camera. Please check permissions and try again.";
  };

  const startRealtime = async () => {
    if (!navigator.mediaDevices?.getUserMedia) {
      setCameraError("This browser does not support camera access.");
      return;
    }

    try {
      stopRealtime();
      setCameraError("");

      const cameraConstraints = [
        {
          video: {
            facingMode: { ideal: "environment" },
            width: { ideal: 1280 },
            height: { ideal: 720 },
          },
          audio: false,
        },
        {
          video: { facingMode: "user" },
          audio: false,
        },
        {
          video: true,
          audio: false,
        },
      ];

      let stream;
      let lastError;
      for (const constraints of cameraConstraints) {
        try {
          stream = await navigator.mediaDevices.getUserMedia(constraints);
          break;
        } catch (error) {
          lastError = error;
          if (error?.name === "NotAllowedError" || error?.name === "SecurityError") {
            throw error;
          }
        }
      }

      if (!stream) {
        throw lastError || new Error("Unable to access camera");
      }

      streamRef.current = stream;
      if (videoRef.current) {
        videoRef.current.srcObject = stream;
        videoRef.current.setAttribute("playsinline", "true");
        await new Promise((resolve) => {
          if (videoRef.current.readyState >= 1) {
            resolve();
            return;
          }
          const onLoadedMetadata = () => {
            videoRef.current?.removeEventListener("loadedmetadata", onLoadedMetadata);
            resolve();
          };
          videoRef.current.addEventListener("loadedmetadata", onLoadedMetadata, { once: true });
        });
        await videoRef.current.play();
      }

      onImageUpload(null);
      onRealtimeStateChange(true);

      captureFrameAndPredict();
      captureIntervalRef.current = setInterval(captureFrameAndPredict, 1800);
    } catch (error) {
      console.error("Unable to start camera:", error);
      setCameraError(getCameraErrorMessage(error));
      stopRealtime();
    }
  };

  const handleModeChange = (_event, newMode) => {
    if (!newMode) return;
    setMode(newMode);
    if (newMode === "upload") {
      stopRealtime();
    }
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
              Drop an image here or use live camera mode for real-time analysis
            </Typography>
          </Box>

          <ToggleButtonGroup
            value={mode}
            exclusive
            onChange={handleModeChange}
            color="primary"
            className="animate-fade-in-up"
            sx={{
              bgcolor: "#f3f6ef",
              borderRadius: 2,
              border: "1px solid rgba(74, 124, 89, 0.12)",
              "& .MuiToggleButton-root": {
                px: 2.5,
                py: 1,
                border: 0,
                fontWeight: 600,
              },
            }}
          >
            <ToggleButton value="upload">Upload Image</ToggleButton>
            <ToggleButton value="realtime">Real-Time Camera</ToggleButton>
          </ToggleButtonGroup>

          {/* Upload zone */}
          <Paper
            elevation={0}
            onDragOver={mode === "upload" ? handleDragOver : undefined}
            onDragLeave={mode === "upload" ? handleDragLeave : undefined}
            onDrop={mode === "upload" ? handleDrop : undefined}
            onClick={mode === "upload" ? () => fileInputRef.current?.click() : undefined}
            className="animate-fade-in-up"
            sx={{
              width: "100%",
              maxWidth: 640,
              p: { xs: 4, sm: 5 },
              border: "2px dashed",
              borderColor: mode === "upload" && isDragging ? "#4a7c59" : "#d4ddd0",
              bgcolor: mode === "upload" && isDragging ? "rgba(74, 124, 89, 0.04)" : "#fafaf7",
              borderRadius: 3,
              cursor: mode === "upload" ? "pointer" : "default",
              transition: "all 0.25s ease",
              "&:hover": {
                borderColor: mode === "upload" ? "#8db580" : "#d4ddd0",
                bgcolor: mode === "upload" ? "rgba(74, 124, 89, 0.02)" : "#fafaf7",
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

            <canvas ref={canvasRef} style={{ display: "none" }} />

            {mode === "upload" && !uploadedImage ? (
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
            ) : null}

            {mode === "upload" && uploadedImage ? (
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
            ) : null}

            {mode === "realtime" ? (
              <Stack spacing={2.5} alignItems="center">
                {cameraError ? <Alert severity="error" sx={{ width: "100%" }}>{cameraError}</Alert> : null}

                <Box
                  sx={{
                    width: "100%",
                    borderRadius: 2,
                    overflow: "hidden",
                    border: "1px solid rgba(0,0,0,0.08)",
                    bgcolor: "#0f1a12",
                    minHeight: { xs: 220, sm: 320 },
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <video
                    ref={videoRef}
                    autoPlay
                    muted
                    playsInline
                    style={{ width: "100%", display: isRealtimeActive ? "block" : "none" }}
                  />
                  {!isRealtimeActive ? (
                    <Typography variant="body2" sx={{ color: "#d9e2d5" }}>
                      Start camera to begin live prediction
                    </Typography>
                  ) : null}
                </Box>

                <Stack direction={{ xs: "column", sm: "row" }} spacing={1.5}>
                  {!isRealtimeActive ? (
                    <Button
                      variant="contained"
                      startIcon={<VideocamOutlined />}
                      onClick={startRealtime}
                    >
                      Start Real-Time Analysis
                    </Button>
                  ) : (
                    <Button
                      variant="outlined"
                      color="error"
                      startIcon={<StopCircleOutlined />}
                      onClick={stopRealtime}
                    >
                      Stop Camera
                    </Button>
                  )}
                </Stack>

                <Typography variant="caption" color="text.secondary">
                  Camera captures frames every ~2 seconds and updates the prediction in real time.
                </Typography>
              </Stack>
            ) : null}
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
