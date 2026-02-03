import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import Paper from "@mui/material/Paper";
import Button from "@mui/material/Button";
import Grid from "@mui/material/Grid";
import Stack from "@mui/material/Stack";
import CloudUploadOutlined from "@mui/icons-material/CloudUploadOutlined";
import SmartToyOutlined from "@mui/icons-material/SmartToyOutlined";
import AssessmentOutlined from "@mui/icons-material/AssessmentOutlined";
import ArrowForwardOutlined from "@mui/icons-material/ArrowForwardOutlined";

const steps = [
  {
    icon: CloudUploadOutlined,
    title: "Upload Crop Image",
    description:
      "Take a clear photo of the affected crop leaf and upload it to our platform",
    color: "#2196F3",
  },
  {
    icon: SmartToyOutlined,
    title: "AI Analyzes Leaf",
    description:
      "Our advanced AI model processes the image and identifies potential diseases",
    color: "#9C27B0",
  },
  {
    icon: AssessmentOutlined,
    title: "Get Disease Report",
    description:
      "Receive detailed analysis with disease name, confidence score, and treatment options",
    color: "#4CAF50",
  },
];

const HowItWorks = () => {
  return (
    <Box
      id="how-it-works"
      sx={{ py: { xs: 8, sm: 12 }, bgcolor: "background.paper" }}
    >
      <Container maxWidth="lg">
        <Stack spacing={8}>
          <Box textAlign="center">
            <Typography variant="h2" fontWeight={700} gutterBottom>
              How It Works
            </Typography>
            <Typography
              variant="h6"
              color="text.secondary"
              maxWidth={600}
              mx="auto"
            >
              Get accurate crop disease detection in three simple steps
            </Typography>
          </Box>

          <Grid container spacing={4} alignItems="stretch">
            {steps.map((step, index) => {
              const Icon = step.icon;
              return (
                <Grid item xs={12} md={4} key={index}>
                  <Paper
                    elevation={2}
                    sx={{
                      p: 4,
                      height: "100%",
                      position: "relative",
                      textAlign: "center",
                      transition: "all 0.3s",
                      "&:hover": {
                        transform: "translateY(-8px)",
                        boxShadow: 6,
                      },
                    }}
                  >
                    <Box
                      sx={{
                        position: "absolute",
                        top: -20,
                        left: "50%",
                        transform: "translateX(-50%)",
                        width: 50,
                        height: 50,
                        bgcolor: "primary.main",
                        color: "white",
                        borderRadius: "50%",
                        display: "flex",
                        alignItems: "center",
                        justifyContent: "center",
                        fontWeight: 700,
                        fontSize: "1.5rem",
                        boxShadow: 3,
                      }}
                    >
                      {index + 1}
                    </Box>

                    <Box sx={{ mt: 3, mb: 3 }}>
                      <Box
                        sx={{
                          width: 80,
                          height: 80,
                          bgcolor: step.color,
                          borderRadius: 2,
                          display: "flex",
                          alignItems: "center",
                          justifyContent: "center",
                          mx: "auto",
                        }}
                      >
                        <Icon sx={{ fontSize: 40, color: "white" }} />
                      </Box>
                    </Box>

                    <Typography variant="h5" fontWeight={700} gutterBottom>
                      {step.title}
                    </Typography>
                    <Typography color="text.secondary">
                      {step.description}
                    </Typography>
                  </Paper>

                  {index < steps.length - 1 && (
                    <Box
                      sx={{
                        display: { xs: "none", md: "flex" },
                        position: "absolute",
                        right: -40,
                        top: "50%",
                        transform: "translateY(-50%)",
                      }}
                    >
                      <ArrowForwardOutlined
                        sx={{ fontSize: 40, color: "text.disabled" }}
                      />
                    </Box>
                  )}
                </Grid>
              );
            })}
          </Grid>

          <Box textAlign="center">
            <Button
              variant="contained"
              size="large"
              onClick={() =>
                document
                  .getElementById("upload")
                  .scrollIntoView({ behavior: "smooth" })
              }
              sx={{ px: 6, py: 2, fontSize: "1.1rem", textTransform: "none" }}
            >
              Try It Now →
            </Button>
          </Box>
        </Stack>
      </Container>
    </Box>
  );
};

export default HowItWorks;
