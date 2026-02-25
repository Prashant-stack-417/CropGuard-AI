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

  const scrollToSection = (id) => {
    document.getElementById(id)?.scrollIntoView({ behavior: "smooth" });
  };

  const socialIcons = [
    { icon: Facebook, label: "Facebook" },
    { icon: Twitter, label: "Twitter" },
    { icon: Instagram, label: "Instagram" },
    { icon: LinkedIn, label: "LinkedIn" },
  ];

  const quickLinks = [
    { name: "Home", id: "home" },
    { name: "Upload Image", id: "upload" },
    { name: "How It Works", id: "how-it-works" },
    { name: "Features", id: "features" },
  ];

  const contactInfo = [
    { icon: EmailOutlined, text: "support@cropguard.ai" },
    { icon: PhoneOutlined, text: "+1 (555) 123-4567" },
    { icon: LocationOnOutlined, text: "Agriculture Tech Hub, CA" },
  ];

  return (
    <Box id="contact" component="footer" sx={{ bgcolor: "#2d3a2d", color: "#fff", py: 6 }}>
      <Container maxWidth="lg">
        <Grid container spacing={5}>
          {/* Brand */}
          <Grid item xs={12} md={4}>
            <Stack spacing={2}>
              <Stack
                direction="row"
                spacing={1}
                alignItems="center"
                onClick={() => scrollToSection("home")}
                sx={{ cursor: "pointer" }}
              >
                <Spa sx={{ fontSize: 28, color: "#8db580" }} />
                <Typography variant="h5" fontWeight={800}>
                  CropGuard
                </Typography>
              </Stack>
              <Typography sx={{ color: "rgba(255,255,255,0.6)", maxWidth: 300, lineHeight: 1.7, fontSize: "0.875rem" }}>
                Helping farmers protect their crops with smart disease detection.
                Simple, accurate, and built for real people.
              </Typography>
              <Stack direction="row" spacing={1}>
                {socialIcons.map((social) => {
                  const SIcon = social.icon;
                  return (
                    <IconButton
                      key={social.label}
                      aria-label={social.label}
                      sx={{
                        color: "rgba(255,255,255,0.5)",
                        border: "1px solid rgba(255,255,255,0.1)",
                        "&:hover": {
                          bgcolor: "rgba(255,255,255,0.08)",
                          color: "#8db580",
                          borderColor: "rgba(141, 181, 128, 0.3)",
                        },
                        transition: "all 0.2s ease",
                      }}
                      size="small"
                    >
                      <SIcon fontSize="small" />
                    </IconButton>
                  );
                })}
              </Stack>
            </Stack>
          </Grid>

          {/* Quick Links */}
          <Grid item xs={12} sm={6} md={3}>
            <Typography variant="subtitle2" fontWeight={700} sx={{ mb: 2, color: "rgba(255,255,255,0.9)" }}>
              Quick Links
            </Typography>
            <Stack spacing={1.5}>
              {quickLinks.map((link) => (
                <Link
                  key={link.id}
                  component="button"
                  variant="body2"
                  onClick={() => scrollToSection(link.id)}
                  sx={{
                    color: "rgba(255,255,255,0.5)",
                    textAlign: "left",
                    textDecoration: "none",
                    transition: "color 0.2s ease",
                    "&:hover": { color: "#8db580" },
                  }}
                >
                  {link.name}
                </Link>
              ))}
            </Stack>
          </Grid>

          {/* Contact */}
          <Grid item xs={12} sm={6} md={5}>
            <Typography variant="subtitle2" fontWeight={700} sx={{ mb: 2, color: "rgba(255,255,255,0.9)" }}>
              Get in Touch
            </Typography>
            <Stack spacing={2}>
              {contactInfo.map((item) => {
                const CIcon = item.icon;
                return (
                  <Stack key={item.text} direction="row" spacing={1.5} alignItems="center">
                    <CIcon sx={{ fontSize: 18, color: "#8db580" }} />
                    <Typography variant="body2" sx={{ color: "rgba(255,255,255,0.5)" }}>
                      {item.text}
                    </Typography>
                  </Stack>
                );
              })}
            </Stack>
          </Grid>
        </Grid>

        {/* Bottom bar */}
        <Box
          sx={{
            borderTop: "1px solid rgba(255,255,255,0.08)",
            mt: 5,
            pt: 3,
            display: "flex",
            flexDirection: { xs: "column", sm: "row" },
            justifyContent: "space-between",
            alignItems: "center",
            gap: 2,
          }}
        >
          <Typography variant="caption" sx={{ color: "rgba(255,255,255,0.4)" }}>
            © {currentYear} CropGuard. All rights reserved.
          </Typography>
          <Stack direction="row" spacing={2}>
            {["Privacy Policy", "Terms of Service"].map((text) => (
              <Link
                key={text}
                href="#"
                variant="caption"
                sx={{
                  color: "rgba(255,255,255,0.4)",
                  textDecoration: "none",
                  "&:hover": { color: "#8db580" },
                }}
              >
                {text}
              </Link>
            ))}
          </Stack>
        </Box>
      </Container>
    </Box>
  );
};

export default Footer;
