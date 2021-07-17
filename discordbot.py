# Imports
import discord
from discord.ext import commands
import os

# Credentials
TOKEN = os.environ['DISCORDTOKEN']

# Create bot
client = commands.Bot(command_prefix='!')

# Startup Information
@client.event
async def on_ready():
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

# Command
@client.command(brief='Creates an alternating upper/lower case version of your message', description='cReAtEs An AlTeRnAtInG uPpEr/LoWeR cAsE vErSiOn Of YoUr MeSsAgE')
async def altcaps(ctx):
    content = ctx.message.content.split(None, 1)[1]
    res = ""
    lower = True
    for c in content:
        newc = c
        if c.isalpha():
            if lower:
                newc = c.lower()
            else:
                newc = c.upper()
            lower = not lower
        res += newc
    await ctx.send(content=res)

client.run(TOKEN)