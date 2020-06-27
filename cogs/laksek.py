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

        # initialize list of possible responses
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
        
        # mention member and select random value from list
        await ctx.send(f'Forecast for: {member.mention}\nAnswer: {random.choice(responses)}')
    
    @commands.command(aliases=['lastssr'])
    async def last_ssr(self, ctx):
        msg = "Last SSR(s): \n"

        # connect to db and initialize cursor
        db = sqlite3.connect('lastssr.sqlite')
        cursor = db.cursor()

        # execute query and fetch all result
        cursor.execute("SELECT * from lastssr")
        result = cursor.fetchall()

        # append message
        for i in result:
            msg += "{}: {} \n".format(i[0], i[1])

        await ctx.send(f'{msg}')

       # close connection
        cursor.close()
        db.close()
    
    @commands.command(aliases=['updatessr'])
    async def update_ssr(self, ctx, arg1, arg2):
        # connect to db and initialize cursor
        db = sqlite3.connect('lastssr.sqlite')
        cursor = db.cursor()

        # execute queries
        cursor.execute('''DELETE FROM lastssr WHERE name = "{}"'''.format(arg1))
        cursor.execute('''INSERT INTO lastssr (name, servant) VALUES ("{}", "{}")'''.format(arg1,arg2))

        await ctx.send("Database has been updated.")
       
       # save changes and close connection
        db.commit()
        cursor.close()
        db.close()

    @commands.command(aliases=['newssr'])
    async def new_ssr(self, ctx, arg1, arg2):
        # connect to db and initialize cursor
        db = sqlite3.connect('lastssr.sqlite')
        cursor = db.cursor()

        # execute query
        cursor.execute('''INSERT INTO lastssr (name, servant) VALUES ("{}", "{}")'''.format(arg1,arg2))

        await ctx.send("New data has been inserted into database.")
       
       # save changes and close connection
        db.commit()
        cursor.close()
        db.close()

    @commands.command()
    async def calculate_luck(self, ctx, arg1, arg2):
        # total login days = arg1, ssr count (including NP) = arg2
        luck = int(arg1) // int(arg2)

        # calculate luck rank
        if(luck == 1):
            rank = "God"
        if(luck >= 10):
            rank = "Saint"
        if(luck >= 20):
            rank = "EX"
        if(luck >= 30):
            rank = "A"
        if(luck >= 40):
            rank = "B"
        if(luck >= 50):
            rank = "C"
        if(luck >= 100):
            rank = "E"
        if(luck >= 200):
            rank = "-"
        
        # send message with calculated rank, mentioning sender
        await ctx.send(f'Luck rank = {arg1}/{arg2}\n{ctx.message.author.mention}\'s luck rank is: {rank}')  

def setup(client):
    client.add_cog(Laksek(client))