from flask import Flask, request
import telegram
import os
import datetime
import asyncio

TOKEN = ""
bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        if "text" in data["message"]:
            text = data["message"]["text"]
            person_name = extract_name(text)
            result = search_apollo(person_name)
            log_to_sheets(text, result)
            bot.send_message(chat_id=chat_id, text=result)
    
    return "ok"


def extract_name(text):
    # Removing the common phrases like "Find details about" or "Email of"
    if "Find details of" in text:
        return text.replace("Find details of", "").strip()
    elif "Email of" in text:
        return text.replace("Email of", "").strip()
    return text.strip()

def search_apollo(name):
    # Replace with real Apollo API call
    return f"Simulated result for {name}:\nName: {name}\nCompany: Google\nEmail: example@google.com"

def log_to_sheets(query, result):
    # Placeholder for Google Sheets logging
    print(f"Logging: {query} → {result}")

async def send_message(chat_id, result):
    # Use the async send_message method
    await bot.send_message(chat_id=chat_id, text=result)

if __name__ == '__main__':
    app.run(port=5000)
