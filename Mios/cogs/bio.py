import discord
from discord.ext import commands

class bio(commands.Cog):
  def __init__(self, Bot):
    self.Bot = Bot

  @commands.command(pass_context =True)
  async def info(self, ctx, name: str=None):
    
    if name is None:
      await ctx.send("Please specify a person!")
    else:
      pass

    #kratoz
    kraemb = discord.Embed(title="Biography of Kratoz!", description = "A Super cool Developer and Sr.Mod who is professional and excellent at his work.", color = discord.Colour.random())

    kraemb.set_footer(text="Mio's Community Staff Team")

    #shinji
    shiemb = discord.Embed(title = "Biography of Detective Shinji Ikari", description = "Weeb and gamer which is active most of the time", color = discord.Colour.random())
    shiemb.set_footer(text = "Mio's community")

    #abid
    abidemb = discord.Embed(title="Biography of Abid_YT", description = "Abid is a normie gamer who flexes with his bloody mouse. He is an admin who has got skill issues", color = discord.Colour.random())
    abidemb.set_footer(text = "Mio's Community Staff")

    if name == "kratoz":
      await ctx.send(embed=kraemb)

    elif name == "shinji":
      await ctx.send(embed = shiemb)

    elif name == "abid":
      await ctx.send(embed = abidemb)

    

def setup(Bot):
  Bot.add_cog(bio(Bot))





  