from discord.ext import commands

class Albion_Tracker(commands.Cog):

    def __init__(self, bot):
        print('init')
        self.bot = bot

#   @commands.command(name='ping2')
#   async def ping2(self, ctx):
#       print('ping recieve')
#       await ctx.send('pong')
#       await ctx.send('mush id: ' + str(ctx.message.author.id))
#       await ctx.send('server id: ' + str(ctx.guild.id))
#       await ctx.send('channel id: ' + str(ctx.channel.id))
#
#    def checkMushy(ctx):
#        return ctx.message.author.id == 118156033720844291
#
#    #@bot.command()
#    async def dadhelp(ctx):
#        await ctx.send('Hey son, I saw you needed help.\n\n Here\'s what I can do for you: \n .track playername\n .untrack playername')
#        #await ctx.send(file=discord.File('test3.png'))
#
#    #@tasks.loop(minutes=5)
#    async def test(bot):
#        print('in albion tracker')
#        channel = bot.get_channel(868319514566230057) #861996836435918889 aionios. current test
#        channel2 = bot.get_channel(861996836435918889)
#        playerUpdates = checkEventUpdate()            #868319514566230057 tkx
#                                                    #816437844507492365 test
#        print('player update: \n' )
#        print(playerUpdates)
#        for x in range(0, len(playerUpdates), 8):
#            print(len(playerUpdates))
#
#            i.pullImages(playerUpdates[x+6])
#            i.pullImages(playerUpdates[x+7])
#            image1 = i.generateImage(playerUpdates[x+6])
#            image2 = i.generateImage(playerUpdates[x+7])
#            finalImage = i.mergeKill(image1, image2, playerUpdates[x+1], playerUpdates[x+5],
#                                    playerUpdates[x+2], playerUpdates[x+3], playerUpdates[x+4]) #send a list idiot
#            #await channel.send('Good job kiddo you killed ' + playerUpdates[x+5])
#            with io.BytesIO() as image_binary:
#                        finalImage.save(image_binary, 'PNG')
#                        image_binary.seek(0)
#                        #await channel.send(file=discord.File(fp=image_binary, filename='finalImage.png'))
#            await channel2.send('Good job kiddo you killed ' + playerUpdates[x+5])
#            with io.BytesIO() as image_binary:
#                        finalImage.save(image_binary, 'PNG')
#                        image_binary.seek(0)
#                        await channel2.send(file=discord.File(fp=image_binary, filename='finalImage.png'))
#        playerUpdates = []
#
#    #@test.before_loop
#    async def before():
#        await bot.wait_until_ready()
#
#    #@bot.command()
#    #@commands.check(checkMushy)
#    @commands.command(name='ping')
#    async def ping(self, ctx):
#        print('ping recieve')
#        await ctx.send('pong')
#        await ctx.send('mush id: ' + str(ctx.message.author.id))
#        await ctx.send('server id: ' + str(ctx.guild.id))
#        await ctx.send('channel id: ' + str(ctx.channel.id))
#
#    #@bot.command()
#    #@commands.check(checkMushy)
#    async def proud(ctx, name='Kiddo'):
#        await ctx.send('Well ' + name + ' you didn\'t quite score a kill but im proud of you.' )
#
#    #@bot.command()
#    #@commands.check(checkMushy)
#    async def clear(ctx, amount=10):
#        await ctx.channel.purge(limit=amount)
#
#    #@bot.command()
#    #@commands.check(checkMushy)
#    async def getTrackList(ctx):
#        with open("players/tracklist.txt", "rb") as file:
#            await ctx.send("Current Track List:", file=discord.File(file, "tracklist.txt"))
#            #tracklist = f.printTrackList()
#            #for line in tracklist:
#            #    await ctx.send(line)
#
#    #@bot.command()
#    #@commands.check(checkMushy)
#    async def track(ctx, playername):
#        #checkTracking = track_player(playername)
#        if (f.checksave(playername) and f.checkLineCount(playername)):
#            await ctx.send('Already tracking: ' + playername)
#
#        elif (f.checksave(playername) and not f.checkLineCount(playername)):
#            await ctx.send('I see an issue with ' + playername + '\'s tracking.. Please try using the command \".track ' + playername + '\" again.')
#            await untrack(ctx, playername)
#        else:
#            await ctx.send('Looking up: ' + playername)
#            playerid = get_player_id(playername)
#            if (playerid == ''):
#                await ctx.send("Couldn't find Albion player. Usernames are CaSe SeNsItIvE..")
#            elif (playerid != ''):
#                f.savefile(playername, playerid)
#                await ctx.send('Found Albion player!: ' + playername)
#                await ctx.send('Saving last few pvp kills..')
#                get_kills(playername, playerid)
#                await ctx.send('Now tracking: ' + playername)
#            else:
#                await ctx.send("Unexpected Error")
#
#        #await ctx.send('Now tracking albion player: ' + playername + ' with id: ')
#
#    #@bot.command()
#    async def untrack(ctx, playername):
#        f.clearfile(playername)
#        await ctx.send('Cleared player ' + playername + "!")
#
#    #@bot.command()
#    #@commands.check(checkMushy)
#    async def clearplayers_remove_all_warning(ctx):
#        f.clearfiles()
#        await ctx.send('cleared!')
#
#    #@bot.command()
#    #@commands.check(checkMushy)
#    async def forceUpdate(ctx, playername='Mushii'):
#        f.forcePlayerUpdate(playername)
#        await test()
#        #await ping(ctx)
#        await ctx.send('update sent')
#
#    #@bot.command()
#    #@commands.check(checkMushy)
#    async def forceUpdate2(ctx, playername='Mushii'):
#        await test()
#        #await ping(ctx)
#        await ctx.send('update sent')
#
#    #def track_player(username):
#    #    print('in track player')
#    #    if (f.checksave(username)):
#    #        return True
#    #    else:
#    #        f.savefile(username, 'this is a test')
#    #        return False
#
#    def get_player_id(username):
#        url = 'https://gameinfo.albiononline.com/api/gameinfo/search?q=' + username
#        #operUrl = urllib.request.urlopen(url)
#        #if(operUrl.getcode()==200):
#        #    data = operUrl.read()
#        #    jsonData = json.loads(data)
#        #else:
#        #    print("Error receiving data", operUrl.getcode())
#
#        try:
#            operUrl = urllib.request.urlopen(url)
#            if(operUrl.getcode()==200):
#                data = operUrl.read()
#                jsonData = json.loads(data)
#        except HTTPError as e:
#            if e.code == 502:
#                operUrl = urllib.request.urlopen(url)
#            else:
#                print('Failure opening link!')
#                return ''
#
#
#        #could be bad code. Duplicate names like Mushii will grab last
#        #doesnt appear to be an issue for other look ups. I did recreate
#        #character Mushii, which is how I noticed double names in lookup
#        u_id = ''
#        for user in jsonData['players']:
#            u_name = user.get('Name')
#            if (u_name == username):
#                #print('Found user ' + u_id)
#                u_id = user.get('Id')
#
#        return u_id
#
#    def get_kills(username, playerId, jsonData=[]):
#
#        if (jsonData == []):
#            print("Looking up kills for " + username)
#            url = 'https://gameinfo.albiononline.com/api/gameinfo/players/' + playerId + '/kills'
#            operUrl = urllib.request.urlopen(url)
#            if(operUrl.getcode()==200):
#                data = operUrl.read()
#                jsonData = json.loads(data)
#            else:
#                print("Error receiving data", operUrl.getcode())
#
#
#        alist = []
#        blist = []
#        for kill in reversed(jsonData):
#            if (kill['Killer']['AverageItemPower']):
#                killerAvgIP = kill['Killer']['AverageItemPower']
#            else:
#                killerAvgIP = '0'
#            if (kill['Killer']['Equipment']['MainHand']):
#                alist.append(kill['Killer']['Equipment']['MainHand']['Type'])
#            else:
#                alist.append('EMPTY')
#            if (kill['Killer']['Equipment']['OffHand']):
#                alist.append(kill['Killer']['Equipment']['OffHand']['Type'])
#            else:
#                alist.append('EMPTY')
#            if (kill['Killer']['Equipment']['Head']):
#                alist.append(kill['Killer']['Equipment']['Head']['Type'])
#            else:
#                alist.append('EMPTY')
#            if (kill['Killer']['Equipment']['Armor']):
#                alist.append(kill['Killer']['Equipment']['Armor']['Type'])
#            else:
#                alist.append('EMPTY')
#            if (kill['Killer']['Equipment']['Shoes']):
#                alist.append(kill['Killer']['Equipment']['Shoes']['Type'])
#            else:
#                alist.append('EMPTY')
#            if (kill['Killer']['Equipment']['Bag']):
#                alist.append(kill['Killer']['Equipment']['Bag']['Type'])
#            else:
#                alist.append('EMPTY')
#            if (kill['Killer']['Equipment']['Cape']):
#                alist.append(kill['Killer']['Equipment']['Cape']['Type'])
#            else:
#                alist.append('EMPTY')
#            if (kill['Killer']['Equipment']['Mount']):
#                alist.append(kill['Killer']['Equipment']['Mount']['Type'])
#            else:
#                alist.append('EMPTY')
#            if (kill['Killer']['Equipment']['Potion']):
#                alist.append(kill['Killer']['Equipment']['Potion']['Type'])
#            else:
#                alist.append('EMPTY')
#            if (kill['Killer']['Equipment']['Food']):
#                alist.append(kill['Killer']['Equipment']['Food']['Type'])
#            else:
#                alist.append('EMPTY')
#
#
#            if (kill['Victim']['Name']):
#                victimName = kill['Victim']['Name']
#            else:
#                victimName = 'None'
#            if (kill['Victim']['AverageItemPower']):
#                victimAvgIP = kill['Victim']['AverageItemPower']
#            else:
#                victimAvgIP = '0'
#            if (kill['TotalVictimKillFame']):
#                killfame = kill['TotalVictimKillFame']
#            else:
#                killfame = '0'
#            if (kill['Victim']['Equipment']['MainHand']):
#                blist.append(kill['Victim']['Equipment']['MainHand']['Type'])
#            else:
#                blist.append('EMPTY')
#            if (kill['Victim']['Equipment']['OffHand']):
#                blist.append(kill['Victim']['Equipment']['OffHand']['Type'])
#            else:
#                blist.append('EMPTY')
#            if (kill['Victim']['Equipment']['Head']):
#                blist.append(kill['Victim']['Equipment']['Head']['Type'])
#            else:
#                blist.append('EMPTY')
#            if (kill['Victim']['Equipment']['Armor']):
#                blist.append(kill['Victim']['Equipment']['Armor']['Type'])
#            else:
#                blist.append('EMPTY')
#            if (kill['Victim']['Equipment']['Shoes']):
#                blist.append(kill['Victim']['Equipment']['Shoes']['Type'])
#            else:
#                blist.append('EMPTY')
#            if (kill['Victim']['Equipment']['Bag']):
#                blist.append(kill['Victim']['Equipment']['Bag']['Type'])
#            else:
#                blist.append('EMPTY')
#            if (kill['Victim']['Equipment']['Cape']):
#                blist.append(kill['Victim']['Equipment']['Cape']['Type'])
#            else:
#                blist.append('EMPTY')
#            if (kill['Victim']['Equipment']['Mount']):
#                blist.append(kill['Victim']['Equipment']['Mount']['Type'])
#            else:
#                blist.append('EMPTY')
#            if (kill['Victim']['Equipment']['Potion']):
#                blist.append(kill['Victim']['Equipment']['Potion']['Type'])
#            else:
#                blist.append('EMPTY')
#            if (kill['Victim']['Equipment']['Food']):
#                blist.append(kill['Victim']['Equipment']['Food']['Type'])
#            else:
#                blist.append('EMPTY')
#
#            #killMoney, victimMoney = checkMarket(alist, blist)
#
#            f.savefile2(username, kill['EventId'], alist, blist, victimName, killerAvgIP, victimAvgIP, killfame)
#            alist.clear()
#            blist.clear()
#
#
#        #print(jsonData[0]['Victim'])
#
#    def getprice(itemName):
#        url = 'https://www.albion-online-data.com/api/v2/stats/prices/' + itemName + '?locations=Thetford,FortSterling,Lymhurst,Bridgewatch,Martlock,Caerleon&qualities=1'
#        #url2 = 'https://www.albion-online-data.com/api/v2/stats/prices/' + itemStringVictim + '?locations=Lymhurst&qualities=1'
#
#        #url = 'https://www.albion-online-data.com/api/v2/stats/history/' + itemStringKill + '?date=5-1-2021&end_date=5-6-2021&locations=FortSterling&qualities=1&time-scale=24'
#        #url2 = 'https://www.albion-online-data.com/api/v2/stats/history/' + itemStringVictim + '?date=5-1-2021&end_date=5-6-2021&locations=FortSterling&qualities=1&time-scale=24'
#        operUrl = urllib.request.urlopen(url)
#        if(operUrl.getcode()==200):
#            data = operUrl.read()
#            jsonData = json.loads(data)
#        else:
#            print("Error receiving data", operUrl.getcode())
#
#        print('Checking item ' + itemName)
#        min = -1
#        for city in jsonData:
#            price = city['sell_price_min']
#            if ((price < min or min == -1) and price != 0):
#                min = price
#
#        minCompare = min * 5
#        sum = 0
#        cities = 0
#        for city in jsonData:
#            price = city['sell_price_min']
#            if (not (price > minCompare)):
#                sum += price
#                cities += 1
#
#        finalSum = sum/cities
#
#        return min
#
#
#    #https://www.albion-online-data.com/api/v2/stats/prices/T4_BAG,T5_BAG?locations=FortSterling&qualities=1
#    #https://www.albion-online-data.com/api/v2/stats/history/T4_BAG?date=5-1-2021&end_date=5-6-2021&locations=Caerleon&qualities=2&time-scale=24
#    #does not care about potion amount FIX sometime.
#    def checkMarket(killList, victimList):
#
#        #itemStringKill = ""
#        #itemStringVictim = ""
#        #for item in killList:
#        #    if (item != 'EMPTY'):
#        #        itemStringKill += (item + ',')
#        #itemStringKill = itemStringKill[:-1]
#        #for item in victimList:
#        #    if (item != 'EMPTY'):
#        #        itemStringVictim += (item + ',')
#        #itemStringVictim = itemStringVictim[:-1]
#
#        #print (itemStringKill)
#        #print (itemStringVictim)
#        #print(getprice(killList[0]))
#
#        sumKiller = 0
#        for kill in killList:
#            if (kill != 'EMPTY'):
#                sumKiller += getprice(kill)
#
#        sumVictim = 0
#        for kill in victimList:
#            if (kill != 'EMPTY'):
#                sumVictim += getprice(kill)
#
#        return sumKiller, sumVictim
#
#
#
#    #optimize this by making player id a tuple within the tracking list
#    #take out the unique id in normal player kill logs
#    #optimize more, we assume only 1 kill at a time - we can fix this with
#    #some sort of algo
#    def checkEventUpdate():
#        playerList = f.getListOfTrack()
#        returnlist = []
#        for player in playerList:
#
#            playerId = f.getPlayerId(player)
#            if (playerId == 0):
#                continue
#
#            url = 'https://gameinfo.albiononline.com/api/gameinfo/players/' + playerId + '/kills'
#            operUrl = urllib.request.urlopen(url)
#            if (operUrl.getcode()==200):
#                data = operUrl.read()
#                jsonData = json.loads(data)
#            else:
#                print("Error receiving data", operUrl.getcode())
#
#            #print('checking latest for ' + player + ' ' + str(jsonData[0]['EventId']))
#            #add error check here for a failed json fetch
#            #print('playername ' + player + ' ' + url)
#
#            if (jsonData != []):
#                jsonEventId = jsonData[0]['EventId']
#
#                tempLastEvent = int(f.getlastevent(player))
#                #tempLastEvent = 257509874
#                if (tempLastEvent != -1):
#                    print('last JSON for ' + player + ' ' + str(jsonEventId))
#                    print('last FILE event for ' + player + ' ' + str(tempLastEvent))
#                    #add a way to initialize a first kill for a player here!!!! -- think done
#                i = 1
#                while (tempLastEvent != -1 and jsonEventId != tempLastEvent and jsonEventId != -1 and i != 10):
#                #if (tempLastEvent != -1 and jsonEventId != tempLastEvent):
#                    if (i == 1):
#                        f.clearfile(player)
#                        f.savefile(player, playerId)
#                        get_kills(player, playerId, jsonData)
#                    #add check wealth here
#                    #call to display last kill?
#                    #if (tempLastEvent != 1)
#                    #print('i ' + str(i))
#                    tempLastKillerName = f.getlastline(player, (6 + ((i-1) * 7)))
#                    tempLastKillFame = f.getlastline(player, (5 + ((i-1) * 7)))
#                    tempLastKillIP = f.getlastline(player, (4 + ((i-1) * 7)))
#                    tempLastVictimIP = f.getlastline(player, (3 + ((i-1) * 7)))
#                    tempLastKiller = f.getlastline(player, (2 + ((i-1) * 7)))
#                    tempLastVictim = f.getlastline(player, (1 + ((i-1) * 7)))
#
#                    #print('name '+tempLastKillerName)
#                    returnlist.insert(0, jsonEventId) #1
#                    returnlist.insert(1, player) #2
#                    returnlist.insert(2, tempLastKillFame) #3
#                    returnlist.insert(3, tempLastKillIP) #4
#                    returnlist.insert(4, tempLastVictimIP) #5
#                    returnlist.insert(5, tempLastKillerName) #6
#                    returnlist.insert(6, tempLastKiller) #7
#                    returnlist.insert(7, tempLastVictim) #8
#
#                    #if (jsonData[i]['EventId']):
#                    #    jsonEventId = jsonData[i]['EventId']
#                    i += 1
#                    #jsonEventId = tempLastEvent
#                    if (tempLastEvent != 1):
#                        jsonEventId = int(f.getlastevent(player, i))
#                    else:
#                        jsonEventId = tempLastEvent
#                    print ('my temp last event: ' + str(tempLastEvent) + ' json evnt id: ' + str(jsonEventId))
#
#        return returnlist