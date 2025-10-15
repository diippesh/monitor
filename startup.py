#!/usr/bin/env python3
"""
Startup script for Azure App Service deployment
This helps debug module loading issues
"""

import sys
import os

print("Python version:", sys.version)
print("Python path:", sys.path)
print("Current working directory:", os.getcwd())

# Test imports
try:
    import fastapi
    print("✅ FastAPI imported successfully, version:", fastapi.__version__)
except ImportError as e:
    print("❌ FastAPI import failed:", e)

try:
    import uvicorn
    print("✅ Uvicorn imported successfully, version:", uvicorn.__version__)
except ImportError as e:
    print("❌ Uvicorn import failed:", e)

try:
    import gunicorn
    print("✅ Gunicorn imported successfully, version:", gunicorn.__version__)
except ImportError as e:
    print("❌ Gunicorn import failed:", e)

try:
    from uvicorn.workers import UvicornWorker
    print("✅ UvicornWorker imported successfully")
except ImportError as e:
    print("❌ UvicornWorker import failed:", e)

try:
    import main
    print("✅ Main module imported successfully")
except ImportError as e:
    print("❌ Main module import failed:", e)

print("Startup check completed.")