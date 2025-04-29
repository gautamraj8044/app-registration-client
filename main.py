import requests
import platform
import uuid
import json

SERVER_URL = "http://127.0.0.1:5000/add_app"  # Modify if your server is hosted elsewhere

# Mock data from the virtual Android system
device_id = str(uuid.uuid4())  # Generate a unique device ID
system_info = platform.platform()  # Get system information

# Prepare the mock data for the app
data = {
    "app_name": f"App-{device_id}",  # Unique app name for identification
    "version": "1.0.0",  
    "description": f"App for device {device_id}, running {system_info}"
}

# Send POST request to the backend API to add an app
try:
    # Sending form-encoded data
    response = requests.post(SERVER_URL, data=data)
    
    # Check if the request was successful
    if response.status_code == 201:
        print("Data sent successfully!")
        # Log the server's response
        response_data = response.json()
        print("Server Response:", json.dumps(response_data, indent=4))
    else:
        print(f"Failed to send data. Server responded with: {response.status_code}")
        print("Server Response:", response.text)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
