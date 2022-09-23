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
import json_files
import os



class help(commands.Cog):
  def __init__(self, Bot):
    self.Bot = Bot
    
  @commands.command()
  async def help(self, ctx):
    with open("json_files/help.json") as f:
      data = json.load(f)
    helpemb = discord.Embed(title="Mio's community | Help Panel", description="List of all available commands!", color=discord.Colour.random())
    helpemb.set_footer(text=f"Issued by {ctx.author.name}", 
    icon_url=ctx.author.avatar_url)
    helpemb.set_image(url="https://cdn.discordapp.com/attachments/929767375488819215/936314289860509706/mioh.gif")
    data = json.load(open("json_files/help.json"))
    for key, value in data.items():
      helpemb.add_field(name=key, value=value, inline=False)
    await ctx.reply(embed=helpemb)

  @commands.command()
  async def pikahelp(self, ctx):
    with open("json_files/pika.json") as f:
      data = json.load(f)
    pikahemb = discord.Embed(title="Mio's community | PikaNetwork Help Panel", description="List of all PikaNetwork commands!", color=discord.Colour.random())
    pikahemb.set_footer(text=f"Issued by {ctx.author.name}", icon_url=ctx.author.avatar_url)
    pikahemb.set_image(url="https://cdn.discordapp.com/attachments/930858260959998073/937013364691972197/help_panel_mioh.gif")
    data = json.load(open("json_files/pika.json"))
    for key, value in data.items():
      pikahemb.add_field(name=key, value=value, inline=False)
    await ctx.reply(embed=pikahemb)

  @commands.command()
  async def serverhelp(self, ctx):
    with open("json_files/server.json") as f:
      data = json.load(f)
    serveremb = discord.Embed(title="Mio's community | Server Help Panel", description="List of all Server commands!", color=discord.Colour.random())
    serveremb.set_footer(text=f"Issued by {ctx.author.name}", icon_url=ctx.author.avatar_url)
    serveremb.set_image(url="https://cdn.discordapp.com/attachments/930858260959998073/937013364691972197/help_panel_mioh.gif")
    data = json.load(open("json_files/server.json"))
    for key, value in data.items():
      serveremb.add_field(name=key, value=value, inline=False)
    await ctx.reply(embed=serveremb)

  @commands.command()
  async def funhelp(self, ctx):
    with open("json_files/fun.json") as f:
      data = json.load(f)
    funemb = discord.Embed(title="Mio's community | Fun Help Panel", description="List of all Server commands!", color=discord.Colour.random())
    funemb.set_footer(text=f"Issued by {ctx.author.name}", icon_url=ctx.author.avatar_url)
    funemb.set_image(url="https://cdn.discordapp.com/attachments/930858260959998073/937013364691972197/help_panel_mioh.gif")
    data = json.load(open("json_files/fun.json"))
    for key, value in data.items():
      funemb.add_field(name=key, value=value, inline=False)
    await ctx.reply(embed=funemb)

  @commands.command()
  @commands.has_role(932275893194326016)
  async def staffhelp(self, ctx):
    with open("json_files/staff.json") as f:
      data = json.load(f)
    staffemb = discord.Embed(title="Mio's community | Staff Help Panel", description="List of all available commands!", color=discord.Colour.random())   
    staffemb.set_footer(text=f"Issued by {ctx.author.name}", 
    icon_url=ctx.author.avatar_url)
    staffemb.set_image(url="https://cdn.discordapp.com/attachments/930858260959998073/937013364691972197/help_panel_mioh.gif")
    data = json.load(open("json_files/staff.json"))
    for key, value in data.items():
      staffemb.add_field(name=key, value=value, inline=False)
    await ctx.reply(embed=staffemb)

  @commands.command()
  async def musichelp(self, ctx):
    with open("json_files/moosic.json") as f:
      data = json.load(f)
    memb = discord.Embed(title="Mio's community | Music Help Panel", description="List of all available commands!", color=discord.Colour.random())
    memb.set_footer(text=f"Issued by {ctx.author.name}", 
    icon_url=ctx.author.avatar_url)
    memb.set_image(url="https://cdn.discordapp.com/attachments/930858260959998073/937013364691972197/help_panel_mioh.gif")
    data = json.load(open("json_files/moosic.json"))
    for key, value in data.items():
      memb.add_field(name=key, value=value, inline=False)
    await ctx.reply(embed=memb)

def setup(Bot):
    Bot.add_cog(help(Bot))
  