
# App Registration Client

This Python script simulates sending mock application data from a virtual device to a backend API using an HTTP POST request. It's useful for testing APIs that register app metadata like name, version, and device details.

## 🔧 Features

- Generates a unique app name using a device UUID.
- Fetches system information from the host machine.
- Sends data to a Flask-based API endpoint.
- Handles and logs server responses.

## 🚀 How It Works

The script creates mock data and sends it to a backend server at:

```
http://127.0.0.1:5000/add_app
```

Make sure your Flask backend is running and listening on the same port.

## 📦 Data Sent

- `app_name`: Auto-generated with a UUID.
- `version`: Static value `"1.0.0"`.
- `description`: Includes the device UUID and system info.

Example payload:
```json
{
  "app_name": "App-3e0a23c6-cc53-4c2b-b2dc-df3cbf849c52",
  "version": "1.0.0",
  "description": "App for device 3e0a23c6..., running Windows-10-10.0.19045-SP0"
}
```

## ✅ Prerequisites

- Python 3.x
- Flask (for backend)
- `requests` library (install using `pip install requests`)

## 📥 How to Use

1. Clone the repo:
   ```bash
   git clone https://github.com/gautamraj8044/app-registration-client.git
   cd app-registration-client
   ```

2. Run the script:
   ```bash
   python app_registration.py
   ```

3. Check your Flask backend for the received data.

## 📂 File Structure

```
app-registration-client/
├── app_registration.py   # Main script file
```

## 📌 Notes

- Update the `SERVER_URL` in the script if your backend is hosted elsewhere.
- This script is for local testing and can be extended for real device/app integrations.

