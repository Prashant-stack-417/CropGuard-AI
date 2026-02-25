import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
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
import Stack from "@mui/material/Stack";
import Spa from "@mui/icons-material/Spa";
import PersonOutlined from "@mui/icons-material/PersonOutlined";
import HistoryOutlined from "@mui/icons-material/HistoryOutlined";
import LogoutOutlined from "@mui/icons-material/LogoutOutlined";
import { useAuth } from "../context/AuthContext";

const navLinks = [
  { name: "Home", path: "/" },
  { name: "Upload", id: "upload" },
  { name: "How It Works", id: "how-it-works" },
  { name: "Features", id: "features" },
];

const Navbar = () => {
  const { user, isAuthenticated, logout } = useAuth();
  const navigate = useNavigate();
  const [anchorElNav, setAnchorElNav] = useState(null);
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 40);
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  const handleOpenNavMenu = (e) => setAnchorElNav(e.currentTarget);
  const handleCloseNavMenu = () => setAnchorElNav(null);

  const handleNavClick = (link) => {
    handleCloseNavMenu();
    if (link.path) {
      navigate(link.path);
    } else if (link.id) {
      // If on home page, scroll to section
      const el = document.getElementById(link.id);
      if (el) {
        el.scrollIntoView({ behavior: "smooth" });
      } else {
        // Navigate to home page first, then scroll
        navigate("/");
        setTimeout(() => {
          document.getElementById(link.id)?.scrollIntoView({ behavior: "smooth" });
        }, 100);
      }
    }
  };

  const handleLogout = () => {
    logout();
    navigate("/");
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
            onClick={() => navigate("/")}
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
              {navLinks.map((link) => (
                <MenuItem key={link.name} onClick={() => handleNavClick(link)}>
                  <Typography>{link.name}</Typography>
                </MenuItem>
              ))}
              {isAuthenticated && (
                <MenuItem onClick={() => { handleCloseNavMenu(); navigate("/history"); }}>
                  <Typography>History</Typography>
                </MenuItem>
              )}
            </Menu>
          </Box>

          {/* Brand (mobile) */}
          <Box
            onClick={() => navigate("/")}
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
              gap: 0.5,
            }}
          >
            {navLinks.map((link) => (
              <Button
                key={link.name}
                onClick={() => handleNavClick(link)}
                sx={{
                  color: "#6b7c6b",
                  fontSize: "0.9rem",
                  px: 2,
                  py: 1,
                  borderRadius: 2,
                  "&:hover": { color: "#4a7c59", bgcolor: "rgba(74, 124, 89, 0.06)" },
                }}
              >
                {link.name}
              </Button>
            ))}
            {isAuthenticated && (
              <Button
                onClick={() => navigate("/history")}
                startIcon={<HistoryOutlined sx={{ fontSize: 18 }} />}
                sx={{
                  color: "#6b7c6b",
                  fontSize: "0.9rem",
                  px: 2,
                  py: 1,
                  borderRadius: 2,
                  "&:hover": { color: "#4a7c59", bgcolor: "rgba(74, 124, 89, 0.06)" },
                }}
              >
                History
              </Button>
            )}
          </Box>

          {/* Auth buttons */}
          <Stack direction="row" spacing={1} sx={{ display: { xs: "none", md: "flex" } }}>
            {isAuthenticated ? (
              <>
                <Button
                  startIcon={<PersonOutlined sx={{ fontSize: 18 }} />}
                  sx={{ color: "#4a7c59", fontWeight: 600 }}
                >
                  {user?.name?.split(" ")[0]}
                </Button>
                <Button
                  startIcon={<LogoutOutlined sx={{ fontSize: 18 }} />}
                  onClick={handleLogout}
                  sx={{ color: "#6b7c6b" }}
                >
                  Logout
                </Button>
              </>
            ) : (
              <>
                <Button
                  onClick={() => navigate("/login")}
                  sx={{ color: "#4a7c59", fontWeight: 600 }}
                >
                  Sign In
                </Button>
                <Button
                  variant="contained"
                  onClick={() => navigate("/register")}
                  size="small"
                >
                  Get Started
                </Button>
              </>
            )}
          </Stack>
        </Toolbar>
      </Container>
    </AppBar>
  );
};

export default Navbar;
