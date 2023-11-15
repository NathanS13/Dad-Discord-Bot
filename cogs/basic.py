import asyncio, discord
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


async def setup(bot):
    await bot.add_cog(Core_Bot(bot))