import discord
import time
from discord.ext import tasks
from itertools import cycle
import asyncio

client = discord.Client()
voicech = discord.voice_client
status = cycle(['in Hollywoo', 'with Joey Pogo', 'Birthday Dad', 'WhatTimeIsItRightNow'])

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    statuschange.start()

@tasks.loop(seconds=30)
async def statuschange():
    await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_message(message):
    message.content.lower()
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('I hope your not talking to me?')
        print("Philbert has responded to the chat")
        time.sleep(10)
        if str(message.author) == "DISCORD ID # DISCORD ID NUMBER":
            await message.channel.send('Why did you bring me into this world.')
            print("Philbert has responded to creator")
    # elif message.content.startswith('connect'):
    #     print("Connect command intialized")
    #     await channel.connect(reconnect = False)
    #     print("Philbert has joined voice chat")
    elif message.content.startswith('hey'):
        await message.channel.send('Why')
        print("Philbert has responded to alt")



client.run('INSERT TOKEN HERE')
