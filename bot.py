import random
import os
import discord
from discord.ext import commands

client = commands.Bot(command_prefix= '.')

# cogs
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

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

# gacha forecast
@client.command(aliases=['ramalan', 'forecast'])
async def gacha_forecast(ctx, member : discord.Member):
    responses = ["Rate up is a lie.",
        "Ampas",
        "YOROKOBE",
        "SSR",
        "SR",
        "Waifu doesn't come home",
        "Luck E",
        "Prepare for salt",
        "Pouring salt for others",
        "SSR in spare account",
        "Just give up",
        "Credit card to the rescue!",
        "Single roll is the way",
        "Spook incoming"]
    await ctx.send(f'Forecast for: {member.mention}\nAnswer: {random.choice(responses)}')

for filename in os.listdir('./cogs'):
    if(filename.endswith('.py')):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('====== INSERT YOUR TOKEN HERE ======')