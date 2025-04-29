import requests
import platform
import uuid
import json

# Configuration
SERVER_URL = "http://127.0.0.1:5000/add_app"

def generate_app_data():
    device_id = str(uuid.uuid4())
    system_info = platform.platform()
    return {
        "app_name": f"App-{device_id}",
        "version": "1.0.0",
        "description": f"App for device {device_id}, running {system_info}"
    }

def send_app_data(data):
    try:
        response = requests.post(SERVER_URL, data=data)
        if response.status_code == 201:
            print("✅ Data sent successfully!")
            print("📨 Server Response:", json.dumps(response.json(), indent=4))
        else:
            print(f"❌ Failed with status code: {response.status_code}")
            print("🔁 Server Response:", response.text)
    except requests.RequestException as e:
        print(f"🚨 Request error: {e}")

if __name__ == "__main__":
    app_data = generate_app_data()
    send_app_data(app_data)
