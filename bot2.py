import os
import discord
import urllib.request
import json
import ast
import fileio as f
import imageprocess as i
import time
import io
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext import tasks

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


bot = commands.Bot(command_prefix='.', intents=intents)

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

@bot.command(aliases='dadhelp')
async def help(ctx, message):
    await ctx.send('Hey son, I saw you needed help.\n\n Here what I can do for you: \n\n .track playername')
    #await ctx.send(file=discord.File('test3.png'))

def checkMushy(ctx):
    return ctx.message.author.id == 118156033720844291

@tasks.loop(minutes=5)
async def test():
    channel = bot.get_channel(868319514566230057) #861996836435918889 aionios. current test
    channel2 = bot.get_channel(861996836435918889)
    playerUpdates = checkEventUpdate()            #868319514566230057 tkx
                                                  #816437844507492365 test
    print('player update: \n' )
    print(playerUpdates)
    for x in range(0, len(playerUpdates), 8):
        print(len(playerUpdates))

        i.pullImages(playerUpdates[x+6])
        i.pullImages(playerUpdates[x+7])
        image1 = i.generateImage(playerUpdates[x+6])
        image2 = i.generateImage(playerUpdates[x+7])
        finalImage = i.mergeKill(image1, image2, playerUpdates[x+1], playerUpdates[x+5],
                                playerUpdates[x+2], playerUpdates[x+3], playerUpdates[x+4]) #send a list idiot
        with io.BytesIO() as image_binary:
                    finalImage.save(image_binary, 'PNG')
                    image_binary.seek(0)
                    await channel.send(file=discord.File(fp=image_binary, filename='finalImage.png'))
        with io.BytesIO() as image_binary:
                    finalImage.save(image_binary, 'PNG')
                    image_binary.seek(0)
                    await channel2.send(file=discord.File(fp=image_binary, filename='finalImage.png'))
    playerUpdates = []



        #i.pullImages(2)
        #i.pullImages(3)
        #image1 = generateImage(itemList2)
        #image2 = generateImage(itemList2)

        #call image updater here
        #clear the playerUpdates list

@test.before_loop
async def before():
    await bot.wait_until_ready()

@bot.command()
@commands.check(checkMushy)
async def ping(ctx):
    await ctx.send('pong')
    await ctx.send('mush id: ' + str(ctx.message.author.id))
    await ctx.send('server id: ' + str(ctx.guild.id))
    await ctx.send('channel id: ' + str(ctx.channel.id))
    #await ctx.send(file=discord.File('test3.png'))
    #checkEventUpdate()

@bot.command()
@commands.check(checkMushy)
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

@bot.command()
@commands.check(checkMushy)
async def track(ctx, playername):
    #checkTracking = track_player(playername)
    if (f.checksave(playername) and f.checkLineCount(playername)):
        await ctx.send('Already tracking: ' + playername)
    else:
        await ctx.send('Looking up: ' + playername)
        playerid = get_player_id(playername)
        if (playerid == ''):
            await ctx.send("Couldn't find Albion player. Usernames are CaSe SeNsItIvE..")
        elif (playerid != ''):
            f.savefile(playername, playerid)
            await ctx.send('Found Albion player!: ' + playername)
            await ctx.send('Saving last few pvp kills..')
            get_kills(playername, playerid)
            await ctx.send('Now tracking: ' + playername)
        else:
            await ctx.send("Unexpected Error")

    #await ctx.send('Now tracking albion player: ' + playername + ' with id: ')

@bot.command()
@commands.check(checkMushy)
async def clearplayers(ctx):
    f.clearfiles()
    await ctx.send('cleared!')

