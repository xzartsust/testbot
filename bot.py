import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix = '/')

hello_words = ['Hi', 'Hello', 'Привіт']


@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} is connected')

@bot.event
async def on_message(message):
    await bot.process_commands(message)

    user = ctx.message.author

    msg = message.content.lower()

    if mgs in hello_words:
        await ctx.send(f'Привіт {user.mention}')
    


@bot.command()
async def ping(ctx, *, text: str):
    user = ctx.message.author
    await ctx.send(f'Pong {user.mention} {text}')

TOKEN = os.environ.get('TOKEN')

bot.run(TOKEN)