import os
import asyncio
import traceback

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intent = discord.Intents.all()
bot = commands.Bot('.', intents=intent)

linux_sys = True if 'posix' in os.name else False

@bot.event
async def load():
    for file in os.listdir(".\cogs"):
        if file.endswith(".py"):
            name = file[:-3]
            await bot.load_extension(f"cogs.{name}")

@bot.event
async def on_ready():
    try:
        print(os.path.join(os.getcwd(), 'cogs'))
        for file in os.listdir(os.path.join(os.getcwd(), 'cogs')):
            if file.endswith(".py"): 
                name = file[:-3]
                await bot.load_extension(f"cogs.{name}")
    except Exception as e:
        traceback_str = traceback.format_exc(limit=10)
        print("ERROR!", e)
        print(traceback_str)


# Command to respond with "Pong!"
@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')


async def main():
    #await load()
    try:
        await bot.start(TOKEN)
    except Exception as e:
        traceback_str = traceback.format_exc(limit=10)
        print("ERROR!", e)
        print(traceback_str)


if __name__ == "__main__":
    asyncio.run(main())