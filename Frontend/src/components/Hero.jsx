import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import Button from "@mui/material/Button";
import Stack from "@mui/material/Stack";
import CameraAltOutlined from "@mui/icons-material/CameraAltOutlined";
import InfoOutlined from "@mui/icons-material/InfoOutlined";

const Hero = ({ onUploadClick }) => {
  return (
    <Box
      id="home"
      sx={{
        pt: { xs: 10, sm: 14 },
        pb: { xs: 8, sm: 12 },
        background: "linear-gradient(170deg, #f4f7f0 0%, #e8f0e0 40%, #fafaf7 100%)",
        position: "relative",
        overflow: "hidden",
      }}
    >
      {/* Soft decorative shape */}
      <Box
        sx={{
          position: "absolute",
          top: -100,
          right: -100,
          width: 400,
          height: 400,
          borderRadius: "50%",
          background: "rgba(74, 124, 89, 0.05)",
          pointerEvents: "none",
        }}
      />

      <Container sx={{ position: "relative", zIndex: 1 }}>
        <Stack
          spacing={4}
          alignItems="center"
          textAlign="center"
          maxWidth={720}
          mx="auto"
        >
          {/* Badge */}
          <Box
            className="animate-fade-in-up"
            sx={{
              display: "inline-flex",
              alignItems: "center",
              gap: 1,
              bgcolor: "rgba(74, 124, 89, 0.08)",
              borderRadius: 3,
              px: 2.5,
              py: 0.75,
            }}
          >
            <Typography
              variant="body2"
              sx={{ color: "#4a7c59", fontWeight: 600, letterSpacing: 0.3 }}
            >
              🌿 Smart Crop Protection
            </Typography>
          </Box>

          {/* Heading */}
          <Typography
            variant="h1"
            className="animate-fade-in-up"
            sx={{
              fontSize: { xs: "2.2rem", sm: "3rem", md: "3.5rem" },
              lineHeight: 1.2,
            }}
          >
            Keep your crops healthy,{" "}
            <Typography
              component="span"
              sx={{
                fontSize: "inherit",
                fontWeight: "inherit",
                letterSpacing: "inherit",
                color: "#4a7c59",
              }}
            >
              naturally
            </Typography>
          </Typography>

          {/* Subtitle */}
          <Typography
            variant="h6"
            className="animate-fade-in-up"
            sx={{
              color: "text.secondary",
              fontWeight: 400,
              lineHeight: 1.7,
              maxWidth: 560,
              fontSize: { xs: "1rem", sm: "1.1rem" },
            }}
          >
            Take a photo of any leaf that looks off. We'll help you figure out
            what's going on and how to treat it — simple as that.
          </Typography>

          {/* CTA buttons */}
          <Stack
            className="animate-fade-in-up"
            direction={{ xs: "column", sm: "row" }}
            spacing={2}
          >
            <Button
              variant="contained"
              size="large"
              startIcon={<CameraAltOutlined />}
              onClick={onUploadClick}
              sx={{ py: 1.5, px: 4, fontSize: "1.05rem" }}
            >
              Upload a Leaf Photo
            </Button>
            <Button
              variant="outlined"
              size="large"
              startIcon={<InfoOutlined />}
              onClick={() =>
                document
                  .getElementById("how-it-works")
                  ?.scrollIntoView({ behavior: "smooth" })
              }
              sx={{ py: 1.5, px: 4, fontSize: "1.05rem" }}
            >
              Learn More
            </Button>
          </Stack>

          {/* Stats row */}
          <Stack
            className="animate-fade-in-up"
            direction="row"
            spacing={{ xs: 3, sm: 6 }}
            sx={{ pt: 3 }}
          >
            {[
              { value: "95%+", label: "Accuracy" },
              { value: "< 3s", label: "Results" },
              { value: "10+", label: "Crop Types" },
            ].map((stat) => (
              <Box key={stat.label} textAlign="center">
                <Typography variant="h4" sx={{ fontWeight: 800, color: "#4a7c59" }}>
                  {stat.value}
                </Typography>
                <Typography variant="body2" sx={{ color: "text.secondary", mt: 0.25 }}>
                  {stat.label}
                </Typography>
              </Box>
            ))}
          </Stack>
        </Stack>
      </Container>
    </Box>
  );
};

export default Hero;
