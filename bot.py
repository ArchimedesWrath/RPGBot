import os
import sys

import discord
from discord.ext import commands

# This works!
import player

MYPLAYER = player.stats

TOKEN = ''

client = discord.Client()

"""
Bot Events / Commands
"""

bot = commands.Bot(command_prefix='!')

# Events
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    await bot.get_channel(714555675769831557).send('Hello! I am now connected...')

# Helper Commands
@bot.command(name='channels')
async def channels(ctx):
    for channel in ctx.bot.get_all_channels():
        print(channel.id)

@bot.command(name='stop')
async def stop(ctx):
    print('Logging out...')
    await ctx.send('Goodbye!')
    await bot.logout()

@bot.command(name='delete')
async def delete(ctx):
    print('Deleting messages...')
    async for message in ctx.message.channel.history(limit=200):
        await message.delete()

#Commands

@bot.command()
async def echo(ctx, *, msg):
    if str(ctx.message.channel.type) != 'text':
        return
    if ctx.message.channel.name != 'general':
        return
    await ctx.send(msg)

#Game Commands
@bot.command(name='stats')
async def stats(ctx):
    embed = discord.Embed(
        description = 'This is where the stats go',
        colour = discord.Color.blue()
    )
    embed.set_author(name=ctx.message.author.name)
    await ctx.send(embed=embed)

@bot.command()
async def addExp(ctx, increase: int):
    if str(ctx.message.channel.type) != 'text':
        return
    if ctx.message.channel.name != 'general':
        return
    global MYPLAYER
    MYPLAYER = player.addExp(MYPLAYER, increase)
    await ctx.send('Player level is now: ' + str(MYPLAYER['level']) + ' Player exp is now: ' + str(MYPLAYER['exp']))


"""
Client Events / Commands
"""
bot.run(TOKEN)

