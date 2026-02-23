import requests
import time

time.sleep(2)  # wait for server to start

response = requests.get("http://localhost:8000/health")

if response.status_code == 200:
    print("✅ App is healthy")
else:
    print("❌ App failed")
    exit(1)