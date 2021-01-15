import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print("Bot is Ready")

client.run('Enter Your Token Here')
