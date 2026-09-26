import os
import requests
from dotenv import load_dotenv


# 1. Load the secret configuration from your hidden .env file
load_dotenv()
target_url = os.getenv("WEBHOOK_URL")

# 2. Your structured JSON payload
hospital_data = {
  "name": "Zora",
  "medicine_type": "Amoxicillin",
  "quantity": 2
}

print("Step 1: Fetching secure URL and pushing the button in VS Code...")

if not target_url:
    print("CRITICAL CONFIG ERROR: Could not find WEBHOOK_URL in your .env file!")
else:
    # 3. MECHANICAL FLOW: Fires the secure POST request
    response = requests.post(target_url, json=hospital_data)
    
    print("Step 2: Checking what the server yelled back...")
    print(f"Status Code Received: {response.status_code} (200 means success!)")
