import discord
import sqlite3
import random
from discord.ext import commands

class Laksek(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command()
    async def callout(self, ctx, member : discord.Member):
        await ctx.send(f'{member.mention} is a laksek!')
    
    @commands.command(aliases=['ramalan', 'forecast'])
    async def gacha_forecast(self, ctx, member : discord.Member):
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
            "SSR in wrong server",
            "Gold lancer = Fionn",
            "Gold assassin = Stheno",
            "Just give up",
            "Credit card to the rescue!",
            "Single roll is the way",
            "Spook incoming"]
        await ctx.send(f'Forecast for: {member.mention}\nAnswer: {random.choice(responses)}')
    
    @commands.command()
    async def last_ssr(self, ctx):
        msg = "Last SSR(s): \n"
        db = sqlite3.connect('lastssr.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT * from lastssr")
        result = cursor.fetchall()

        for i in result:
            msg += "{}: {} \n".format(i[0], i[1])

        await ctx.send(f'{msg}')
       
        cursor.close()
        db.close()

def setup(client):
    client.add_cog(Laksek(client))