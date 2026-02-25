import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import Paper from "@mui/material/Paper";
import Button from "@mui/material/Button";
import Stack from "@mui/material/Stack";
import CloudUploadOutlined from "@mui/icons-material/CloudUploadOutlined";
import SearchOutlined from "@mui/icons-material/SearchOutlined";
import AssignmentOutlined from "@mui/icons-material/AssignmentOutlined";

const steps = [
  {
    icon: CloudUploadOutlined,
    title: "Snap & Upload",
    description:
      "Take a clear photo of the leaf that looks off and drop it into our uploader.",
    color: "#4a7c59",
    bg: "#eaf5ea",
  },
  {
    icon: SearchOutlined,
    title: "We Check It Out",
    description:
      "Our system examines the image and compares it against thousands of known disease patterns.",
    color: "#6d84a0",
    bg: "#ecf0f5",
  },
  {
    icon: AssignmentOutlined,
    title: "Get Your Plan",
    description:
      "You'll receive a clear report with what's wrong, how serious it is, and what to do about it.",
    color: "#9b7d4a",
    bg: "#f8f3ea",
  },
];

const HowItWorks = () => {
  return (
    <Box id="how-it-works" sx={{ py: { xs: 8, sm: 12 }, bgcolor: "#fff" }}>
      <Container maxWidth="lg">
        <Stack spacing={8}>
          {/* Header */}
          <Box textAlign="center" className="animate-fade-in-up">
            <Typography variant="h2" sx={{ fontSize: { xs: "1.8rem", sm: "2.2rem" }, mb: 1.5 }}>
              How It Works
            </Typography>
            <Typography variant="body1" color="text.secondary" maxWidth={480} mx="auto">
              Three simple steps — no technical know-how needed
            </Typography>
          </Box>

          {/* Steps */}
          <Stack
            direction={{ xs: "column", md: "row" }}
            spacing={3}
            alignItems="stretch"
            className="stagger-children"
          >
            {steps.map((step, index) => {
              const Icon = step.icon;
              return (
                <Paper
                  key={index}
                  elevation={0}
                  className="animate-fade-in-up hover-lift"
                  sx={{
                    flex: 1,
                    p: 4,
                    textAlign: "center",
                    border: "1px solid rgba(0,0,0,0.06)",
                    position: "relative",
                    overflow: "visible",
                  }}
                >
                  {/* Step number */}
                  <Box
                    sx={{
                      position: "absolute",
                      top: -14,
                      left: "50%",
                      transform: "translateX(-50%)",
                      width: 32,
                      height: 32,
                      bgcolor: step.color,
                      color: "#fff",
                      borderRadius: "50%",
                      display: "flex",
                      alignItems: "center",
                      justifyContent: "center",
                      fontWeight: 800,
                      fontSize: "0.85rem",
                    }}
                  >
                    {index + 1}
                  </Box>

                  <Box sx={{ mt: 2, mb: 2.5 }}>
                    <Box
                      sx={{
                        width: 64,
                        height: 64,
                        bgcolor: step.bg,
                        borderRadius: 2,
                        display: "flex",
                        alignItems: "center",
                        justifyContent: "center",
                        mx: "auto",
                      }}
                    >
                      <Icon sx={{ fontSize: 30, color: step.color }} />
                    </Box>
                  </Box>

                  <Typography variant="h6" fontWeight={700} gutterBottom>
                    {step.title}
                  </Typography>
                  <Typography variant="body2" color="text.secondary" lineHeight={1.7}>
                    {step.description}
                  </Typography>
                </Paper>
              );
            })}
          </Stack>

          {/* CTA */}
          <Box textAlign="center" className="animate-fade-in-up">
            <Button
              variant="contained"
              size="large"
              onClick={() =>
                document.getElementById("upload")?.scrollIntoView({ behavior: "smooth" })
              }
              sx={{ px: 5, py: 1.5, fontSize: "1rem" }}
            >
              Give It a Try →
            </Button>
          </Box>
        </Stack>
      </Container>
    </Box>
  );
};

export default HowItWorks;
