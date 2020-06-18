import os
import sqlite3
import discord
from discord.ext import commands, tasks

client = commands.Bot(command_prefix= '.')
token = 'YOUR TOKEN HERE'

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

# initialize bot
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Fate/Grand Order'))
    
    print('Gudako on standby.')

# welcome message
@client.event
async def on_member_join(ctx, member):
    await ctx.send(f'{member} has walked into gacha hell. Welcome!')

# goodbye message
@client.event
async def on_member_remove(ctx, member):
    await ctx.send(f'{member} has left the gacha hell. Can we get an F?')

#clear messages 
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

for filename in os.listdir('./cogs'):
    if(filename.endswith('.py')):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)