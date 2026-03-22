"""
Vercel Serverless — ASGI entry point for CropGuard AI FastAPI app.
Vercel automatically routes requests to this file.
"""

import sys
from pathlib import Path

# Add parent directory to path so imports work
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.main import app

# Vercel ASGI serverless: app is automatically detected and used as the handler
