import discord
from discord.ext import commands

import os
from dotenv import load_dotenv
load_dotenv()

client = commands.Bot(command_prefix="$")

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases= ["hi"])
async def hi(ctx): 
    await ctx.send(f'Hi')

client.run(os.getenv('TOKEN'))
