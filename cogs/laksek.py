import discord
from discord.ext import commands

class Laksek(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        await client.change_presence(status=discord.Status.online, activity=discord.Game('Fate/Grand Order'))
        print('Gudako on standby.')
    
    # Commands
    @commands.command()
    async def callout(self, ctx, member : discord.Member):
        await ctx.send(f'{member.mention} is a laksek!')
    
    @commands.command(aliases=['ramalan', 'forecast'])
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

def setup(client):
    client.add_cog(Laksek(client))