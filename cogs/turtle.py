import discord
import turtle
import os
from discord.ext import commands

class turtle(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.counter = 0

    @commands.command()
    async def turtle(self, ctx, size, rotationr, rotationl, times):
        await ctx.send("Drawing... :turtle:")
        os.system('python ting.py '+ size + " " + rotationr + " "+ rotationl + " " + times)
        await ctx.send(file=discord.File('output.png'))
        await ctx.send("Done")
    
    @commands.command(name="tree")
    async def tree(self, ctx):
        await ctx.send("Drawing... :turtle:")
        os.system('python twee.py')
        await ctx.send(file=discord.File('output.png'))
        await ctx.send("Done")

            




def setup(bot):
    bot.add_cog(turtle(bot))