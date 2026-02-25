import { useState, useEffect } from "react";
import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import IconButton from "@mui/material/IconButton";
import Typography from "@mui/material/Typography";
import Menu from "@mui/material/Menu";
import MenuIcon from "@mui/icons-material/Menu";
import Container from "@mui/material/Container";
import Button from "@mui/material/Button";
import MenuItem from "@mui/material/MenuItem";
import Spa from "@mui/icons-material/Spa";

const pages = [
  { name: "Home", id: "home" },
  { name: "Upload", id: "upload" },
  { name: "How It Works", id: "how-it-works" },
  { name: "Features", id: "features" },
  { name: "Contact", id: "contact" },
];

const Navbar = () => {
  const [anchorElNav, setAnchorElNav] = useState(null);
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 40);
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  const handleOpenNavMenu = (e) => setAnchorElNav(e.currentTarget);
  const handleCloseNavMenu = () => setAnchorElNav(null);

  const scrollToSection = (id) => {
    document.getElementById(id)?.scrollIntoView({ behavior: "smooth" });
    handleCloseNavMenu();
  };

  return (
    <AppBar
      position="sticky"
      elevation={0}
      sx={{
        bgcolor: scrolled ? "rgba(255, 255, 255, 0.95)" : "#fff",
        borderBottom: "1px solid",
        borderColor: scrolled ? "rgba(0,0,0,0.08)" : "transparent",
        transition: "all 0.3s ease",
      }}
    >
      <Container maxWidth="xl">
        <Toolbar disableGutters sx={{ py: 0.5 }}>
          {/* Brand (desktop) */}
          <Box
            onClick={() => scrollToSection("home")}
            sx={{
              display: { xs: "none", md: "flex" },
              alignItems: "center",
              gap: 1,
              cursor: "pointer",
              mr: 4,
            }}
          >
            <Spa sx={{ fontSize: 26, color: "#4a7c59" }} />
            <Typography
              variant="h6"
              noWrap
              sx={{ fontWeight: 800, color: "#2d3a2d", letterSpacing: "-0.02em" }}
            >
              CropGuard
            </Typography>
          </Box>

          {/* Mobile hamburger */}
          <Box sx={{ flexGrow: 1, display: { xs: "flex", md: "none" } }}>
            <IconButton size="large" onClick={handleOpenNavMenu} sx={{ color: "#2d3a2d" }}>
              <MenuIcon />
            </IconButton>
            <Menu
              anchorEl={anchorElNav}
              anchorOrigin={{ vertical: "bottom", horizontal: "left" }}
              keepMounted
              transformOrigin={{ vertical: "top", horizontal: "left" }}
              open={Boolean(anchorElNav)}
              onClose={handleCloseNavMenu}
              sx={{ display: { xs: "block", md: "none" } }}
            >
              {pages.map((page) => (
                <MenuItem key={page.id} onClick={() => scrollToSection(page.id)}>
                  <Typography>{page.name}</Typography>
                </MenuItem>
              ))}
            </Menu>
          </Box>

          {/* Brand (mobile) */}
          <Box
            onClick={() => scrollToSection("home")}
            sx={{
              display: { xs: "flex", md: "none" },
              alignItems: "center",
              gap: 1,
              cursor: "pointer",
              flexGrow: 1,
            }}
          >
            <Spa sx={{ fontSize: 22, color: "#4a7c59" }} />
            <Typography variant="h6" noWrap sx={{ fontWeight: 800, color: "#2d3a2d" }}>
              CropGuard
            </Typography>
          </Box>

          {/* Desktop nav links */}
          <Box
            sx={{
              flexGrow: 1,
              display: { xs: "none", md: "flex" },
              justifyContent: "flex-end",
              gap: 0.5,
            }}
          >
            {pages.map((page) => (
              <Button
                key={page.id}
                onClick={() => scrollToSection(page.id)}
                sx={{
                  color: "#6b7c6b",
                  fontSize: "0.9rem",
                  px: 2,
                  py: 1,
                  borderRadius: 2,
                  "&:hover": {
                    color: "#4a7c59",
                    bgcolor: "rgba(74, 124, 89, 0.06)",
                  },
                }}
              >
                {page.name}
              </Button>
            ))}
          </Box>
        </Toolbar>
      </Container>
    </AppBar>
  );
};

export default Navbar;
