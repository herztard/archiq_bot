# ArchiqBot

## Description
A Telegram bot that forwards user messages to an API and returns the response. The bot provides a conversational interface for users to interact with AI-Agent on the backend API service.

## Team Members

| Name                  | Student ID  | Lecture Group | Practice Group | Role                                          |
|-----------------------|-------------|---------------|----------------|-----------------------------------------------|
| Adilzhan Slyamgazy    | 220103151   | 04-N          | 16-P           | Backend, AI-agent development, Database setup |
| Dauletkhan Izbergenov | 220103015   | 04-N          | 15-P           | Frontend                                      |
| Alikhan Toleberdyyev  | 220103050   | 04-N          | 16-P           | Frontend                                      |
| Bakdaulet Bekkhoja    | 220103014   | 04-N          | 15-P           | DevOps                                        |
| Aknur Bauyrzhankyzy   | 220103314   | 04-N          | 16-P           | PM, Manual testing, Design-scratching         |


## Installation

```bash
# Clone the repository
git clone https://github.com/herztard/archiq_bot.git

# Navigate to the project directory
cd archiq_bot

# 3. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file with your credentials
echo "BOT_TOKEN=your_telegram_bot_token" > .env
echo "API_BASE_URL=your_api_base_url" >> .env
```

## Usage

```bash
# Run the bot
python main.py
```

## Features
- Forwards user messages to a configured API endpoint
- Sends typing indicator while waiting for API response
- Logs user interactions
- Supports Markdown formatting in responses
- Collects and forwards user metadata with requests

## Environment Variables
- `BOT_TOKEN`: Your Telegram Bot token from BotFather
- `API_BASE_URL`: Base URL for the API that processes user messages

## Dependencies
- python-telegram-bot
- requests
- python-dotenv
- icecream (for debugging)
- nest-asyncio

## License
[MIT](https://choosealicense.com/licenses/mit/) 