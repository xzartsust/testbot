import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix = '/')

words = ['bb', 'пока', 'пп']

@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} is connected')

@bot.command()
async def ping(ctx, *, text: str):
    user = ctx.message.author
    await ctx.send(f'Pong {user.mention} {text}')

@bot.event
async def on_message(message):

    await bot.process_commands(message)
    user = ctx.message.author
    if message in words:
        await ctx.send(f'Hello {user.mention}')

TOKEN = os.environ.get('TOKEN')

bot.run(TOKEN)