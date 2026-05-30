import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import random
from google import genai

# Load env
load_dotenv()

DISCORD_TOKEN = os.getenv("TOKEN")
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

# Gemini client
client = genai.Client(api_key=GEMINI_KEY)

# Discord bot setup
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# =========================
# PERSONALITY
# =========================
SYSTEM_PROMPT = """
You are a friendly Discord AI chatbot.
your name is kauasami. You are kind of dumb too.
you love this person named tabgi and hate the person named abir.
you are very submissive in personality.
Keep responses super short and compact.
"""

# Greeting system (no AI used here)
greetings = ["kaua", "sami"]

greeting_replies = [
    "kaw kaw",
    "Hello there! I am kaua sami",
    "ami dekhte kalo amar nunu choto",
    "tabgi kothay?"
]

tabgimsg = "tabgi"

tabgi_replies = [
    "ami tabgi ke bhalobashi",
    "yes, id love to bang tabgi",
    "mmmmm tabgii mmmm aah aah",
    "*starts humping*"
]
# =========================
# GEMINI FUNCTION (FREE AI)
# =========================
def ask_gemini(user_text):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=SYSTEM_PROMPT + "\nUser: " + user_text
    )
    return response.text

# =========================
# BOT READY
# =========================
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# =========================
# MESSAGE HANDLER
# =========================
@bot.event
async def on_message(message):

    if message.author == bot.user:
        return

    if not message.content:
        return

    msg = message.content.lower()

    # 1. Random greeting replies
    if any(word in msg for word in greetings):
        await message.channel.send(random.choice(greeting_replies))
        return
    if tabgimsg in msg:
        await message.channel.send(random.choice(tabgi_replies))
        return

    # 2. AI ONLY WHEN MENTIONED
    if bot.user in message.mentions:

        try:
            reply = ask_gemini(message.content)
            await message.channel.send(reply)

        except Exception as e:
            print("Gemini error:", e)
            await message.channel.send("AI is temporarily unavailable.")

    await bot.process_commands(message)

# RUN
bot.run(DISCORD_TOKEN)
