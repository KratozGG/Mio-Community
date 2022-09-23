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






class pika(commands.Cog):
  def __init__(self, Bot):
    self.Bot = Bot

  @commands.command(pass_context=True, aliases = ["Pika", "p"])
  async def pikanetwork(self, ctx):
          pikaofc = discord.Embed(title="Pika-network Official Website", description="<----------------------->\n[Click here](https://pika-network.net/) to open the official website of PikaNetwork\n<----------------------->",color=0xccc411)
          pikaofc.timestamp = datetime.datetime.utcnow()
          pikaofc.set_footer(text="Mio's Community")
          await ctx.send(embed=pikaofc)

  @commands.command(pass_context=True, aliases = ["store", "pstr", "str"])
  async def pikastore(self, ctx):
          pikastoreemb = discord.Embed(title="Pika-network Official Store", description="<----------------------->\n[Click here](https://store.pika-network.net/) to open the official store of PikaNetwork\n<----------------------->",color=0xccc411)
          pikastoreemb.timestamp = datetime.datetime.utcnow()
          pikastoreemb.set_footer(text="Mio's Community")
          await ctx.send(embed=pikastoreemb)

  @commands.command(pass_context=True, aliases = ["vote", "pv", "v"])
  async def pikavote(self, ctx):
          pikavoteemb = discord.Embed(title="Pika-network Voting sites", description="<----------------------->\n[Click here](https://pika-network.net/vote/) to open the official voting site of PikaNetwork\n<----------------------->",color=0xccc411)
          pikavoteemb.timestamp = datetime.datetime.utcnow()
          pikavoteemb.set_footer(text="Mio's Community")
          await ctx.send(embed=pikavoteemb)

  @commands.command(pass_context=True, aliases = ["forums", "forum", "frm","pfrm"])
  async def pikaforums(self, ctx):
          pikaforumsemb = discord.Embed(title="Pika-network Official Forums", description="<----------------------->\n[Click here](https://pika-network.net/vote/) to open the official voting site of PikaNetwork\n<----------------------->",color=0xccc411)
          pikaforumsemb.timestamp = datetime.datetime.utcnow()
          pikaforumsemb.set_footer(text="Mio's Community")
          await ctx.send(embed=pikaforumsemb)

  @commands.command(pass_context=True, aliases = ["ps","suggestions", "psg"])
  async def pikasuggestion(self, ctx):
          pikasuggestemb = discord.Embed(title="Pika-network Official Suggestions", description="<----------------------->\n[Click here](https://pika-network.net/forums/suggestions/) to open the official Suggestions forum of PikaNetwork\n<----------------------->",color=0xccc411)
          pikasuggestemb.timestamp = datetime.datetime.utcnow()
          pikasuggestemb.set_footer(text="Mio's Community")
          await ctx.send(embed=pikasuggestemb)

  @commands.command(pass_context=True, aliases = ["psr"])
  async def pikareport(self, ctx):
          pikarepemb = discord.Embed(title="Pika-network", description="<----------------------->\n[Click here](https://pika-network.net/forums/player-reports.150/) to open the official Player Reports forum of PikaNetwork\n<----------------------->\n[click here](https://pika-network.net/forums/bug_reports/) to open the official bug reports forum of PikaNetwork\n<----------------------->",color=0xccc411)
          pikarepemb.timestamp = datetime.datetime.utcnow()
          pikarepemb.set_footer(text="Mio's Community")
          await ctx.send(embed=pikarepemb)

  @commands.command(pass_context=True, aliases = ["apply","papl","apl"])
  async def pikaapply(self, ctx):
          pikaapplyemb = discord.Embed(title="Pika-network", description="<----------------------->\n[Click here](https://pika-network.net/categories/applications.192/) to open the official Application forum of PikaNetwork\n<----------------------->",color=0xccc411)
          pikaapplyemb.timestamp = datetime.datetime.utcnow()
          pikaapplyemb.set_footer(text="Mio's Community")
          await ctx.send(embed=pikaapplyemb)

def setup(Bot):
  Bot.add_cog(pika(Bot))