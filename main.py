import os, asyncio

import discord
from discord.ext import commands
from dotenv import load_dotenv

cogs = [
    'cogs.basic'
]


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intent = discord.Intents.all()
bot = commands.Bot('.', intents=intent)

@bot.event
async def load():
    for file in os.listdir(".\cogs"):
        if file.endswith(".py"): 
            name = file[:-3]
            await bot.load_extension(f"cogs.{name}")

@bot.event
async def on_ready():
    for file in os.listdir(".\cogs"):
        if file.endswith(".py"): 
            name = file[:-3]
            await bot.load_extension(f"cogs.{name}")


# Command to respond with "Pong!"
@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')


async def main():
    #await load()
    await bot.start(TOKEN)


if __name__ == "__main__":
    asyncio.run(main())