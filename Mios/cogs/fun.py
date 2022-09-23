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

class fun(commands.Cog):
  def __init__(self, Bot):
    self.Bot = Bot

  @commands.command()
  async def howpro(self, ctx):
    proemb = discord.Embed(title="**Proffesionalism rating Machine**", description=f"{ctx.author.mention} OMG you are {randint(1, 100)}% a Pro, Get em!!!", color=discord.Colour.random())
    proemb.timestamp = datetime.datetime.utcnow()
    proemb.set_footer(text=f"Proffesionalism of {ctx.author.name}!!", icon_url=f'{ctx.author.avatar_url}')
    await ctx.reply(embed=proemb)
  
  @commands.command()
  async def hownoob(self, ctx):
    noobemb = discord.Embed(title="**Noobness rating Machine**", description=f"{ctx.author.mention} LOL you are {randint(1, 100)}% a Noob, Get better!", color=discord.Colour.random())
    noobemb.timestamp = datetime.datetime.utcnow()
    noobemb.set_footer(text=f"Noobness of {ctx.author.name}!!", icon_url=f'{ctx.author.avatar_url}')
    await ctx.reply(embed=noobemb)

  @commands.command()
  async def howgay(self, ctx):
    gayemb = discord.Embed(title="**Gayness rating Machine**", description=f"{ctx.author.mention} You are {randint(1, 100)}% Gay, That's SuS dude.", color=discord.Colour.random())
    gayemb.timestamp = datetime.datetime.utcnow()
    gayemb.set_footer(text=f"Gayness of {ctx.author.name}!!", icon_url=f'{ctx.author.avatar_url}')
    await ctx.reply(embed=gayemb)


  @commands.command()
  async def howcute(self, ctx):
    cutemb = discord.Embed(title="**Cuteness rating Machine**", description=f"{ctx.author.mention} You are {randint(1, 100)}% Cute, sheesh!!!", color=discord.Colour.random())
    cutemb.timestamp = datetime.datetime.utcnow()
    cutemb.set_footer(text=f"Cuteness of {ctx.author.name}!!", icon_url=f'{ctx.author.avatar_url}')
    await ctx.reply(embed=cutemb)

  @commands.command(aliases=["av"])
  async def avatar(self, ctx, member:discord.User = None):
    if member is None:
      member = ctx.author
    

    avemb = discord.Embed(title=f"Avatar of {member.name}", description = "Yoo your avatar is cool :D", color=discord.Colour.random())
    avemb.set_image(url=member.avatar_url)
    avemb.set_footer(text=f"Issued by {ctx.author}")
    await ctx.send(embed=avemb)

  @commands.command(pass_context=True)
  async def roll(self, ctx, num=None):
    if num is None:
      num = 100

    rollemb = discord.Embed(title="roll", description = f"{ctx.author.name} has rolled {random.randint(1, int(num))}", color = discord.Colour.random())
    await ctx.send(embed=rollemb)

  @commands.command(pass_context=True)
  async def choose(self, ctx, object2: str, object1: str):
    if object1 is None:
      await ctx.send("Enter a valid first object")
    else:
      pass

    ok = []
    ok.append(object1)
    ok.append(object2)

    content = random.choice(ok)

    chemb = discord.Embed(title="Choose", description = f"I have chosen {content}!")

    await ctx.send(embed=chemb)
  @commands.command(pass_context=True)
  @commands.has_role(933375388405628938)
  async def facereveal(self, ctx):

    embed = discord.Embed(title = "Kratoz Face Reveal", color=discord.Colour.random())
    embed.set_image(url="https://media.discordapp.net/attachments/927205293388087348/934390607810560061/9k.png")

    await ctx.send(embed=embed)

  @commands.command(aliases=["cf"])
  async def coinflip(self, ctx, choice:str):

    if choice is None:
      await ctx.send("Provide a valid choice of either `Head` or `Tail`")

    list1 = ['head', 'tail']

    c_choice = random.choice(list1)

    if choice == c_choice:
      embed7 = discord.Embed(title= "", description = f"You chose {choice} and I chose {c_choice}. You won!", color = discord.Colour.random())

      embed7.set_author(name = "Coin Flip!")
      embed7.set_thumbnail(url="https://cdn.discordapp.com/attachments/934777769861206016/937607366617215016/goldcoin1.png")
      await ctx.send(embed=embed7)

    elif choice != c_choice:
      embed8 = discord.Embed(title= "", description = f"You chose {choice} and I chose {c_choice}. You lost!", color = discord.Colour.random())

      embed8.set_author(name = "Coin Flip!")
      embed8.set_thumbnail(url="https://cdn.discordapp.com/attachments/934777769861206016/937607366617215016/goldcoin1.png")

      await ctx.send(embed=embed8)

    else:
      pass

def setup(Bot):
    Bot.add_cog(fun(Bot))