@bot.command()
@commands.check(checkMushy)
async def forceUpdate(ctx, playername='Mushii'):
    f.forcePlayerUpdate(playername)
    await test()
    #await ping(ctx)
    await ctx.send('update sent')

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
    print("Looking up kills for " + username)
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
        if (kill['Killer']['AverageItemPower']):
            killerAvgIP = kill['Killer']['AverageItemPower']
        else:
            killerAvgIP = '0'
        if (kill['Killer']['Equipment']['MainHand']):
            alist.append(kill['Killer']['Equipment']['MainHand']['Type'])
        else:
            alist.append('EMPTY')
        if (kill['Killer']['Equipment']['OffHand']):
            alist.append(kill['Killer']['Equipment']['OffHand']['Type'])
        else:
            alist.append('EMPTY')
        if (kill['Killer']['Equipment']['Head']):
            alist.append(kill['Killer']['Equipment']['Head']['Type'])
        else:
            alist.append('EMPTY')
        if (kill['Killer']['Equipment']['Armor']):
            alist.append(kill['Killer']['Equipment']['Armor']['Type'])
        else:
            alist.append('EMPTY')
        if (kill['Killer']['Equipment']['Shoes']):
            alist.append(kill['Killer']['Equipment']['Shoes']['Type'])
        else:
            alist.append('EMPTY')
        if (kill['Killer']['Equipment']['Bag']):
            alist.append(kill['Killer']['Equipment']['Bag']['Type'])
        else:
            alist.append('EMPTY')
        if (kill['Killer']['Equipment']['Cape']):
            alist.append(kill['Killer']['Equipment']['Cape']['Type'])
        else:
            alist.append('EMPTY')
        if (kill['Killer']['Equipment']['Mount']):
            alist.append(kill['Killer']['Equipment']['Mount']['Type'])
        else:
            alist.append('EMPTY')
        if (kill['Killer']['Equipment']['Potion']):
            alist.append(kill['Killer']['Equipment']['Potion']['Type'])
        else:
            alist.append('EMPTY')
        if (kill['Killer']['Equipment']['Food']):
            alist.append(kill['Killer']['Equipment']['Food']['Type'])
        else:
            alist.append('EMPTY')


        if (kill['Victim']['Name']):
            victimName = kill['Victim']['Name']
        else:
            victimName = 'None'
        if (kill['Victim']['AverageItemPower']):
            victimAvgIP = kill['Victim']['AverageItemPower']
        else:
            victimAvgIP = '0'
        if (kill['TotalVictimKillFame']):
            killfame = kill['TotalVictimKillFame']
        else:
            killfame = '0'
        if (kill['Victim']['Equipment']['MainHand']):
            blist.append(kill['Victim']['Equipment']['MainHand']['Type'])
        else:
            blist.append('EMPTY')
        if (kill['Victim']['Equipment']['OffHand']):
            blist.append(kill['Victim']['Equipment']['OffHand']['Type'])
        else:
            blist.append('EMPTY')
        if (kill['Victim']['Equipment']['Head']):
            blist.append(kill['Victim']['Equipment']['Head']['Type'])
        else:
            blist.append('EMPTY')
        if (kill['Victim']['Equipment']['Armor']):
            blist.append(kill['Victim']['Equipment']['Armor']['Type'])
        else:
            blist.append('EMPTY')
        if (kill['Victim']['Equipment']['Shoes']):
            blist.append(kill['Victim']['Equipment']['Shoes']['Type'])
        else:
            blist.append('EMPTY')
        if (kill['Victim']['Equipment']['Bag']):
            blist.append(kill['Victim']['Equipment']['Bag']['Type'])
        else:
            blist.append('EMPTY')
        if (kill['Victim']['Equipment']['Cape']):
            blist.append(kill['Victim']['Equipment']['Cape']['Type'])
        else:
            blist.append('EMPTY')
        if (kill['Victim']['Equipment']['Mount']):
            blist.append(kill['Victim']['Equipment']['Mount']['Type'])
        else:
            blist.append('EMPTY')
        if (kill['Victim']['Equipment']['Potion']):
            blist.append(kill['Victim']['Equipment']['Potion']['Type'])
        else:
            blist.append('EMPTY')
        if (kill['Victim']['Equipment']['Food']):
            blist.append(kill['Victim']['Equipment']['Food']['Type'])
        else:
            blist.append('EMPTY')

        #killMoney, victimMoney = checkMarket(alist, blist)

        f.savefile2(username, kill['EventId'], alist, blist, victimName, killerAvgIP, victimAvgIP, killfame)
        alist.clear()
        blist.clear()


    #print(jsonData[0]['Victim'])

def getprice(itemName):
    url = 'https://www.albion-online-data.com/api/v2/stats/prices/' + itemName + '?locations=Thetford,FortSterling,Lymhurst,Bridgewatch,Martlock,Caerleon&qualities=1'
    #url2 = 'https://www.albion-online-data.com/api/v2/stats/prices/' + itemStringVictim + '?locations=Lymhurst&qualities=1'

    #url = 'https://www.albion-online-data.com/api/v2/stats/history/' + itemStringKill + '?date=5-1-2021&end_date=5-6-2021&locations=FortSterling&qualities=1&time-scale=24'
    #url2 = 'https://www.albion-online-data.com/api/v2/stats/history/' + itemStringVictim + '?date=5-1-2021&end_date=5-6-2021&locations=FortSterling&qualities=1&time-scale=24'
    operUrl = urllib.request.urlopen(url)
    if(operUrl.getcode()==200):
        data = operUrl.read()
        jsonData = json.loads(data)
    else:
        print("Error receiving data", operUrl.getcode())

    print('Checking item ' + itemName)
    min = -1
    for city in jsonData:
        price = city['sell_price_min']
        if ((price < min or min == -1) and price != 0):
            min = price




    minCompare = min * 5
    sum = 0
    cities = 0
    for city in jsonData:
        price = city['sell_price_min']
        if (not (price > minCompare)):
            sum += price
            cities += 1

    finalSum = sum/cities

    return min


