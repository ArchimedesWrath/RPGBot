import os
import sys

import discord
from discord.ext import commands

import player
import event

# MYPLAYER = player.stats
PLAYERS = {}

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

"""
----------------------Helper Commands-------------------------------------------------------
"""

@bot.command(name='channels')
async def channels(ctx):
    for channel in ctx.bot.get_all_channels():
        print(channel.id)

@bot.command(name='members')
async def members(ctx):
    for member in ctx.channel.members:
        if not member.bot:
            PLAYERS[member.name] = player.stats # TODO: Make it so this retrieves from DB
            print(f'Added {member.name} to PLAYERS dict.')

@bot.command(name='stop')
async def stop(ctx):
    if ctx.message.author.name == 'TectonicFlow':
        print('Logging out...')
        await ctx.send('Goodbye!')
        await bot.logout()
    else:
        print(f'{ctx.message.author.name} attempted to stop the bot.')
        await ctx.send(f'You do not have privs to run that command, {ctx.message.author.name}!')

@bot.command(name='deleteAllMessages')
async def deleteAllMessages(ctx):
    if ctx.message.author.name == 'TectonicFlow':
        print('Deleting all messages...')
        async for message in ctx.message.channel.history(limit=200):
            await message.delete()
    else:
        print(f'{ctx.message.author.name} attempted to delete all messages.')
        await ctx.send(f'You do not have privs to run that command, {ctx.message.author.name}!')

@bot.command(name='deleteCommandMessages')
async def deleteCommandMessages(ctx):
    if ctx.message.author.name == 'TectonicFlow':
        print('Deleting command messages...')
        async for message in ctx.message.channel.history(limit=200):
            if message.content.startswith('!'):
                await message.delete()
    else:
        print(f'{ctx.message.author.name} attempted to delete command messages.')
        await ctx.send(f'You do not have privs to run that command, {ctx.message.author.name}!')

@bot.command(name='deleteBotMessages')
async def deleteBotMessages(ctx):
    if ctx.message.author.name == 'TectonicFlow':
        print('Deleting bot messages...')
        async for message in ctx.message.channel.history(limit=200):
            if message.author.bot:
                await message.delete()
    else:
        print(f'{ctx.message.author.name} attempted to delete bot messages.')
        await ctx.send(f'You do not have privs to run that command, {ctx.message.author.name}!')

"""
----------------------Player Commands-------------------------------------------------------
"""
@bot.command(name='random')
async def random(ctx):
    print(f'You rolled a: {event.randomRoll(1, 100)}')

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
    MYPLAYER = PLAYERS[ctx.message.author.name]
    embed = discord.Embed(
        description ='Level : ' + str(MYPLAYER['level'])
                 + '\nExp : ' + str(MYPLAYER['exp']) + '/' + str(MYPLAYER['expNext'])
                 + '\nHealth : ' + str(MYPLAYER['health']) + '/' + str(MYPLAYER['maxHealth'])
                 + '\nAttack : ' + str(MYPLAYER['attack'])
                 + '\nDefense : ' + str(MYPLAYER['defense'])
                 + '\nWisdom : ' + str(MYPLAYER['wisdom'])
                 + '\nSpeed : ' + str(MYPLAYER['speed']),
        colour = discord.Color.blue()
    )
    embed.set_author(name=ctx.message.author.name)
    await ctx.send(embed=embed)

@bot.command()
async def addExp(ctx, increase: int):
    name = ctx.message.author.name
    if str(ctx.message.channel.type) != 'text':
        return
    if ctx.message.channel.name != 'general':
        return
    level = PLAYERS[name]['level']
    PLAYERS[name] = player.addExp(PLAYERS[name], increase)
    print(f"{str(increase)} exp has been awarded to {name}")
    if PLAYERS[name]['level'] > level:
        await ctx.send(f'Congrats, {name}, you are now level ' + str(PLAYERS[name]['level']) + '!')

"""
Client Events / Commands
"""
bot.run(TOKEN)

