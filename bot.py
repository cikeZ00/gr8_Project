import discord, time, logging, json, os
from discord.ext import commands
from discord import Game, Embed, Color, Status, ChannelType
from random import randint, sample
from discord.ext.commands import cooldown
from os import path

#Logging
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='logs.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

#Loading config
if path.exists("config.json") == False:
    with open('config.json', 'w') as configout:
        json.dump({
        "token": "Token goes here",
        "prefix": "!"
         }, configout)
    print("[INFO] config.json generated!!")
    quit()
else:
    with open("config.json") as f:
        config = json.load(f)


#Cogs
initial_extensions = ['cogs.turtle']

#Init bot
bot = commands.Bot(command_prefix=config.get('prefix'), self_bot=False, case_insensitive=True, help_command=None)

#Load cogs
if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

#Cofnirm the bot is up
@bot.event
async def on_ready():
    print("Bot appears to have been started")
    await bot.change_presence(activity=discord.Game(name="Type !help", type=1))

#Error handling
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '[ERROR] This command is on a cooldown, please try again in {:.2f}s'.format(error.retry_after)
        user = ctx.message.author
        await user.send(msg)
        await ctx.message.add_reaction(emoji="❌")
    elif isinstance(error, commands.CheckFailure):
        msg = '[ERROR] You do not have the required permission to use this command!.'
        user = ctx.message.author
        await user.send(msg)
        await ctx.message.add_reaction(emoji="❌")
    elif isinstance(error, commands.CommandNotFound):
        msg = '[ERROR] This command does not exist!'
        user = ctx.message.author
        await user.send(msg)
        await ctx.message.add_reaction(emoji="❌")
    elif isinstance(error, commands.MissingRequiredArgument):
        msg = "[ERROR] Missing required argument(s)!"
        user = ctx.message.author
        await user.send(msg)
        await ctx.send("```"+str(error)+"```")
        await ctx.message.add_reaction(emoji="❌")

#Help commands
@bot.command()
async def help(ctx):
    user = ctx.message.author
    helpembed = discord.Embed(color=discord.Color.red())
    helpembed.set_author(name="Help (Base commands)")
    helpembed.add_field(name="!turtle", value="Usage: !turtle <size> <RRotation> <LRotation> <RepeatCount>",inline=False)
    helpembed.add_field(name="!tree", value="Draws a tree!",inline=False)
    helpembed.add_field(name="!bbdes", value="Draws a thing!",inline=False)
    helpembed.add_field(name="!help", value="Shows this message :rofl:",inline=False)
    await user.send(embed=helpembed)
    await ctx.message.add_reaction(emoji="✅")


# Authentication
if config.get('token') == "Token goes here":
    print("[ERROR] No token present!")
elif config.get('token') == "":
    print("[ERROR] No token present!")
else:
    print("[INFO] Starting up and logging in...")
    bot.run(config.get('token'), bot=True, reconnect=True)