#https://www.albion-online-data.com/api/v2/stats/prices/T4_BAG,T5_BAG?locations=FortSterling&qualities=1
#https://www.albion-online-data.com/api/v2/stats/history/T4_BAG?date=5-1-2021&end_date=5-6-2021&locations=Caerleon&qualities=2&time-scale=24
#does not care about potion amount FIX sometime.
def checkMarket(killList, victimList):

    #itemStringKill = ""
    #itemStringVictim = ""
    #for item in killList:
    #    if (item != 'EMPTY'):
    #        itemStringKill += (item + ',')
    #itemStringKill = itemStringKill[:-1]
    #for item in victimList:
    #    if (item != 'EMPTY'):
    #        itemStringVictim += (item + ',')
    #itemStringVictim = itemStringVictim[:-1]

    #print (itemStringKill)
    #print (itemStringVictim)
    #print(getprice(killList[0]))

    sumKiller = 0
    for kill in killList:
        if (kill != 'EMPTY'):
            sumKiller += getprice(kill)

    sumVictim = 0
    for kill in victimList:
        if (kill != 'EMPTY'):
            sumVictim += getprice(kill)

    return sumKiller, sumVictim



#optimize this by making player id a tuple within the tracking list
#take out the unique id in normal player kill logs
#optimize more, we assume only 1 kill at a time - we can fix this with
#some sort of algo
def checkEventUpdate():
    playerList = f.getListOfTrack()
    returnlist = []
    for player in playerList:

        playerId = f.getPlayerId(player)

        url = 'https://gameinfo.albiononline.com/api/gameinfo/players/' + playerId + '/kills'
        operUrl = urllib.request.urlopen(url)
        if(operUrl.getcode()==200):
            data = operUrl.read()
            jsonData = json.loads(data)
        else:
            print("Error receiving data", operUrl.getcode())

        #print('checking latest for ' + player + ' ' + str(jsonData[0]['EventId']))
        tempLastEvent = f.getlastevent(player)
        if (tempLastEvent != -1):
            print('checking latest for ' + player + ' ' + str(jsonData[0]['EventId']))
            print('last event for ' + player + ' ' + tempLastEvent)
        #add a way to initialize a first kill for a player here!!!!
        if (tempLastEvent != -1 and str(jsonData[0]['EventId']) != tempLastEvent):
            f.clearfile(player)
            f.savefile(player, playerId)
            get_kills(player, playerId)
            #add check wealth here
            #call to display last kill?
            tempLastKillerName = f.getlastline(player, 6)

            tempLastKillFame = f.getlastline(player, 5) #
            tempLastKillIP = f.getlastline(player, 4) #
            tempLastVictimIP = f.getlastline(player, 3) #

            #tempLastKillMoney = f.getlastline(player, 4)
            #tempLastKillVictimMoney = f.getlastline(player, 3)

            tempLastKiller = f.getlastline(player, 2)
            tempLastVictim = f.getlastline(player, 1)


            returnlist.append(tempLastEvent)
            returnlist.append(player)

            returnlist.append(tempLastKillFame) #
            returnlist.append(tempLastKillIP) #
            returnlist.append(tempLastVictimIP) #

            #returnlist.append(tempLastKillMoney)
            #returnlist.append(tempLastKillVictimMoney)

            returnlist.append(tempLastKillerName)
            returnlist.append(tempLastKiller)
            returnlist.append(tempLastVictim)
            #print('killer ' + tempLastKiller)
            #print('victim ' + tempLastVictim)
    return returnlist




def main():

    print('hello')
    #x, y = checkMarket(['T4_2H_IRONGAUNTLETS_HELL@2', 'EMPTY', 'T4_HEAD_LEATHER_SET3@2', 'T5_ARMOR_CLOTH_SET2@1', 'T4_SHOES_LEATHER_HELL@2', 'T4_BAG', 'T4_CAPEITEM_FW_THETFORD@2', 'T3_MOUNT_HORSE', 'EMPTY', 'EMPTY'],
    #['T6_2H_CLAWPAIR', 'EMPTY', 'T5_HEAD_CLOTH_SET3', 'T5_ARMOR_LEATHER_SET3', 'T6_SHOES_LEATHER_SET1', 'T4_BAG@1', 'T4_CAPEITEM_DEMON@2', 'T3_MOUNT_HORSE', 'T6_POTION_COOLDOWN', 'T8_MEAL_STEW@1'])

    #print (str(x) + " " + str(y))
    #playerUpdates = []
    #playerUpdates = checkEventUpdate()
    #if (len(playerUpdates) > 0):
        #print ('new kill from main')
        #print (playerUpdates)
        #print()













#playerName = data["Id"]



#https://gameinfo.albiononline.com/api/gameinfo/search?q=Mushii
#QPELoDHRQwWI3-yhzAGYmA
#https://gameinfo.albiononline.com/api/gameinfo/players/QPELoDHRQwWI3-yhzAGYmA/kills
#https://render.albiononline.com/v1/item/T4_OFF_SHIELD.png

main()
test.start()
bot.run(TOKEN)
