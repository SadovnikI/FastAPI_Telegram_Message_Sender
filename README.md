# FastAPI Telegram Message Sender

This is a simple FastAPI web service for sending messages to Telegram using JSON payloads.

## Getting Started

### Prerequisites

- Python 3.7+
- pip \(Python package manager\)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/SadovnikI/FastAPI_Telegram_Message_Sender.git
   ```

2. Navigate to the project directory:

   ```bash
   cd fastapi-telegram-message-sender
   ```
 
3. Create a virtual environment (optional but recommended):  
   ```bash
   # On Windows
   python -m venv venv
   
   # On macOS and Linux
   python3 -m venv venv
   ```
4.   Activate the virtual environment:
   ```bash
   # On Windows
   venv\Scripts\activate
   
   # On macOS and Linux
   source venv/bin/activate
   ```
5. Install the required dependencies::

   ```bash
   pip install -r requirements.txt
   ```
   
## Usage

1. Run the FastAPI application:

   ```bash
   uvicorn telegram_message_sender:app --reload
   ```
   
2. Send a POST request to the /send_message endpoint with a JSON payload containing the Telegram bot token (bottoken), chat ID (chatid), and message (message):

   ```bash
   curl -X POST "http://localhost:8000/send_message" -H "Content-Type: application/json" -d '{
     "bottoken": "YOUR_TELEGRAM_BOT_TOKEN",
     "chatid": "YOUR_CHAT_ID",
     "message": "YOUR_MESSAGE"
      }'
   ```
3. Alternatively, you can use the Swagger UI to send a POST request:

* Open your browser and navigate to http://localhost:8000/docs.
* Locate the /send_message endpoint and click on it to expand.
* Click on the "Try it out" button.
* Enter the required parameters (bottoken, chatid, message) in the provided fields.
* Click on the "Execute" button to send the request.
   
## API Documentation

You can access the Swagger documentation for the API by visiting http://localhost:8000/docs in your browser. You can also explore the API using the interactive interface provided by Swagger UI.