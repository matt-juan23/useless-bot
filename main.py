import os

import discord

TOKEN = os.environ['DISCORD_TOKEN']

client = discord.Client()

# random quote

# random quote from day

@client.event
async def on_ready():
    print(f"{client.user.name} connected to Discord")

@client.event
async def on_message(message):
    if message.author == client.user:
        # don't want to infinitely respond to self
        return

    if str(message.author) == "odell#7491":
        await message.channel.send("Shut up Odell")

    if str(message.author) == "zachyboiii#5666":
        await message.channel.send("Shut up Zach")
    
    if str(message.author) == "BKEmbers#0351":
        await message.channel.send("Ben Kwok: \"truth is I like semen in my ass\" - Monday 14 November")

client.run(TOKEN)