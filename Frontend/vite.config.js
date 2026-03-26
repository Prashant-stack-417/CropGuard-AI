import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      },
    },
  },
  build: {
    chunkSizeWarningLimit: 700,
    rollupOptions: {
      output: {
        manualChunks: {
          vercel: ['@vercel/analytics', '@vercel/speed-insights'],
        },
      },
    },
  },
  ssr: {
    noExternal: ['@vercel/analytics', '@vercel/speed-insights'],
  },
})
