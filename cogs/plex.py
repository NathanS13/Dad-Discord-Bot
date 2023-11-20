import os
import asyncio
from discord.ext import commands

from src import utils

class Plex_Bot(commands.Cog):

    def __init__(self, bot):
        print('init')
        self.bot = bot

    @commands.command(name='request')
    async def plex_request(self, ctx):
        request = ctx.message.clean_content[len(ctx.prefix) + len(ctx.command.name):].strip()
        await ctx.send(f'Plex Request: {request}')
        path = os.path.join('/share', 'Random', 'Discord', 'requests.txt') if 'posix' in os.name \
            else os.path.join(os.getcwd(), 'request.txt')
        print(path)
        with open(path, 'r+', encoding='utf-8') as file:
            for line in file:
                #print('request compare: ', request, line)
                if request == line.strip():
                    await ctx.send(f'Request {request} already exists, check the list with \'.request_list\'')
                    file.close()
                    return
            file.write(f'{request}\n')
            await self.alert_plex_admins(request)

    @commands.command(name='request_list')
    async def plex_request_list(self, ctx):
        print('request_list called')
        path = os.path.join('/share', 'Random', 'Discord', 'requests.txt')
        with open(path, 'r', encoding='utf-8') as file:
            file_data = file.read()
            print(file_data)
            await ctx.send(file_data)

    #@commands.Cog.listen('plex_request')
    @commands.Cog.listener()
    async def alert_plex_admins(self, message):
        channel = self.bot.get_channel(1146933704057442395) # aionions
        #channel = self.bot.get_channel(816437844507492365) #debug
        #members = [118156033720844291, 118192661822832646] # aionios
        #members = [118156033720844291] # debug

        path = os.path.join(os.getcwd(), 'the_boys.json')
        members = utils.batch_user_list(path, 'plex_tag', True)

        if len(members > 0):
            member_list = [channel.guild.get_member(member).mention for member in members]
            await channel.send(f"{' '.join(member_list)} New Movie request: {message}")

    @commands.command(name='subscribe')
    async def subscribe_alert_request(self, ctx):
        channel = self.bot.get_channel(1146933704057442395)
        print('subscribe new user')
        path = os.path.join(os.getcwd(), 'the_boys.json')
        if utils.replace_value(path, int(ctx.message.author.id), 'plex_tag', True):
            await channel.send(f"{ctx.message.author.mention} You subscribed to nas alerts!")

    @commands.command(name='unsubscribe')
    async def unsubscribe_alert_request(self, ctx):
        channel = self.bot.get_channel(1146933704057442395)
        print('subscribe new user')
        path = os.path.join(os.getcwd(), 'the_boys.json')
        if utils.replace_value(path, int(ctx.message.author.id), 'plex_tag', False):
            await channel.send(f"{ctx.message.author.mention} You unsubscribed from nas alerts!")

async def setup(bot):
    await bot.add_cog(Plex_Bot(bot))
