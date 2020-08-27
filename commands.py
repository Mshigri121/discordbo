import discord
from discord.ext import commands, tasks
from itertools import cycle

bot = commands.Bot(command_prefix="!")
#vc = guild.voice_channels
status = cycle(['in Hollywoo', 'Diane'])

@bot.command()
async def tt(ctx):
    await ctx.send("test")
@bot.command()
async def info(ctx):
    print(vc.name)
    print(vc.id)
    print(dis.user)

@bot.command(name="join")
async def join_voice(ctx):
    print("Joined")
    if ctx.message.author.voice:
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send('You must be in VC to invoke this command')

@bot.command(name="leave")
async def leave_voice(ctx):
    print("Leaving")
    if ctx.message.author.voice:
        server = ctx.message.guild.voice_client
        await server.disconnect()

bot.run('NzE5NzEwMTkyNzkwNDA1MTYw.Xt7Z1A.6NDlTdxaJ22GfxGHkfzERdkD7Ns')