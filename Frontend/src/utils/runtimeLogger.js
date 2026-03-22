const envFlag = (import.meta.env.VITE_RUNTIME_LOGS || "").toLowerCase();

const isRuntimeLoggingEnabled =
  import.meta.env.PROD || envFlag === "1" || envFlag === "true" || envFlag === "yes";

const buildMeta = () => ({
  app: "cropguard-frontend",
  mode: import.meta.env.MODE,
  ts: new Date().toISOString(),
});

const print = (level, event, payload) => {
  if (!isRuntimeLoggingEnabled) return;

  const message = {
    ...buildMeta(),
    level,
    event,
    ...(payload ? { payload } : {}),
  };

  if (level === "error") {
    console.error("[runtime]", message);
    return;
  }

  if (level === "warn") {
    console.warn("[runtime]", message);
    return;
  }

  console.info("[runtime]", message);
};

export const runtimeLogger = {
  enabled: isRuntimeLoggingEnabled,
  info: (event, payload) => print("info", event, payload),
  warn: (event, payload) => print("warn", event, payload),
  error: (event, payload) => print("error", event, payload),
};
