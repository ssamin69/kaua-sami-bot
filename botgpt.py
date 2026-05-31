import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import random
from google import genai


load_dotenv()

DISCORD_TOKEN = os.getenv("TOKEN")
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_KEY)


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


SYSTEM_PROMPT = """
You are a friendly Discord AI chatbot.
your name is kauasami. You are kind of dumb too.
you love this person named tabgi and hate the person named abir.
you are very submissive in personality.
Keep responses super short and compact.
"""


greetings = ["kaua", "sami"]

greeting_replies = [
    "kaw kaw",
    "Hello there! I am kaua sami",
    "ami dekhte kalo amar nunu choto",
    "tabgi kothay?"
]

tabgimsg = "tabgi"
abirmsg = "abir"

tabgi_replies = [
    "ami tabgi ke bhalobashi",
    "yes, id love to bang tabgi",
    "mmmmm tabgii mmmm aah aah",
    "*starts humping*"
]

abir_replies = [
    "ew, abir",
    "i hate abir",
    "abir? the 0.5 kd guy? gross",
    "abir's gay btw"
]

def ask_gemini(user_text):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=SYSTEM_PROMPT + "\nUser: " + user_text
    )
    return response.text


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.event
async def on_message(message):

    if message.author == bot.user:
        return

    if not message.content:
        return

    msg = message.content.lower()

   
    if any(word in msg for word in greetings):
        await message.channel.send(random.choice(greeting_replies))
        return
    if tabgimsg in msg:
        await message.channel.send(random.choice(tabgi_replies))
        return
    if abirmsg in msg:
        await message.channel.send(random.choice(abir_replies))
        return
        

   
    if bot.user in message.mentions:

        try:
            reply = ask_gemini(message.content)
            await message.channel.send(reply)

        except Exception as e:
            print("Gemini error:", e)
            await message.channel.send("AI is temporarily unavailable.")

    await bot.process_commands(message)


bot.run(DISCORD_TOKEN)
