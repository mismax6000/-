import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
ADMIN_ID = int(os.getenv("ADMIN_ID", 0))

# OpenRouter Settings
OPENROUTER_URL = "https://openrouter.ai/api/v1"
AI_MODEL = "google/gemini-2.0-flash-lite-preview-02-05:free" # Using a free model by default

# Список слов для авто-бана
BAD_WORDS = ["спам", "реклама", "купить", "подпишись"] 
# Добавьте сюда другие маты, за которые бот должен банить автоматически.
ALLOWED_LINKS = ["t.me/your_channel"]
