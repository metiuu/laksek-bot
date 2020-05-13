import discord
from discord.ext import commands

class Laksek(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Gudako on standby.')
    
    # Commands
    @commands.command()
    async def callout(self, ctx, member : discord.Member):
        await ctx.send(f'{member.mention} is a laksek!')

def setup(client):
    client.add_cog(Laksek(client))