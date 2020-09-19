import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix = '/')

@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} is connected')

@bot.command()
async def ping(ctx, *, text: str, text1: str):
    user = ctx.message.author
    await ctx.send(f'Pong {user.mention} {text} {text1}')

TOKEN = os.environ.get('TOKEN')


bot.run(TOKEN)