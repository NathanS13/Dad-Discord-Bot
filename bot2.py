import os
import discord
import urllib.request
import json
import ast
import fileio as f
import time
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext import tasks

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

@tasks.loop(minutes=1)
async def test():
    channel = bot.get_channel(816437844507492365)
    await channel.send("Updating List!")
    checkEventUpdate()
    await channel.send("Done Updating List!")

@test.before_loop
async def before():
    await bot.wait_until_ready()
    
@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def track(ctx, playername):
    #checkTracking = track_player(playername)
    if (f.checksave(playername)):
        await ctx.send('Already tracking: ' + playername)
    else:
        await ctx.send('Looking up: ' + playername)
        playerid = get_player_id(playername)
        f.savefile(playername, playerid)
        await ctx.send('Found Albion player!: ' + playername)
        await ctx.send('Saving last few pvp kills..')
        get_kills(playername, playerid)
        await ctx.send('Now tracking: ' + playername)
    #await ctx.send('Now tracking albion player: ' + playername + ' with id: ')

@bot.command()
async def clearplayers(ctx):
    f.clearfiles()
    await ctx.send('cleared!')

#def track_player(username):
#    print('in track player')
#    if (f.checksave(username)):
#        return True
#    else:
#        f.savefile(username, 'this is a test')
#        return False

def get_player_id(username):
    url = 'https://gameinfo.albiononline.com/api/gameinfo/search?q=' + username
    operUrl = urllib.request.urlopen(url)
    if(operUrl.getcode()==200):
        data = operUrl.read()
        jsonData = json.loads(data)
    else:
        print("Error receiving data", operUrl.getcode())

    #could be bad code. Duplicate names like Mushii will grab last
    #doesnt appear to be an issue for other look ups. I did recreate
    #character Mushii, which is how I noticed double names in lookup
    u_id = ''
    for user in jsonData['players']:
        u_name = user.get('Name')
        if (u_name == username):
            #print('Found user ' + u_id)
            u_id = user.get('Id')

    return u_id

def get_kills(username, playerId):
    url = 'https://gameinfo.albiononline.com/api/gameinfo/players/' + playerId + '/kills'
    operUrl = urllib.request.urlopen(url)
    if(operUrl.getcode()==200):
        data = operUrl.read()
        jsonData = json.loads(data)
    else:
        print("Error receiving data", operUrl.getcode())


    alist = []
    blist = []
    for kill in reversed(jsonData):
        if (kill['Killer']['Equipment']['MainHand']):            
            alist.append(kill['Killer']['Equipment']['MainHand']['Type'])
        if (kill['Killer']['Equipment']['Head']):
            alist.append(kill['Killer']['Equipment']['Head']['Type'])
        if (kill['Killer']['Equipment']['Armor']):
            alist.append(kill['Killer']['Equipment']['Armor']['Type'])    
        if (kill['Killer']['Equipment']['Shoes']):
            alist.append(kill['Killer']['Equipment']['Shoes']['Type'])          
        if (kill['Killer']['Equipment']['Bag']):
            alist.append(kill['Killer']['Equipment']['Bag']['Type'])            
        if (kill['Killer']['Equipment']['Cape']):
            alist.append(kill['Killer']['Equipment']['Cape']['Type'])
        if (kill['Killer']['Equipment']['Mount']):
            alist.append(kill['Killer']['Equipment']['Mount']['Type'])
        if (kill['Killer']['Equipment']['Potion']):
            alist.append(kill['Killer']['Equipment']['Potion']['Type'])
        if (kill['Killer']['Equipment']['Food']):
            alist.append(kill['Killer']['Equipment']['Food']['Type'])
        
        if (kill['Victim']['Equipment']['MainHand']):            
            blist.append(kill['Victim']['Equipment']['MainHand']['Type'])
        if (kill['Victim']['Equipment']['Head']):
            blist.append(kill['Victim']['Equipment']['Head']['Type'])
        if (kill['Victim']['Equipment']['Armor']):
            blist.append(kill['Victim']['Equipment']['Armor']['Type'])
        if (kill['Victim']['Equipment']['Shoes']):
            blist.append(kill['Victim']['Equipment']['Shoes']['Type'])
        if (kill['Victim']['Equipment']['Bag']):
            blist.append(kill['Victim']['Equipment']['Bag']['Type'])
        if (kill['Victim']['Equipment']['Cape']):
            blist.append(kill['Victim']['Equipment']['Cape']['Type'])
        if (kill['Victim']['Equipment']['Mount']):
            blist.append(kill['Victim']['Equipment']['Mount']['Type'])
        if (kill['Victim']['Equipment']['Potion']):
            blist.append(kill['Victim']['Equipment']['Potion']['Type'])
        if (kill['Victim']['Equipment']['Food']):
            blist.append(kill['Victim']['Equipment']['Food']['Type'])
            
        f.savefile2(username, kill['EventId'], alist, blist)
        alist.clear()
        blist.clear()

        
    #print(jsonData[0]['Victim'])

#optimize this by making player id a tuple within the tracking list
#take out the unique id in normal player kill logs
#optimize more, we assume only 1 kill at a time - we can fix this with
#some sort of algo
def checkEventUpdate():
    playerList = f.getListOfTrack()
    for player in playerList:

        playerId = f.getPlayerId(player)

        url = 'https://gameinfo.albiononline.com/api/gameinfo/players/' + playerId + '/kills'
        operUrl = urllib.request.urlopen(url)
        if(operUrl.getcode()==200):
            data = operUrl.read()
            jsonData = json.loads(data)
        else:
            print("Error receiving data", operUrl.getcode())

        print('checking latest for ' + player + ' ' + str(jsonData[0]['EventId']))
        if (str(jsonData[0]['EventId']) != f.getlastevent(player)):
            f.clearfile(player)
            f.savefile(player, playerId)
            get_kills(player, playerId)
            #call to display last kill?

        
        


def main():
    #playerId = get_player_id("Mushii")
    #print(playerId)
    #get_kills("Mushii", playerId)
    #print(f.checksave('test'))
    #f.savefile('test','sdasdasd')
    #alist = {}
    #alist['username'] = []
    #alist['playerid'] = []
    #alist['kills'] = []

    #alist['username'].append("Mushii")
    #alist['playerid'].append("Mushii")
    #alist['playerid'].append("Mushii")
    #alist = {}
    

    #alist['username']= 'Mushii'
    #alist['playerid']= 'QPELoDHRQwWI3-yhzAGYmA'

    #alist['kills'] = {'eventid': '123'}
    #alist['kills']['killer'] = {
    #    'wep': 'pito'
    #    }
    #print(alist['kills']['killer']['wep'])
    print('hello')
    checkEventUpdate()
    


    
    
    #with open('test.txt', 'w') as outfile:
    #    json.dump(alist, outfile)

    #print(json.dumps(alist, indent=4))


        
    


#playerName = data["Id"]



#https://gameinfo.albiononline.com/api/gameinfo/search?q=Mushii
#QPELoDHRQwWI3-yhzAGYmA
#https://gameinfo.albiononline.com/api/gameinfo/players/QPELoDHRQwWI3-yhzAGYmA/kills


main()
test.start()
bot.run(TOKEN)


