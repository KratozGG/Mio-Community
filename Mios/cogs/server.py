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


class server(commands.Cog):
  def __init__(self, Bot):
    self.Bot = Bot
  @commands.command()
  async def ping(self, ctx):
          pingemb = discord.Embed(title="**Ping**", description=f'My ping is `{round(self.Bot.latency * 100)}ms`', color=discord.Colour.random())
          pingemb.timestamp = datetime.datetime.utcnow()
          pingemb.set_footer(text="Mio's Community")
          await ctx.send(embed=pingemb)

  @commands.command()
  async def devinfo(self, ctx):
          devinfoemb = discord.Embed(title="Developer Information",description="I'm currently being developed by KraToz. He is a very cool developer :D",color=discord.Colour.random())
          devinfoemb.set_image(url="https://www.google.com/url?sa=i&url=https%3A%2F%2Fweheartit.com%2Fentry%2F296174630&psig=AOvVaw0lpNgq1K-h3csZLHIxwHCo&ust=1642739364722000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCLjb2Jm_v_UCFQAAAAAdAAAAABAJ")
          devinfoemb.set_footer(text="Mio's Community")
          await ctx.send(embed=devinfoemb)

  @commands.command(aliases=['s'])
  async def suggest(self, ctx, *, suggestion):
    await ctx.channel.purge(limit=1)
    channel = self.Bot.get_channel(933574171705876490)
    suglogchn = self.Bot.get_channel(933595881456951337)

    suggestemb = discord.Embed(color=0x0600ff)
    suggestemb.set_author(name=f'Suggested by {ctx.message.author}', icon_url = f' {ctx.author.avatar_url}')
    suggestemb.add_field(name='Suggestion!', value=f'{suggestion}')

    
  

    slogemb = discord.Embed(title = "Suggestion command usage", description = f"{ctx.author} has used the suggestion command in {ctx.channel}", color=0x0600ff)
    
    message = await channel.send(embed=suggestemb)
    
    await suglogchn.send(embed=slogemb)

    await message.add_reaction('✅')
    await message.add_reaction('❌')
    
  @commands.command(aliases=['r'])
  async def report(self, ctx, member:discord.Member, *, report=None):
    report_channel = self.Bot.get_channel(933615898172989470)
    if member is None:
      return await ctx.reply("Kindly specify an User in order to report!")
    if report is None:
      return await ctx.reply("Kindly specify the appropriate information after metioning the rule breaker!")
    else:
      reportemb = discord.Embed(title="User Report", description=f"{ctx.author.mention} has reported {member}")
      reportemb.set_thumbnail(url="")
      reportemb.add_field(name="Information / Evidence :", value=f"{report}")
      reportemb.set_footer(icon_url=ctx.author.avatar_url, text=f"React with ✅ if the evidence is valid and the action has been taken")
      report_message = await report_channel.send(embed=reportemb)
      await report_message.add_reaction('✅')
      await ctx.send(f"{ctx.author.mention} Your report has been sent!")

      try:
        def check(reaction, user):
          return user == ctx.author and str(reaction.emoji) in ["✅"]
        
        reaction, user = await commands.wait_for("reaction_add", timeout=604800, check=check)

        if str(reaction.emoji) == "✅":
          await report_message.reply("Report has been accepted!")
      except Exception as e:
        print(e)


  @commands.command()
  async def serverinfo(self, ctx):
    created_at = ctx.guild.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")
    server_owner = str(ctx.guild.owner)
    serverinfoemb=discord.Embed(title="",color=0x71368a)

    serverinfoemb.add_field(name="Server Owner", value="Mio_Naruse#0537", inline=True)
    serverinfoemb.add_field(name="Server ID", value=f"{ctx.guild.id}", inline=True)
    serverinfoemb.add_field(name="Members", value=f"{ctx.guild.member_count}", inline=True)
    serverinfoemb.add_field(name="Channels count", value=f"{len(ctx.guild.channels)}", inline=True)
    serverinfoemb.add_field(name="Text channels", value=f"{len(ctx.guild.text_channels)}", inline=True)
    serverinfoemb.add_field(name="Voice channels", value=f"{len(ctx.guild.voice_channels)}", inline=True)
    serverinfoemb.add_field(name="Roles", value=f"{len(ctx.guild.roles)}", inline=True)
    
    serverinfoemb.set_thumbnail(url=f"{ctx.guild.icon_url}")
    serverinfoemb.set_author(name=f"{ctx.guild.name}", icon_url=f"{ctx.guild.icon_url}")
    serverinfoemb.set_footer(text=f"Created on {created_at}")
    await ctx.send(embed=serverinfoemb)



  

  @commands.command()
  async def membercount(self, ctx):
    mcemb = discord.Embed(title="Member count", description = f"{ctx.guild.member_count}",color=discord.Colour.random())
    mcemb.set_footer(text=f"Issued by {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
    await ctx.send(embed=mcemb)

  @commands.command()
  async def zfrostt(self, ctx):
    
    
    frost = """=> zFrostt is a twitch streamer who streams minecraft (PikaNetwork) and Call of duty.
    
    => He is a very good entertainer and thus he deserves more followers on twitch.
    
    => If he hits 150 followers on twitch, we will be giving away x1 Pikanetwork VIP rank. But in the case if he reaches 150 followers within this weekend, we will be giving away x2 VIP ranks
    
    => So go Follow him on twitch!!!
    
    => https://www.twitch.tv/zfrostt/"""
    


    
    zfrostt = discord.Embed(title = "Support ZFrostt", description="=>zFrostt is live, go watch him on twitch!!!\n=> https://www.twitch.tv/zfrostt/", color=discord.Colour.random())
    zfrostt.set_footer(text="Follow zFrostt on twitch")
    zfrostt.set_thumbnail(url="https://cdn.discordapp.com/attachments/934777769861206016/935120333508313128/unknown.png")
    zfrostt.set_image(url="https://cdn.discordapp.com/attachments/934777769861206016/935120271684304956/unknown.png")

    await ctx.send(embed = zfrostt)
  
  @commands.command(case_insensitive = True, aliases = ["remind", "remindme", "remind_me"])
  @commands.bot_has_permissions(attach_files = True, embed_links = True)
  async def reminder(self, ctx, time, *, reminder):
      print(time)
      print(reminder)
      user = ctx.message.author
      embed = discord.Embed(color=0x55a7f7, timestamp=datetime.datetime.utcnow())
      embed.set_footer(text="Mio's community", icon_url=f"{self.Bot.user.avatar_url}")
      seconds = 0
      if reminder is None:
          embed.add_field(name='Warning', value='Please specify what do you want me to remind you.') # Error message
      if time.lower().endswith("d"):
          seconds += int(time[:-1]) * 60 * 60 * 24
          counter = f"{seconds // 60 // 60 // 24} days"
      if time.lower().endswith("h"):
          seconds += int(time[:-1]) * 60 * 60
          counter = f"{seconds // 60 // 60} hours"
      elif time.lower().endswith("m"):
          seconds += int(time[:-1]) * 60
          counter = f"{seconds // 60} minutes"
      elif time.lower().endswith("s"):
          seconds += int(time[:-1])
          counter = f"{seconds} seconds"
      if seconds == 0:
          embed.add_field(name='Warning',
                          value='Please specify a proper duration.')
      elif seconds < 300:
          embed.add_field(name='Warning',
                          value='You have specified a too short duration!\nMinimum duration is 5 minutes.')
      elif seconds > 7776000:
          embed.add_field(name='Warning', value='You have specified a too long duration!\nMaximum duration is 90 days.')
      else:
        embed = discord.Embed(title="Reminder", description=f"Reminder: {reminder}\nTime: {counter}", color=discord.Colour.random())
        await ctx.send(embed=embed)
        await asyncio.sleep(seconds)
        await ctx.send(f"Reminder,{user.mention} you set your reminder about {reminder} {counter} ago.")  
        return
      await ctx.send(embed=embed)




  afks = {}

  @commands.command(pass_context = True)
  async def afk(self, ctx, *, reason = "No reason provided"):
    
    member = ctx.author
    if member.id in afks.keys():
      afks.pop(member.id)
    else:
      try:
        await member.edit(nick = f"[AFK] {member.display_name}")
      except:
        pass

    afks[member.id] = reason
    embed = discord.Embed(title = "Member AFK", description = f"{member.mention} has gone AFK", color = member.color)
    embed.set_thumbnail(url = member.avatar_url)
    embed.set_author(name=commands.user.name, icon_url= commands.user.avatar_url)
    embed.add_field(name='AFK Reason:', value=reason)
    await ctx.send(embed=embed)

  def remove(afk):
    if "[AFK]" in afk.split():
      return " ".join(afk.split()[1:])
    else:
      return afk


  @commands.Cog.listener()
  async def on_message2(message):
    if message.author.id in afks.keys():
      afks.pop(message.author.id)
      try:
        await message.author.edit(nick = afks.pop(message.author.display_name))
      except:
        pass
      await message.channel.send(f'Welcome back {message.author.mention}, I removed your AFK')

    for id, reason in afks.items():
      member = get(message.guild.members, id = id) 
      if (message.reference and member == (await message.channel.fetch_message(message.reference.message_id)).author) or member.id in message.raw_mentions:
        await message.reply(f"{member.name} is AFK ; AFK reason - {reason}")


  rolleventpart = []
        
  @commands.command()
  async def register(self, ctx):
    """t = <t:1642946400>"""
    emoji = "<:tick_yes:930438933228175370>"
    embed = discord.Embed(title="", description=f"Registrations has been closed!", color= 0x19df5f)
    await ctx.send(embed=embed)

  @commands.command(aliases=["nreq"])
  async def nickreq(self,ctx, *, name):
    embednick = discord.Embed(title="Nickname Request", description = f"{ctx.author.name} has requested to change their name to {name}", color=discord.Colour.random())

    embednick.set_footer(text="Mio's community")

    channel2 = self.Bot.get_channel(929767377086849092)

    await ctx.reply("Your request has been sent!")
    await channel2.send(embed=embednick)

def setup(Bot):
  Bot.add_cog(server(Bot))
