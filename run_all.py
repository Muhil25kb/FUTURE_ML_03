import subprocess
import sys
import os
import time

# Absolute path to D:\support_bot
root_dir = os.path.dirname(os.path.abspath(__file__))

# Define subfolder paths
backend_dir = os.path.join(root_dir, "backend")
web_dir = os.path.join(root_dir, "web")

# Commands
backend_cmd = [sys.executable, "-m", "uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"]
web_cmd = [sys.executable, "-m", "streamlit", "run", "app.py"]

print("⏳ Starting Backend (Wait 15 seconds for AI model to load)...")
# CRITICAL: Run inside /backend so it finds model.pkl
backend_proc = subprocess.Popen(backend_cmd, cwd=backend_dir)

# CRITICAL: You must wait for model.pkl to load in retriever.py
time.sleep(15) 

print("🚀 Starting Web UI...")
# Run inside /web folder
web_proc = subprocess.Popen(web_cmd, cwd=web_dir)

try:
    backend_proc.wait()
    web_proc.wait()
except KeyboardInterrupt:
    backend_proc.terminate()
    web_proc.terminate()
    print("🛑 Stopped.")