import random
import os
import discord
from discord.ext import commands

client = commands.Bot(command_prefix= '.')
token = '===== INSERT YOUR TOKEN HERE ====='

# cogs
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

# welcome message
@client.event
async def on_member_join(member):
    await ctx.send(f'{member} has walked into gacha hell. Welcome!')

# goodbye message
@client.event
async def on_member_remove(member):
    await ctx.send(f'{member} has left the gacha hell. Can we get an F?')

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

for filename in os.listdir('./cogs'):
    if(filename.endswith('.py')):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)