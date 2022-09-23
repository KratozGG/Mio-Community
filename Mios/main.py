import discord
import json
import pymongo
import keep_alive
import datetime 
import random
import asyncio
import praw
import aiohttp
import os
from random import randint
from discord.ext import commands
from discord.utils import get


keep_alive.keep_alive()

Bot = commands.Bot(command_prefix="mc!", case_insensitve=True)
Bot.remove_command('help')



@Bot.event
async def on_ready():
    await Bot.change_presence(activity=discord.Streaming(name='Minecraft', url='https://www.twitch.tv/zfrostt/'))
    print(f'Logged in as {Bot.user}')

@Bot.command(pass_context=True)
async def loadcog(ctx, cog):
    if ctx.author.id == 752403250975604756 or 703671503954378782 or 688293803613880334:
        Bot.load_extension(f"cogs.{cog}")
        await ctx.reply("Successfully loaded cog.")
    else:
        await ctx.reply("You can't use this command.")

@Bot.command(pass_context=True)
async def unloadcog(ctx, cog):
    if ctx.author.id == 752403250975604756 or 703671503954378782 or 688293803613880334:
        Bot.unload_extension(f"cogs.{cog}")
        await ctx.reply("Successfully unloaded cog.")
    else:
        await ctx.reply("Only developers of this bot can run this commmand.")

@Bot.command(pass_context=True)
async def reloadcog(ctx, cog):
    if ctx.author.id == 752403250975604756 or 703671503954378782 or 688293803613880334:
        Bot.unload_extension(f"cogs.{cog}")
        Bot.load_extension(f"cogs.{cog}")
        await ctx.reply("Successfully reloaded cog.")
    else:
        await ctx.reply("Only developers of this bot can run this command.")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        Bot.load_extension(f"cogs.{filename[:-3]}")

Bot.run("")
