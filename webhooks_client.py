import requests

# The local address where your Flask app is listening
url = "http://127.0.0.1:5000/webhook"

# Mock data simulating a webhook payload
payload = {
    "event": "independent_test",
    "status": "working",
    "message": "Hello from the local sender script!",
}

try:
    # Send the POST request
    response = requests.post(url, json=payload)
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Body: {response.json()}")
except requests.exceptions.ConnectionError:
    print("Error: Could not connect. Is your Flask app running on port 5000?")
