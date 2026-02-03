import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import Paper from "@mui/material/Paper";
import Button from "@mui/material/Button";
import Grid from "@mui/material/Grid";
import Stack from "@mui/material/Stack";
import LinearProgress from "@mui/material/LinearProgress";
import Chip from "@mui/material/Chip";
import CircularProgress from "@mui/material/CircularProgress";
import DownloadOutlined from "@mui/icons-material/DownloadOutlined";
import SupportAgentOutlined from "@mui/icons-material/SupportAgentOutlined";

const Results = ({ result, isLoading }) => {
  if (!result && !isLoading) return null;

  const getConfidenceColor = (confidence) => {
    if (confidence >= 80) return "success";
    if (confidence >= 60) return "warning";
    return "error";
  };

  return (
    <Box sx={{ py: { xs: 8, sm: 12 }, bgcolor: "background.default" }}>
      <Container maxWidth="lg">
        <Stack spacing={6} alignItems="center">
          <Typography variant="h2" fontWeight={700} textAlign="center">
            Detection Results
          </Typography>

          {isLoading ? (
            <Paper
              elevation={3}
              sx={{ p: 8, textAlign: "center", width: "100%", maxWidth: 600 }}
            >
              <CircularProgress size={64} thickness={4} sx={{ mb: 3 }} />
              <Typography variant="h5" fontWeight={600} gutterBottom>
                Analyzing Image...
              </Typography>
              <Typography color="text.secondary">
                Our AI is detecting crop diseases
              </Typography>
            </Paper>
          ) : (
            <Paper
              elevation={3}
              sx={{ width: "100%", maxWidth: 900, overflow: "hidden" }}
            >
              <Box sx={{ bgcolor: "primary.main", color: "white", p: 3 }}>
                <Stack
                  direction="row"
                  justifyContent="space-between"
                  alignItems="center"
                >
                  <Typography variant="h5" fontWeight={700}>
                    Analysis Complete
                  </Typography>
                  <Chip
                    label={result.status}
                    color={result.status === "Healthy" ? "success" : "error"}
                    sx={{ fontWeight: 600, color: "white" }}
                  />
                </Stack>
              </Box>

              <Box sx={{ p: 4 }}>
                <Grid container spacing={4}>
                  <Grid item xs={12} md={6}>
                    <Typography
                      variant="overline"
                      color="text.secondary"
                      fontWeight={600}
                    >
                      Disease Name
                    </Typography>
                    <Typography
                      variant="h4"
                      fontWeight={700}
                      color="text.primary"
                    >
                      {result.diseaseName}
                    </Typography>
                  </Grid>
                  <Grid item xs={12} md={6}>
                    <Typography
                      variant="overline"
                      color="text.secondary"
                      fontWeight={600}
                    >
                      Crop Type
                    </Typography>
                    <Typography
                      variant="h4"
                      fontWeight={700}
                      color="text.primary"
                    >
                      {result.cropName}
                    </Typography>
                  </Grid>

                  <Grid item xs={12}>
                    <Stack spacing={1}>
                      <Stack direction="row" justifyContent="space-between">
                        <Typography
                          variant="overline"
                          color="text.secondary"
                          fontWeight={600}
                        >
                          Confidence Score
                        </Typography>
                        <Typography
                          variant="h5"
                          fontWeight={700}
                          color="primary.main"
                        >
                          {result.confidence}%
                        </Typography>
                      </Stack>
                      <LinearProgress
                        variant="determinate"
                        value={result.confidence}
                        color={getConfidenceColor(result.confidence)}
                        sx={{ height: 12, borderRadius: 2 }}
                      />
                    </Stack>
                  </Grid>

                  <Grid item xs={12}>
                    <Typography
                      variant="overline"
                      color="text.secondary"
                      fontWeight={600}
                      gutterBottom
                    >
                      Description
                    </Typography>
                    <Paper
                      sx={{
                        p: 3,
                        bgcolor: "background.default",
                        borderLeft: 4,
                        borderColor: "primary.main",
                      }}
                    >
                      <Typography color="text.primary">
                        {result.description}
                      </Typography>
                    </Paper>
                  </Grid>

                  <Grid item xs={12}>
                    <Typography
                      variant="overline"
                      color="text.secondary"
                      fontWeight={600}
                      gutterBottom
                    >
                      Treatment & Prevention
                    </Typography>
                    <Stack spacing={2}>
                      {result.treatments.map((treatment, index) => (
                        <Paper
                          key={index}
                          sx={{
                            p: 2,
                            bgcolor: "success.50",
                            border: 1,
                            borderColor: "success.200",
                            display: "flex",
                            gap: 2,
                          }}
                        >
                          <Box
                            sx={{
                              width: 28,
                              height: 28,
                              bgcolor: "primary.main",
                              color: "white",
                              borderRadius: "50%",
                              display: "flex",
                              alignItems: "center",
                              justifyContent: "center",
                              fontWeight: 700,
                              flexShrink: 0,
                            }}
                          >
                            {index + 1}
                          </Box>
                          <Typography color="text.primary" sx={{ flex: 1 }}>
                            {treatment}
                          </Typography>
                        </Paper>
                      ))}
                    </Stack>
                  </Grid>

                  <Grid item xs={12}>
                    <Stack direction={{ xs: "column", sm: "row" }} spacing={2}>
                      <Button
                        variant="contained"
                        size="large"
                        startIcon={<DownloadOutlined />}
                        fullWidth
                      >
                        Download Report
                      </Button>
                      <Button
                        variant="outlined"
                        size="large"
                        startIcon={<SupportAgentOutlined />}
                        fullWidth
                      >
                        Consult Expert
                      </Button>
                    </Stack>
                  </Grid>
                </Grid>
              </Box>
            </Paper>
          )}
        </Stack>
      </Container>
    </Box>
  );
};

export default Results;
