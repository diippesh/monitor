import os
import sys
from fastapi import FastAPI

# Add some debugging info
print(f"Python version: {sys.version}")
print(f"Python path: {sys.path}")
print(f"Current working directory: {os.getcwd()}")

# Try to import app_insights_logger safely
try:
    import app_insights_logger
    print("✅ app_insights_logger imported successfully")
except ImportError as e:
    print(f"⚠️ app_insights_logger import failed: {e}")

app = FastAPI(title="FastAPI Azure App", version="1.0.0")

@app.get('/')
def welcome():
    return {"message": "hello worldd", "status": "running"}

@app.get('/greet/{name}')
def greet(name: str):
    return {"message": f"hello {name} welcome to fast api", "name": name}

@app.get('/health')
def health_check():
    return {"status": "healthy", "python_version": sys.version}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
