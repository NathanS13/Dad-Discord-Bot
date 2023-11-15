import os
import asyncio
from discord.ext import commands

class Core_Bot(commands.Cog):

    def __init__(self, bot):
        print('init')
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} has joined the server.')
        #await guild.send('Welcome to the server kiddo! {member} Make us proud')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left the server.')

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        print('inside!')

    @commands.command(name='ping2')
    async def ping2(self, ctx):
        print('ping recieve')
        await ctx.send('pong')
        await ctx.send('mush id: ' + str(ctx.message.author.id))
        await ctx.send('server id: ' + str(ctx.guild.id))
        await ctx.send('channel id: ' + str(ctx.channel.id))

    @commands.command(name='test2')
    async def test2(self, ctx):
        print('????????????????')
        await ctx.send('Test command works!')

    @commands.Cog.listener()
    async def on_message(self, message):
        print(f'Message received: {message.content}')

    @commands.command(name='request')
    async def plex_request(self, ctx):
        request = ctx.message.clean_content[len(ctx.prefix) + len(ctx.command.name):].strip()
        await ctx.send(f'Plex Request: {request}')
        path = os.path.join('/share', 'Random', 'Discord', 'requests.txt')
        with open(path, 'r+', encoding='utf-8') as file:
            for line in file:
                #print('request compare: ', request, line)
                if request == line.strip():
                    await ctx.send(f'Request {request} already exists, check the list with \'.request_list\'')
                    file.close()
                    return
            file.write(f'{request}\n')

    @commands.command(name='request_list')
    async def plex_request_list(self, ctx):
        print('request_list called')
        path = os.path.join('/share', 'Random', 'Discord', 'requests.txt')
        with open(path, 'r', encoding='utf-8') as file:
            file_data = file.read()
            print(file_data)

            await ctx.send(file_data)



async def setup(bot):
    await bot.add_cog(Core_Bot(bot))