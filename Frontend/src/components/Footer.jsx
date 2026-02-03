import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import Grid from "@mui/material/Grid";
import Stack from "@mui/material/Stack";
import Link from "@mui/material/Link";
import IconButton from "@mui/material/IconButton";
import Spa from "@mui/icons-material/Spa";
import Facebook from "@mui/icons-material/Facebook";
import Twitter from "@mui/icons-material/Twitter";
import Instagram from "@mui/icons-material/Instagram";
import LinkedIn from "@mui/icons-material/LinkedIn";
import EmailOutlined from "@mui/icons-material/EmailOutlined";
import PhoneOutlined from "@mui/icons-material/PhoneOutlined";
import LocationOnOutlined from "@mui/icons-material/LocationOnOutlined";

const Footer = () => {
  const currentYear = new Date().getFullYear();

  const scrollToSection = (sectionId) => {
    const element = document.getElementById(sectionId);
    if (element) {
      element.scrollIntoView({ behavior: "smooth" });
    }
  };

  return (
    <Box
      id="contact"
      component="footer"
      sx={{
        bgcolor: "grey.900",
        color: "white",
        py: 6,
      }}
    >
      <Container maxWidth="lg">
        <Grid container spacing={4}>
          <Grid item xs={12} md={4}>
            <Stack spacing={2}>
              <Stack direction="row" spacing={1} alignItems="center">
                <Spa sx={{ fontSize: 32 }} />
                <Typography variant="h5" fontWeight={700}>
                  CropGuard AI
                </Typography>
              </Stack>
              <Typography color="grey.400" sx={{ maxWidth: 350 }}>
                Empowering farmers with AI-powered crop disease detection.
                Protect your harvest with instant, accurate analysis and expert
                recommendations.
              </Typography>
              <Stack direction="row" spacing={1}>
                <IconButton
                  sx={{
                    bgcolor: "grey.800",
                    color: "white",
                    "&:hover": { bgcolor: "primary.main" },
                  }}
                >
                  <Facebook />
                </IconButton>
                <IconButton
                  sx={{
                    bgcolor: "grey.800",
                    color: "white",
                    "&:hover": { bgcolor: "primary.main" },
                  }}
                >
                  <Twitter />
                </IconButton>
                <IconButton
                  sx={{
                    bgcolor: "grey.800",
                    color: "white",
                    "&:hover": { bgcolor: "primary.main" },
                  }}
                >
                  <Instagram />
                </IconButton>
                <IconButton
                  sx={{
                    bgcolor: "grey.800",
                    color: "white",
                    "&:hover": { bgcolor: "primary.main" },
                  }}
                >
                  <LinkedIn />
                </IconButton>
              </Stack>
            </Stack>
          </Grid>

          <Grid item xs={12} sm={6} md={3}>
            <Typography variant="h6" fontWeight={600} gutterBottom>
              Quick Links
            </Typography>
            <Stack spacing={1}>
              <Link
                component="button"
                variant="body2"
                onClick={() => scrollToSection("home")}
                sx={{
                  color: "grey.400",
                  textAlign: "left",
                  textDecoration: "none",
                  "&:hover": { color: "primary.main" },
                }}
              >
                Home
              </Link>
              <Link
                component="button"
                variant="body2"
                onClick={() => scrollToSection("upload")}
                sx={{
                  color: "grey.400",
                  textAlign: "left",
                  textDecoration: "none",
                  "&:hover": { color: "primary.main" },
                }}
              >
                Upload Image
              </Link>
              <Link
                component="button"
                variant="body2"
                onClick={() => scrollToSection("how-it-works")}
                sx={{
                  color: "grey.400",
                  textAlign: "left",
                  textDecoration: "none",
                  "&:hover": { color: "primary.main" },
                }}
              >
                How It Works
              </Link>
              <Link
                component="button"
                variant="body2"
                onClick={() => scrollToSection("features")}
                sx={{
                  color: "grey.400",
                  textAlign: "left",
                  textDecoration: "none",
                  "&:hover": { color: "primary.main" },
                }}
              >
                Features
              </Link>
            </Stack>
          </Grid>

          <Grid item xs={12} sm={6} md={5}>
            <Typography variant="h6" fontWeight={600} gutterBottom>
              Contact
            </Typography>
            <Stack spacing={2}>
              <Stack direction="row" spacing={1} alignItems="center">
                <EmailOutlined sx={{ color: "grey.400" }} />
                <Typography color="grey.400">support@cropguard.ai</Typography>
              </Stack>
              <Stack direction="row" spacing={1} alignItems="center">
                <PhoneOutlined sx={{ color: "grey.400" }} />
                <Typography color="grey.400">+1 (555) 123-4567</Typography>
              </Stack>
              <Stack direction="row" spacing={1} alignItems="center">
                <LocationOnOutlined sx={{ color: "grey.400" }} />
                <Typography color="grey.400">Agriculture Tech Hub</Typography>
              </Stack>
            </Stack>
          </Grid>
        </Grid>

        <Box
          sx={{
            borderTop: 1,
            borderColor: "grey.800",
            mt: 6,
            pt: 4,
            textAlign: "center",
          }}
        >
          <Typography color="grey.400" variant="body2">
            © {currentYear} CropGuard AI. All rights reserved. | Powered by
            Advanced Machine Learning
          </Typography>
          <Stack
            direction="row"
            spacing={2}
            justifyContent="center"
            sx={{ mt: 2 }}
          >
            <Link
              href="#"
              variant="body2"
              sx={{
                color: "grey.400",
                textDecoration: "none",
                "&:hover": { color: "primary.main" },
              }}
            >
              Privacy Policy
            </Link>
            <Typography color="grey.600">•</Typography>
            <Link
              href="#"
              variant="body2"
              sx={{
                color: "grey.400",
                textDecoration: "none",
                "&:hover": { color: "primary.main" },
              }}
            >
              Terms of Service
            </Link>
            <Typography color="grey.600">•</Typography>
            <Link
              href="#"
              variant="body2"
              sx={{
                color: "grey.400",
                textDecoration: "none",
                "&:hover": { color: "primary.main" },
              }}
            >
              Cookie Policy
            </Link>
          </Stack>
        </Box>
      </Container>
    </Box>
  );
};

export default Footer;
