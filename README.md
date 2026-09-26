# Hospital Webhook Pipeline Simulator

An automated data pipeline simulating a real-time clinical dispatch system using **Python, Webhooks, and JSON payloads**.

## System Architecture & Mechanical Flow
1. **Trigger:** The script builds a structured JSON payload representing a patient order.
2. **Transport (POST Request):** The script executes a secure HTTP POST request, transferring the JSON data across the network to a designated server URL endpoint.
3. **Validation & Response:** The receiver parses the JSON data format and responds with an HTTP status code (e.g., `200 OK`) to confirm data safety.

## How to Run It Locally
1. Clone this repository.
2. Install the network tools: `pip install requests python-dotenv`
3. Create a `.env` file in the root directory and add your endpoint:
   `WEBHOOK_URL=your_webhook_url_here`
4. Execute the pipeline script: `python hospital_webhook.py`
