import os
import asyncio
import datetime
from discord.ext import commands, tasks

from src import utils

utc = datetime.timezone.utc

# If no tzinfo is given then UTC is assumed.
times = [
    datetime.time(hour=13, tzinfo=utc),
    #datetime.time(hour=22, minute=54, tzinfo=utc),
    #datetime.time(hour=16, minute=40, second=30, tzinfo=utc)
]

class Birthday_Bot(commands.Cog):

    def __init__(self, bot):
        print('init birthday bot')
        self.bot = bot
        self.birthday_check.start()

    def cog_unload(self):
        self.birthday_check.cancel()

    @tasks.loop(time=times)
    async def birthday_check(self):
        print('Birthday Timed Event')
        channel = self.bot.get_channel(995062169894916177)
        birthdays = self.generate_birthday_list()
        if len(birthdays) > 0:
            print('We have some birthdays!', birthdays)
            for id in birthdays:
                birthday_boy = channel.guild.get_member(id).mention
                age = utils.parse_data(os.path.join(os.getcwd(), 'the_boys.json'), id, 'age')
                print('wouldve sent!')
                await channel.send(f"Happy Birthday {birthday_boy}!")
                await channel.send(f"Wow kiddo, already {age} years old.")

    def generate_birthday_list(self):
        user_list = utils.batch_user_list(os.path.join(os.getcwd(), 'the_boys.json'), 'discord_id', None)
        birthday_list = []
        for id in user_list:
            year = utils.parse_data(os.path.join(os.getcwd(), 'the_boys.json'), id, 'dob_year')
            month = utils.parse_data(os.path.join(os.getcwd(), 'the_boys.json'), id, 'dob_month')
            day = utils.parse_data(os.path.join(os.getcwd(), 'the_boys.json'), id, 'dob_day')
            today = datetime.datetime.now()
            if day == today.day and month == today.month:
                birthday_list.append(id)
                utils.replace_value(os.path.join(os.getcwd(), 'the_boys.json'), id, 'age', (today.year-year))

        return birthday_list

    @birthday_check.before_loop
    async def before_birthday_check(self):
        print('birthday check waiting...')
        await self.bot.wait_until_ready()

    @commands.command(name='birthday')
    async def birthday_test(self, ctx):
        await self.birthday_check()

async def setup(bot):
    await bot.add_cog(Birthday_Bot(bot))
