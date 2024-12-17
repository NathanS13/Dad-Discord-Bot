# Reference: https://github.com/Rapptz/discord.py/blob/master/examples/basic_voice.py
import os
import shutil
import asyncio
import youtube_dl
from pytube import Playlist
import discord
import yt_dlp
import json

from discord.ext import commands, tasks


youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': False,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ydl_opts = {
    'format': 'm4a/bestaudio/best',
    # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'm4a',
    }]
}



class Music_Bot(commands.Cog):

    def __init__(self, bot):
        print('init music_bot')
        self.bot = bot
        self._playlist_play = []
        self._voice_channel = None
        self._ctx = None
        

    @commands.command(name='ping3')
    async def ping3(self, ctx):
        print('ping recieve')
        await ctx.send('pong')
        await ctx.send('mush id: ' + str(ctx.message.author.id))
        await ctx.send('server id: ' + str(ctx.guild.id))
        await ctx.send('channel id: ' + str(ctx.channel.id))

    @commands.command(name='join')
    async def join(self, ctx):
        print('join command')
        try:
            if not ctx.message.author.voice:
                await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
                return
            else:
                channel = ctx.message.author.voice.channel
            await channel.connect()
        except Exception as e:
            print(e)

    @commands.command(name='leave')
    async def leave(self, ctx):
        print('leave command')
        try:
            if not ctx.voice_client:
                await ctx.send("Not connected to a voice channel")
                return
            else:
                await ctx.send("Disconnecting..")
                await ctx.voice_client.disconnect()
        except Exception as e:
            print(e)

    @commands.command(name='play3')
    async def play3(self, ctx, url):
        """Plays a file from the local filesystem"""
        try :
            await self.join(ctx)
            server = ctx.message.guild
            voice_channel = server.voice_client
            if self._voice_channel is None:
                print('2222222222222222222 ', type(self._voice_channel), type(voice_channel))
                self._voice_channel = voice_channel # @TODO FIX THIS! trash code 
                self.play_music.start()
            if self._ctx is None:
                self._ctx = ctx
            #voice_channel = ctx.message.guild.voice_client
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                if not ydl._download_retcode:
                    #print(json.dumps(ydl.sanitize_info(info)))
                    _json_info = json.loads(json.dumps(ydl.sanitize_info(info)))
                    _json_info_debug = json.dumps(ydl.sanitize_info(info), indent=4)
                    with open('temp.json', 'w') as file:
                        file.write(_json_info_debug)

                    _file_path = []
                    _playlist = _json_info['entries'] if 'entries' in _json_info else None
                    if _playlist:
                        for song in _playlist:
                            async with ctx.typing():
                                await ctx.send('**Successfully Downloaded:** {}'.format(song['title']))
                        for song in _playlist:
                            _file_path.append(song['requested_downloads'][0]['filepath'])
                            print('DEBUG: ', _file_path)
                    else:
                        _file_path.append(_json_info['requested_downloads'][0]['filepath'])
                        print('DEBUG: ', _file_path)
                        async with ctx.typing():
                            await ctx.send('**Successfully Downloaded:** {}'.format(_json_info['title']))

                    for song in _file_path:
                        new_path = song.replace('Dad-Discord-Bot', 'music')
                        shutil.move(song, new_path)
                        print('moved ', song , ' to ', new_path)
                        self._playlist_play.append(new_path)

                    if len(self._playlist_play) > 0 and not self._voice_channel.is_playing():
                        print('???????????????')
                        await self.play_music()

        except Exception as e:
            print(e)
            await ctx.send("The bot is not connected to a voice channel.", e)

    @tasks.loop(seconds=10)
    async def play_music(self):
        if len(self._playlist_play) > 0 and not self._voice_channel.is_playing():
            await self.join(self._ctx)
            for song in self._playlist_play:
                self._voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg", source=song))
                async with self._ctx.typing():
                    await self._ctx.send('**Now playing:** {}'.format(song.split('/')[-1]))
                while self._voice_channel.is_playing():
                    await asyncio.sleep(1)

    @commands.command(name='list')
    async def list(self, ctx):
        if len(self._playlist_play) == 0:
            print('playlist is empty')
            await ctx.send('**Playlist is empty!**')
            return
        list_ret = '\n'.join([f"{i+1}. {path.split('/')[-1]}" for i, path in enumerate(self._playlist_play) while i < 5])
        print(list_ret)
        async with ctx.typing():
            await ctx.send('**Playlist:**')
            await ctx.send('{}'.format(list_ret))

    @commands.command(name='play2')
    async def play2(self, ctx, *, query):
        """Plays a file from the local filesystem"""

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(query))
        ctx.voice_client.play(source, after=lambda e: print(f'Player error: {e}') if e else None)

        await ctx.send(f'Now playing: {query}')

    @commands.command(name='play', help='To play song')
    async def play(self, ctx, url):
        try :
            server = ctx.message.guild
            voice_channel = server.voice_client
            #voice_channel = ctx.message.guild.voice_client
            if 'list' in url or 'index' in url:
                playlist = Playlist(url)
                print('Number Of Videos In playlist: ', len(playlist.video_urls))
                print(playlist)
            else:
                playlist = [url]
            for url in playlist:
                #urls.append(url)
                filename = await YTDLSource.from_url(url, loop=self.bot.loop)
                filename_moved = []
                for x, file_n in enumerate(filename):
                    filename_moved.append(shutil.move(file_n, os.path.join('/misc', 'music', file_n)))
                    print('New file path', filename_moved[x])
                    voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg", source=filename_moved[x]))
                    async with ctx.typing():
                        await ctx.send('**Now playing:** {}'.format(filename_moved[x].split('/')[-1]))
                    while voice_channel.is_playing():
                        await asyncio.sleep(1)
        except Exception as e:
            print(e)
            await ctx.send("The bot is not connected to a voice channel.", e)

    @commands.command(name='skip', help='To skip a song')
    async def skip(self, ctx):
        """skips the song playing"""
        server = ctx.message.guild
        voice_channel = server.voice_client
        voice_channel.stop()

    @commands.command(name='yt')
    async def yt(self, ctx, *, url):
        """Plays from a url (almost anything youtube_dl supports)"""

        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop)
            ctx.voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)

        await ctx.send(f'Now playing: {player.title}')

    @commands.command(name='stream')
    async def stream(self, ctx, *, url):
        """Streams from a url (same as yt, but doesn't predownload)"""

        #async with ctx.typing():
        #    player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
        #    print('player', player)
        #    ctx.voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)
#
        #await ctx.send(f'Now playing: {player.title}')

        try :
            server = ctx.message.guild
            voice_channel = server.voice_client
            #voice_channel = ctx.message.guild.voice_client

            async with ctx.typing():
                filename = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
                print('DEBUG', filename)
                for player in filename:
                    voice_channel.play(player, after=lambda e: print(f'Player error: {e}') if e else None)
                    await ctx.send('**Now playing:** {}'.format(player.title))
                    while voice_channel.is_playing():
                        await asyncio.sleep(1)
        except Exception as e:
            print(e)
            await ctx.send("The bot is not connected to a voice channel.", e)

    @commands.command(name='volume')
    async def volume(self, ctx, volume: int):
        """Changes the player's volume"""

        if ctx.voice_client is None:
            return await ctx.send("Not connected to a voice channel.")

        ctx.voice_client.source.volume = volume / 100
        await ctx.send(f"Changed volume to {volume}%")

    @commands.command(name='stop')
    async def stop(self, ctx):
        """Stops and disconnects the bot from voice"""

        await ctx.voice_client.disconnect()

    @play.before_invoke
    @yt.before_invoke
    @stream.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()

async def setup(bot):
    await bot.add_cog(Music_Bot(bot))
