import os

import discord

TOKEN = os.environ['DISCORD_TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(f"{client.user.name} connected to Discord")

@client.event
async def on_message(message):
    if message.author == client.user:
        # don't want to infinitely respond to self
        return

    print(message.author)


client.run(TOKEN)