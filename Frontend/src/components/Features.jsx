import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import Paper from "@mui/material/Paper";
import Button from "@mui/material/Button";
import Grid from "@mui/material/Grid";
import Stack from "@mui/material/Stack";
import PsychologyOutlined from "@mui/icons-material/PsychologyOutlined";
import SpeedOutlined from "@mui/icons-material/SpeedOutlined";
import AgricultureOutlined from "@mui/icons-material/AgricultureOutlined";
import PhoneAndroidOutlined from "@mui/icons-material/PhoneAndroidOutlined";
import BoltOutlined from "@mui/icons-material/BoltOutlined";
import PublicOutlined from "@mui/icons-material/PublicOutlined";

const features = [
  {
    icon: PsychologyOutlined,
    title: "AI-Powered Analysis",
    description:
      "Advanced deep learning models trained on thousands of crop disease images",
    gradient: "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
  },
  {
    icon: SpeedOutlined,
    title: "Fast & Accurate Detection",
    description:
      "Get results in seconds with over 95% accuracy across multiple crop types",
    gradient: "linear-gradient(135deg, #f093fb 0%, #f5576c 100%)",
  },
  {
    icon: AgricultureOutlined,
    title: "Farmer-Friendly Interface",
    description:
      "Simple, intuitive design that anyone can use without technical knowledge",
    gradient: "linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)",
  },
  {
    icon: PhoneAndroidOutlined,
    title: "Mobile Compatible",
    description: "Access from any device - smartphone, tablet, or computer",
    gradient: "linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)",
  },
  {
    icon: BoltOutlined,
    title: "Real-Time Results",
    description: "Instant disease detection and treatment recommendations",
    gradient: "linear-gradient(135deg, #fa709a 0%, #fee140 100%)",
  },
  {
    icon: PublicOutlined,
    title: "Multi-Crop Support",
    description:
      "Detects diseases across various crops including rice, wheat, tomato, and more",
    gradient: "linear-gradient(135deg, #30cfd0 0%, #330867 100%)",
  },
];

const Features = () => {
  return (
    <Box
      id="features"
      sx={{ py: { xs: 8, sm: 12 }, bgcolor: "background.default" }}
    >
      <Container maxWidth="lg">
        <Stack spacing={8}>
          <Box textAlign="center">
            <Typography variant="h2" fontWeight={700} gutterBottom>
              Powerful Features
            </Typography>
            <Typography
              variant="h6"
              color="text.secondary"
              maxWidth={700}
              mx="auto"
            >
              Everything you need for accurate crop disease detection and
              management
            </Typography>
          </Box>

          <Grid container spacing={4}>
            {features.map((feature, index) => {
              const Icon = feature.icon;
              return (
                <Grid item xs={12} sm={6} lg={4} key={index}>
                  <Paper
                    elevation={2}
                    sx={{
                      p: 4,
                      height: "100%",
                      transition: "all 0.3s",
                      "&:hover": {
                        transform: "translateY(-8px)",
                        boxShadow: 6,
                      },
                    }}
                  >
                    <Stack spacing={2}>
                      <Box
                        sx={{
                          width: 64,
                          height: 64,
                          background: feature.gradient,
                          borderRadius: 2,
                          display: "flex",
                          alignItems: "center",
                          justifyContent: "center",
                          transition: "transform 0.3s",
                          "&:hover": {
                            transform: "scale(1.1) rotate(5deg)",
                          },
                        }}
                      >
                        <Icon sx={{ fontSize: 32, color: "white" }} />
                      </Box>

                      <Typography variant="h5" fontWeight={700}>
                        {feature.title}
                      </Typography>

                      <Typography color="text.secondary">
                        {feature.description}
                      </Typography>
                    </Stack>
                  </Paper>
                </Grid>
              );
            })}
          </Grid>

          <Paper
            elevation={3}
            sx={{
              p: { xs: 4, sm: 6 },
              background: "linear-gradient(135deg, #2E7D32 0%, #1B5E20 100%)",
              color: "white",
              textAlign: "center",
            }}
          >
            <Stack spacing={3} alignItems="center">
              <Typography variant="h4" fontWeight={700}>
                Ready to protect your crops?
              </Typography>
              <Typography variant="h6" sx={{ opacity: 0.9 }}>
                Join thousands of farmers using AI for better yields
              </Typography>
              <Button
                variant="contained"
                size="large"
                onClick={() =>
                  document
                    .getElementById("upload")
                    .scrollIntoView({ behavior: "smooth" })
                }
                sx={{
                  bgcolor: "white",
                  color: "primary.main",
                  px: 6,
                  py: 2,
                  fontSize: "1.1rem",
                  textTransform: "none",
                  "&:hover": {
                    bgcolor: "grey.100",
                  },
                }}
              >
                Get Started Free
              </Button>
            </Stack>
          </Paper>
        </Stack>
      </Container>
    </Box>
  );
};

export default Features;
