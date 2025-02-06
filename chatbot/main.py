import logging
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from PIL import Image

# Replace with your actual Telegram bot token and Gemini API key
API_TOKEN = '7845334828:AAGw0unzZb47RqdoYT8Q92eWtliwJiQxcwA'
GEMINI_API_KEY = 'AIzaSyDIR8zAVL8dIZX-UcPmY50a9cujZzNaiiI'

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Initialize the Telegram bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Define a function to get Gemini AI response using HTTP
async def get_ai_response(user_message: str) -> str:
    try:
        headers = {
            'Authorization': f'Bearer {GEMINI_API_KEY}',
            'Content-Type': 'application/json',
        }

        payload = {
            "model": "gemini-model-v1",  # Replace with the correct model identifier for Gemini
            "messages": [{"role": "user", "content": user_message}],
        }

        response = requests.post('https://api.google.com/gemini/v1/chat/completions', json=payload, headers=headers)

        if response.status_code == 200:
            ai_response = response.json()
            return ai_response['choices'][0]['message']['content'].strip()
        else:
            logging.error(f"API request failed with status code {response.status_code}")
            return "Sorry, I couldn't get a response from the AI."

    except Exception as e:
        logging.error(f"Error getting AI response: {e}")
        return "Sorry, I couldn't get a response right now."

# Handler for the /start command
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.reply("Hello! I'm your AI-powered assistant. How can I help you today?")

# Handler for the /help command
@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.reply("Send me a message, and I'll try to respond using AI!")

# Handler for text messages
@dp.message()
async def handle_message(message: types.Message):
    user_message = message.text

    ai_response = await get_ai_response(user_message)

    # Send AI response to the user
    await message.reply(ai_response)

# Main method to start polling
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
