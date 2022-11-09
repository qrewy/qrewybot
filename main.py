import discord
import json
from discord.ext import commands

file = open('config.json', 'r')
config = json.load(file)

bot = commands.Bot(config['prefix'])
@bot.command(name='ping')
async def ping(ctx):
    await ctx.send(f'{ctx.author.mention} pong!')


bot.run(config['token'])
