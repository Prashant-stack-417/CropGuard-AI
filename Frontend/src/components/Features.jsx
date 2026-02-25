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
    title: "Smart Detection",
    description: "Trained on thousands of real leaf images to spot diseases accurately.",
    color: "#6d6daa",
    bg: "#eeeef8",
  },
  {
    icon: SpeedOutlined,
    title: "Fast Results",
    description: "Get answers in under 3 seconds — no waiting around.",
    color: "#aa6d7a",
    bg: "#f8eef0",
  },
  {
    icon: AgricultureOutlined,
    title: "Easy to Use",
    description: "Designed for real people in the field — no tech skills required.",
    color: "#4a7c59",
    bg: "#eaf5ea",
  },
  {
    icon: PhoneAndroidOutlined,
    title: "Works on Any Device",
    description: "Use your phone in the field, tablet at home, or desktop in the office.",
    color: "#5a8a9a",
    bg: "#e8f2f5",
  },
  {
    icon: BoltOutlined,
    title: "Actionable Plans",
    description: "Don't just learn what's wrong — get clear steps for treatment.",
    color: "#9b7d4a",
    bg: "#f8f3ea",
  },
  {
    icon: PublicOutlined,
    title: "Multiple Crops",
    description: "Covers rice, wheat, tomato, cucumber, and more — growing all the time.",
    color: "#5a7a5a",
    bg: "#edf5ed",
  },
];

const Features = () => {
  return (
    <Box id="features" sx={{ py: { xs: 8, sm: 12 }, bgcolor: "#fafaf7" }}>
      <Container maxWidth="lg">
        <Stack spacing={8}>
          {/* Header */}
          <Box textAlign="center" className="animate-fade-in-up">
            <Typography variant="h2" sx={{ fontSize: { xs: "1.8rem", sm: "2.2rem" }, mb: 1.5 }}>
              What Makes It Great
            </Typography>
            <Typography variant="body1" color="text.secondary" maxWidth={520} mx="auto">
              Built to help farmers protect their crops — simple, accurate, and free
            </Typography>
          </Box>

          {/* Feature cards */}
          <Grid container spacing={3} className="stagger-children">
            {features.map((feature, index) => {
              const Icon = feature.icon;
              return (
                <Grid item xs={12} sm={6} lg={4} key={index}>
                  <Paper
                    elevation={0}
                    className="animate-fade-in-up hover-lift"
                    sx={{
                      p: 3.5,
                      height: "100%",
                      border: "1px solid rgba(0,0,0,0.06)",
                    }}
                  >
                    <Stack spacing={2}>
                      <Box
                        sx={{
                          width: 52,
                          height: 52,
                          bgcolor: feature.bg,
                          borderRadius: 2,
                          display: "flex",
                          alignItems: "center",
                          justifyContent: "center",
                        }}
                      >
                        <Icon sx={{ fontSize: 26, color: feature.color }} />
                      </Box>

                      <Typography variant="subtitle1" fontWeight={700}>
                        {feature.title}
                      </Typography>

                      <Typography variant="body2" color="text.secondary" lineHeight={1.7}>
                        {feature.description}
                      </Typography>
                    </Stack>
                  </Paper>
                </Grid>
              );
            })}
          </Grid>

          {/* CTA Banner */}
          <Paper
            elevation={0}
            className="animate-fade-in-up"
            sx={{
              p: { xs: 4, sm: 6 },
              bgcolor: "#4a7c59",
              textAlign: "center",
              borderRadius: 3,
            }}
          >
            <Stack spacing={2.5} alignItems="center">
              <Typography variant="h4" fontWeight={700} sx={{ color: "#fff", fontSize: { xs: "1.4rem", sm: "1.8rem" } }}>
                Ready to check on your crops?
              </Typography>
              <Typography variant="body1" sx={{ color: "rgba(255,255,255,0.85)", maxWidth: 420 }}>
                It's free, it's fast, and it might just save your harvest
              </Typography>
              <Button
                variant="contained"
                size="large"
                onClick={() =>
                  document.getElementById("upload")?.scrollIntoView({ behavior: "smooth" })
                }
                sx={{
                  bgcolor: "#fff",
                  color: "#4a7c59",
                  px: 5,
                  py: 1.5,
                  "&:hover": { bgcolor: "#f0f0f0" },
                }}
              >
                Get Started — It's Free
              </Button>
            </Stack>
          </Paper>
        </Stack>
      </Container>
    </Box>
  );
};

export default Features;
