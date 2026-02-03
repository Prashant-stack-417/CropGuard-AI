import { useState } from "react";
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
  { name: "Upload Image", id: "upload" },
  { name: "How It Works", id: "how-it-works" },
  { name: "Features", id: "features" },
  { name: "Contact", id: "contact" },
];

const Navbar = () => {
  const [anchorElNav, setAnchorElNav] = useState(null);

  const handleOpenNavMenu = (event) => {
    setAnchorElNav(event.currentTarget);
  };

  const handleCloseNavMenu = () => {
    setAnchorElNav(null);
  };

  const scrollToSection = (sectionId) => {
    const element = document.getElementById(sectionId);
    if (element) {
      element.scrollIntoView({ behavior: "smooth" });
      handleCloseNavMenu();
    }
  };

  return (
    <AppBar
      position="sticky"
      color="default"
      elevation={1}
      sx={{ bgcolor: "rgba(255, 255, 255, 0.9)", backdropFilter: "blur(10px)" }}
    >
      <Container maxWidth="xl">
        <Toolbar disableGutters>
          <Spa
            sx={{
              display: { xs: "none", md: "flex" },
              mr: 1,
              color: "primary.main",
            }}
          />
          <Typography
            variant="h6"
            noWrap
            component="div"
            onClick={() => scrollToSection("home")}
            sx={{
              mr: 2,
              display: { xs: "none", md: "flex" },
              fontWeight: 700,
              color: "primary.main",
              cursor: "pointer",
            }}
          >
            CropGuard AI
          </Typography>

          <Box sx={{ flexGrow: 1, display: { xs: "flex", md: "none" } }}>
            <IconButton
              size="large"
              onClick={handleOpenNavMenu}
              color="inherit"
            >
              <MenuIcon />
            </IconButton>
            <Menu
              anchorEl={anchorElNav}
              anchorOrigin={{
                vertical: "bottom",
                horizontal: "left",
              }}
              keepMounted
              transformOrigin={{
                vertical: "top",
                horizontal: "left",
              }}
              open={Boolean(anchorElNav)}
              onClose={handleCloseNavMenu}
              sx={{
                display: { xs: "block", md: "none" },
              }}
            >
              {pages.map((page) => (
                <MenuItem
                  key={page.id}
                  onClick={() => scrollToSection(page.id)}
                >
                  <Typography textAlign="center">{page.name}</Typography>
                </MenuItem>
              ))}
            </Menu>
          </Box>

          <Spa
            sx={{
              display: { xs: "flex", md: "none" },
              mr: 1,
              color: "primary.main",
            }}
          />
          <Typography
            variant="h6"
            noWrap
            component="div"
            onClick={() => scrollToSection("home")}
            sx={{
              mr: 2,
              display: { xs: "flex", md: "none" },
              flexGrow: 1,
              fontWeight: 700,
              color: "primary.main",
              cursor: "pointer",
            }}
          >
            CropGuard AI
          </Typography>

          <Box
            sx={{
              flexGrow: 1,
              display: { xs: "none", md: "flex" },
              justifyContent: "flex-end",
            }}
          >
            {pages.map((page) => (
              <Button
                key={page.id}
                onClick={() => scrollToSection(page.id)}
                sx={{ my: 2, color: "text.primary", display: "block" }}
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
