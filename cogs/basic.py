import os
import asyncio
from discord.ext import commands
import discord
import traceback

class Core_Bot(commands.Cog):

    def __init__(self, bot):
        print('init')
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(348996870434979841) # aionions
        print(f'{member} has joined the server.')
        await channel.send(f'Welcome to the server kiddo! {member} Make us proud!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(348996870434979841) # aionions
        print(f'{member} has left the server.')
        await channel.send(f'See ya later kiddo! {member}')

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
        await ctx.send('Test command works!')

    @commands.Cog.listener()
    async def on_message(self, message):
        print(f'Message received: {message.content}')

    @commands.command(name='getids')
    async def getids(self, ctx):
        try:
            guild = ctx.guild

            shitty_boy = "Shitty Boys"
            shitty_girl = "Shitty Grills"

            role1 = discord.utils.get(guild.roles, name=shitty_boy) #Shitty Boys Tag
            role2 = discord.utils.get(guild.roles, name=shitty_girl) #Shitty Girls Tag

            members_role1 = role1.members
            members_role2 = role2.members

            user_ids_role1 = [member.id for member in members_role1]
            user_ids_role2 = [member.id for member in members_role2]

            user_names_role1 = [member.name for member in members_role1]
            user_names_role2 = [member.name for member in members_role2]

            final_list1 = [f"{user_id} ({user_name})" for user_id, user_name in zip(user_names_role1, user_ids_role1)]
            final_list2 = [f"{user_id} ({user_name})" for user_id, user_name in zip(user_names_role2, user_ids_role2)]

            result_str1 = '\n'.join(map(str, final_list1))
            result_str2 = '\n'.join(map(str, final_list2))
            
            await ctx.send(f"User IDs for {shitty_boy}:\n{result_str1}")
            await ctx.send(f"User IDs for {shitty_girl}:\n{result_str2}")
        
        except Exception as e:
            traceback_str = traceback.format_exc(limit=10)
            print("ERROR!", e)
            print(traceback_str)

async def setup(bot):
    await bot.add_cog(Core_Bot(bot))