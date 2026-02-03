import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import Button from "@mui/material/Button";
import Grid from "@mui/material/Grid";
import Stack from "@mui/material/Stack";
import { alpha } from "@mui/material/styles";
import CameraAltOutlined from "@mui/icons-material/CameraAltOutlined";
import InfoOutlined from "@mui/icons-material/InfoOutlined";
import ScienceOutlined from "@mui/icons-material/ScienceOutlined";

const Hero = ({ onUploadClick }) => {
  return (
    <Box
      id="home"
      sx={{
        pt: { xs: 12, sm: 16 },
        pb: { xs: 8, sm: 12 },
        background: (theme) =>
          `linear-gradient(135deg, ${alpha(theme.palette.primary.main, 0.05)} 0%, ${alpha(theme.palette.secondary.main, 0.15)} 100%)`,
        position: "relative",
        overflow: "hidden",
      }}
    >
      <Container>
        <Grid container spacing={6} alignItems="center">
          <Grid item xs={12} md={6}>
            <Stack spacing={4}>
              <Typography
                variant="h1"
                sx={{
                  fontSize: { xs: "2.5rem", sm: "3.5rem", md: "4rem" },
                  fontWeight: 800,
                  color: "text.primary",
                  lineHeight: 1.2,
                }}
              >
                Detect Crop Diseases{" "}
                <Typography
                  component="span"
                  sx={{
                    fontSize: "inherit",
                    fontWeight: "inherit",
                    color: "primary.main",
                  }}
                >
                  Instantly
                </Typography>{" "}
                Using AI
              </Typography>

              <Typography
                variant="h5"
                color="text.secondary"
                sx={{ maxWidth: 600 }}
              >
                Empower your farming with cutting-edge artificial intelligence.
                Upload a leaf image and get accurate disease detection,
                confidence scores, and expert treatment recommendations in
                seconds.
              </Typography>

              <Stack direction={{ xs: "column", sm: "row" }} spacing={2}>
                <Button
                  variant="contained"
                  size="large"
                  startIcon={<CameraAltOutlined />}
                  onClick={onUploadClick}
                  sx={{
                    py: 1.5,
                    px: 4,
                    fontSize: "1.1rem",
                    textTransform: "none",
                    borderRadius: 2,
                  }}
                >
                  Upload Leaf Image
                </Button>
                <Button
                  variant="outlined"
                  size="large"
                  startIcon={<InfoOutlined />}
                  onClick={() =>
                    document
                      .getElementById("how-it-works")
                      .scrollIntoView({ behavior: "smooth" })
                  }
                  sx={{
                    py: 1.5,
                    px: 4,
                    fontSize: "1.1rem",
                    textTransform: "none",
                    borderRadius: 2,
                  }}
                >
                  How It Works
                </Button>
              </Stack>
            </Stack>
          </Grid>
          <Grid
            item
            xs={12}
            md={6}
            sx={{ display: { xs: "none", md: "block" } }}
          >
            <Box
              sx={{
                position: "relative",
                height: 400,
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
              }}
            >
              <Box
                sx={{
                  width: "100%",
                  height: "100%",
                  bgcolor: alpha("#fff", 0.5),
                  backdropFilter: "blur(20px)",
                  borderRadius: 4,
                  border: "4px solid",
                  borderColor: (theme) =>
                    alpha(theme.palette.primary.main, 0.2),
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "center",
                  boxShadow: 3,
                }}
              >
                <Stack alignItems="center" spacing={2}>
                  <ScienceOutlined
                    sx={{ fontSize: 120, color: "primary.main" }}
                  />
                  <Typography
                    variant="h5"
                    fontWeight={600}
                    color="text.primary"
                  >
                    AI-Powered Detection
                  </Typography>
                </Stack>
              </Box>
            </Box>
          </Grid>
        </Grid>
      </Container>
    </Box>
  );
};

export default Hero;
