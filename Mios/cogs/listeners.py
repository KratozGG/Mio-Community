import discord
import json
import pymongo
import keep_alive
import datetime 
import random
import asyncio
import praw
import aiohttp
from random import randint
from discord.ext import commands
from discord.utils import get




class listeners(commands.Cog):
  def __init__(self, Bot):
    self.Bot = Bot
  @commands.Cog.listener()
  async def on_message(self, message):
      channel = self.Bot.get_channel(934425632547405904)
      embed = discord.Embed(title="Word Hunt", description = f"{message.author.mention} has found the word. It was `suggestions`", color=discord.Colour.random())
    
      if message.content.startswith('suggestions'):
        await channel.send(embed=embed)


  @commands.command(pass_context=True)
  @commands.has_permissions(administrator=True)
  async def clue(self, ctx, *, clue: str):

    channel = self.Bot.get_channel(934425632547405904)
    embed = discord.Embed(title="Clue", description=f"{clue}", color=discord.Colour.random())

    await channel.send(embed=embed)

  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    erroremb = discord.Embed(
    title='',
    color=discord.Colour.random())
    if isinstance(error, commands.CommandNotFound):
      pass
    if isinstance(error, commands.MissingPermissions):
      erroremb.add_field(name=f'Invalid Permissions', value=f'You do not have the permissions to issue this command.')
      await ctx.send(embed=erroremb)
    else:
      erroremb.add_field(name=f':x: Terminal Error',value=f"{error}")
      await ctx.send(embed=erroremb)
      raise error

def setup(Bot):
    Bot.add_cog(listeners(Bot))
  