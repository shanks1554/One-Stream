import subprocess
import time
import signal
import sys

# Start Flask (frontend)
flask_process = subprocess.Popen(
    ['python','frontend/app.py'],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

# Start FastAPI (Backend)
fastapi_process = subprocess.Popen(
    ['uvicorn','backend.main:app','--reload'],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

def shutdown():
    print("\nShutting down both servers...")
    flask_process.send_signal(signal.SIGINT)
    fastapi_process.send_signal(signal.SIGINT)
    flask_process.wait()
    fastapi_process.wait()
    sys.exit(0)
    
try:
    print("✅ Flask and FastAPI servers are starting...")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    shutdown()