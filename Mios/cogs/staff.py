import discord
import json
import datetime 
import random
import asyncio
import praw
import aiohttp

from random import randint
from discord.ext import commands
from discord.utils import get

class staff(commands.Cog):

  def __init__(self, Bot):
    self.Bot = Bot


  
  @commands.command()
  @commands.has_permissions(administrator = True)
  async def accept(self, ctx, msg_id: int = None):
      if not msg_id:
          channel = self.Bot.get_channel(112233445566778899) 
          msg_id = 998877665544332211 
  
      channel = self.Bot.get_channel(933574171705876490)
      msg = await channel.fetch_message(msg_id)
      await msg.edit(content=f"Suggestion Accepted : Accepted and Implemented")

  @commands.command()
  @commands.has_permissions(administrator = True)
  async def deny(self, ctx, msg_id: int = None, *, reason):
      if not msg_id:
          channel = self.Bot.get_channel(112233445566778899) 
          msg_id = 998877665544332211 
  
      channel = self.Bot.get_channel(933574171705876490)
      msg = await channel.fetch_message(msg_id)
      await msg.edit(content=f"Suggestion Denied : {reason}")

  @commands.command()
  @commands.has_permissions(administrator = True)
  async def announce(self,ctx, *,title):

    anemb1 = discord.Embed(
      title="Announcement",
      description="Send the content of the announcement you want to send\n=>This operation will timeout in one minute",
      color=discord.Colour.random())

    anclogemb = discord.Embed(title="Announcement command Usage", description = f"{ctx.author} has used the announcement command in {ctx.channel}", color=0x0600ff)

    anchannel= self.Bot.get_channel(930431259077922836)
    anclogchannel = self.Bot.get_channel(933595881456951337)
    sent = await ctx.send(embed=anemb1)

    try:
      msg = await self.Bot.wait_for(  
        "message",
        timeout=60,
        check=lambda message: message.author == ctx.author
                            and message.channel == ctx.channel
      )
      if msg:
        await sent.delete()
        await msg.delete()
        ancemb2 = discord.Embed(
          title=f"{title}",
          description=f"{msg.content}",
          color=0x030303
        )
        ancemb2.set_footer(text="Mio's Community")
        await anchannel.send(embed=ancemb2)
        await anclogchannel.send(embed=anclogemb)


    except asyncio.TimeoutError:
      await sent.delete()
      await ctx.send("Cancelling the process due to the Timeout")


  def convert(time):
    pos = ["s","m","h","d"]

    time_dict = {"s" : 1, "m" : 60, "h" : 3600, "d" : 3600*24}

    unit = time[-1]

    if unit not in pos:
      return -1
    try:
      val = int(time[:-1])
    except:
      return -2

    return val * time_dict[unit]


  @commands.command()
  @commands.has_permissions(administrator = True)
  async def gstart(self, ctx):

    def convert(time):
      pos = ["s","m","h","d"]

      time_dict = {"s" : 1, "m" : 60, "h" : 3600, "d" : 3600*24}

      unit = time[-1]

      if unit not in pos:
        return -1
      try:
        val = int(time[:-1])
      except:
        return -2

      return val * time_dict[unit]

    await ctx.send("Starting the giveaway, answer these questions within the next 15 seconds")

    questions = ["Which channel do you want it to be hosted in?","Enter the duration of the giveaway in (s|m|h|d)","What is the prize of the Giveaway?"]

    answers = []

    def check(m):
      return m.author == ctx.author and m.channel == ctx.channel

    for i in questions:
      await ctx.send(i)

      try:
        msg = await self.Bot.wait_for('message', timeout=15.0, check=check)
      except asyncio.TimeoutError:
        await ctx.send('You didn\'t answer in time, please be quick the next time')
        return
      else:
        answers.append(msg.content)

    try:
      c_id = int(answers[0][2:-1])
    except:
      await ctx.send("You didn't mention a channel properly.")
      return

    channel = self.Bot.get_channel(c_id)
    role_id = 930426267155705857
    role = get(ctx.guild.roles, id=role_id)

    time = convert(answers[1])
    if time == -1:
      await ctx.send("You didn't enter a valid time duration")
      return
    elif time == -2:  
      await ctx.send("The time must be an Integer")
      return
    prize = answers[2]

    await ctx.send(f"The Giveaway will be hosted in {channel.mention} and will last for {answers[1]}")

    gaemb = discord.Embed(title="Giveaway",description = f"{prize}",color=0x00ffff)
    gaemb.add_field(name = "Hosted by:", value = ctx.author.mention)
    gaemb.set_footer(text = f"Ends {answers[1]} from now")

    my_msg = await channel.send(embed = gaemb)

    await my_msg.add_reaction("🎉")
    await channel.send(f"role mention placeholder")

    await asyncio.sleep(time)

    new_msg = await channel.fetch_message(my_msg.id)

    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(ctx.guild.me))

    winner = random.choice(users)
    await channel.send(f"Congratulations! {winner.mention} won {prize}")

  @commands.command()
  @commands.has_permissions(administrator = True)
  async def reroll(self, ctx, channel: discord.TextChannel, id_ : int):
  
      try:
        new_msg = await channel.fetch_message(id_)
      except:
        await ctx.send("The id entered was incorrect")
        return

      users = await new_msg.reactions[0].users().flatten()
      users.pop(users.index(ctx.guild.me))

      winner = random.choice(users)

      await channel.send(f"Congratulations! The new winner is {winner.mention}")

  @commands.command()
  @commands.has_permissions(administrator = True)
  async def purge(self, ctx, lm: int):
      await ctx.channel.purge(limit=lm + 1)


  @commands.command(pass_context=True)
  @commands.has_permissions(administrator = True)
  async def polladd(self, ctx, object1, object2, rs : int = None):

    r1 = '🍕'
    r2 = '🍔'
  
    poll_channel = self.Bot.get_channel(929767375232991243)
    pollemb = discord.Embed(title="Poll", color=discord.Colour.random())
    pollemb.add_field(name = f"react with {r1}", value=f"{object1}", inline=True)
    pollemb.add_field(name = f"react with {r2}", value=f"{object2}", inline=True)
    pollemb.set_footer(text=f"Poll by {ctx.author.name}")

    poll_message = await poll_channel.send(embed=pollemb)
    await poll_message.add_reaction('🍕')
    await poll_message.add_reaction('🍔')
  
    nrm1 = get(poll_message.reactions, emoji=f'{r1}')
    nrm2 = get(poll_message.reactions, emoji=f'{r2}')
  
    if nrm1 == rs:
      await poll_message.reply(f"GGs, {object1} has won the Poll")
    elif nrm2 == rs:
      await poll_message.reply(f"GGs, {object2} has won the Poll")
    else:
      pass

  @commands.command()
  @commands.has_permissions(administrator = True)
  async def ebuild(self, ctx, *, title: str):
    await ctx.send("Starting the process, answer these questions within the next 1 minute")

    questions = ["Which channel do you want it to be sent in?","Enter the content of the Embed","Confirm posting it?"]

    answers = []

    def check(m):
      return m.author == ctx.author and m.channel == ctx.channel

    for i in questions:
      await ctx.send(i)

      try:  
        msg = await self.Bot.wait_for('message', timeout=60, check=check)
      except asyncio.TimeoutError:
        await ctx.send('You didn\'t answer in time, please be quick the next time')
        return
      else:
        answers.append(msg.content)

    try:
      c_id = int(answers[0][2:-1])
    except:
      await ctx.send("You didn't mention a channel properly.")
      return

    channel = self.Bot.get_channel(c_id)
    content = answers[1]


  

    emb = discord.Embed(title=f"{title}",description = f"{content}",color=0x00ffff)
    emb.set_footer(text = f"Mio's Community")
    emb.set_image(url = "https://media.discordapp.net/attachments/929767377086849092/943064573718691841/unknown.png")

    await channel.send(embed = emb)
    await ctx.channel.purge(limit=9)
    await ctx.send(f"The embed will be sent in {answers[0]}")


  @commands.command()
  @commands.has_role(933375388405628938)
  async def bupdate(self, ctx, *,title):

    bupemb = discord.Embed(
      title="Bot update",
      description="Send the content of the bot update you want to send\n=>This operation will timeout in one minute",
      color=0x0600ff)

    buplogemb = discord.Embed(title="BotUpdate command Usage", description = f"{ctx.author} has used the BotUpdate command in {ctx.channel}", color=0x0600ff)

    bupchannel= self.Bot.get_channel(id=933610329638854688)
    buplogchannel = self.Bot.get_channel(id=933595881456951337)
    sent = await ctx.send(embed=bupemb)

    try:
      msg = await self.Bot.wait_for(  
        "message",
        timeout=60,
        check=lambda message: message.author == ctx.author
                            and message.channel == ctx.channel
      )
      if msg:
        await sent.delete()
        await msg.delete()
        bupemb2 = discord.Embed(
          title=f"{title}",
          description=f"{msg.content}",
          color=0x0600ff
        )
        bupemb2.set_footer(text="Mio's Community")
        await bupchannel.send(embed=bupemb2)
        await buplogchannel.send(embed=buplogemb)


    except asyncio.TimeoutError:
      await sent.delete()
      await ctx.send("Cancelling the process due to the Timeout")

  @commands.command()
  async def kratoz(self, ctx):
    await ctx.reply("kratoz gae sus")


def setup(Bot):
    Bot.add_cog(staff(Bot))