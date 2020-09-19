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
    msg = message.content.lower()
    user = message.author
    if msg in words:
        await message.send(f'Hello {user.mention}')

TOKEN = os.environ.get('TOKEN')

bot.run(TOKEN)