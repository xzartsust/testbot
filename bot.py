import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix = '/')

hello_words = ['Hi', 'hello', 'Привіт']

@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} is connected')
    await bot.change_presence(status = discord.Status.idle, activity = discord.Game(name = 'Hello'))

@bot.event
async def on_message(message):
    
    await bot.process_commands(message)

    msg = message.content
    user = message.author

    if msg in hello_words:
        await message.channel.send(f'Hi {user.mention}')

@bot.command()
@commands.cooldown(1, 15, commands.BucketType.member)
async def ping(ctx, *, text: str):
    user = ctx.message.author
    await ctx.send(f'Pong {user.mention} {text}')

TOKEN = os.environ.get('TOKEN')

bot.run(TOKEN)