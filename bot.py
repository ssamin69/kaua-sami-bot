import discord
import random
from discord.ext import commands

TOKEN = "MTUxMDMzMDQxMTg2NjEzMjY4Mw.GZBnyI.ujpzpT7ITr6hK8fbzMIrgx8bsYR1Wa1eVncknE"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

@bot.event
async def on_ready():
    print("Bot is online!")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")
@bot.event
async def on_message(message):

    if message.author == bot.user:
        return
    msg = message.content.lower()

    if "kaua" in msg:
        replies = [
            "Hi! Ami Kaua Sami",
            "Hello! Ami onek Kalo",
            "Kaw Kaw",
            "Amar nunu onek choto karon ami dekhte kalo"
        ]

        await message.channel.send(random.choice(replies))
    if "tabgi" in msg:
        replies = [
            "ami tabgi ke bhalobashi",
            "yes, id love to bang tabgi",
            "mmmmm tabgii mmmm aah aah",
            "*starts humping*"
        ]

        await message.channel.send(random.choice(replies))
    

    if "kalo" in message.content.lower():
        await message.channel.send("hae ami kalo")
    if "kaw kaw" in message.content.lower():
        await message.channel.send("kaw kaw")
    if "nunu" in message.content.lower():
        await message.channel.send("amar nunu onek choto hehehe")

    await bot.process_commands(message)

bot.run(TOKEN)
