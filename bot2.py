import os
import discord
import urllib.request
import json
import ast
import fileio
from dotenv import load_dotenv
from discord.ext import commands

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@bot.event
async def on_member_join(member):
    print(f'{member} has joined the server.')
    #await guild.send('Welcome to the server kiddo! {member} Make us proud')

@bot.event
async def on_member_remove(member):
    print(f'{member} has left the server.')
    
@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def track(ctx, playername):
    await ctx.send('test success ' + playername)


def get_player_id(username):
    url = 'https://gameinfo.albiononline.com/api/gameinfo/search?q=' + username
    operUrl = urllib.request.urlopen(url)
    if(operUrl.getcode()==200):
        data = operUrl.read()
        jsonData = json.loads(data)
    else:
        print("Error receiving data", operUrl.getcode())

    for user in jsonData['players']:
        u_id = user.get('Id')
        u_Name = user.get('Name')
        print(u_id)
        print(u_Name)
        print()
        if (u_id == 'QPELoDHRQwWI3-yhzAGYmA'):
            print('Found real mushii')
            return u_id

def get_kills(playerId):
    url = 'https://gameinfo.albiononline.com/api/gameinfo/players/' + playerId + '/kills'
    operUrl = urllib.request.urlopen(url)
    if(operUrl.getcode()==200):
        data = operUrl.read()
        jsonData = json.loads(data)
    else:
        print("Error receiving data", operUrl.getcode())

    print(jsonData[0]['Killer']['AverageItemPower'])
    #276980348
    print(jsonData[0]['EventId'])





def main():
    playerId = get_player_id("Mushii")
    print(playerId)
    get_kills(playerId)




    


#playerName = data["Id"]



#https://gameinfo.albiononline.com/api/gameinfo/search?q=Mushii
#QPELoDHRQwWI3-yhzAGYmA
#https://gameinfo.albiononline.com/api/gameinfo/players/QPELoDHRQwWI3-yhzAGYmA/kills


main()
bot.run(TOKEN)

