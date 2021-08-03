import discord
import os
from discord.ext import commands

PREFIX = "/"

bot = commands.Bot(command_prefix=PREFIX)

TOKEN = 'Token here pls'
#MINIGAMES1 = "hide & seek"
#MINIGAMES2 = "shooter"
#MINIGAMES3 = "Parkour"
IP = "here your server ip!"

##bot made by ItsJeBoyGoogle

print("Bot Connected")
print("Running!")
# Bot Attribute

var = "a"

@bot.command(pass_context=True)
async def day485(ctx, variable):
  global var
  await ctx.message.delete()
  file = open("day.txt","w")
  print("Before", variable)
  var = variable
  file.write(var)
  file.close()
  await ctx.send(var, delete_after=10.0)


@bot.command()
async def minigames(ctx):
    await ctx.message.delete()
    f = open("day.txt","r")
    contents =f.read()
    f.close()
    
    file=open('minigames.txt')
    content = file.readlines()
    var1=content[0]
    var2=content[1]
    var3=content[2]
    file.close
    
    embed=discord.Embed(title="What minigames do we play on "+ contents + "?", description="Have fun!", color=0x39aa31)
    embed.add_field(name="MINIGAME 1", value=var1, inline=True)
    embed.add_field(name="MINIGAME 2", value=var2, inline=True)
    embed.add_field(name="MINIGAME 3", value=var3, inline=True)
    embed.set_footer(text="Join "+IP)
    # await ctx.send()
    await ctx.send(embed=embed, delete_after=10.0)
    

@bot.command()
async def minigames4(ctx):
    await ctx.message.delete()
    f = open("day.txt","r")
    contents =f.read()
    
    file=open('minigames.txt')
    content = file.readlines()
    var1=content[0]
    var2=content[1]
    var3=content[2]
    file.close
    
    embed=discord.Embed(title="Choose which minigames to play on "+ contents + ".", description="Have fun!", color=0x39aa31)
    embed.add_field(name="MINIGAME 1", value=var1, inline=True)
    embed.add_field(name="MINIGAME 2", value=var2, inline=True)
    embed.add_field(name="MINIGAME 3", value=var3, inline=True)
    embed.set_footer(text="Join "+IP)
    await ctx.send(embed=embed)

    
@bot.event
async def on_message(message):
    if message.author.id == bot.user.id:
        return
    
    msg_content = message.content.lower()
        
    ip = ['ip', 'IP']

    if any(word in msg_content for word in ip):
        await message.channel.send(IP)   
    await bot.process_commands(message)

bot.run(TOKEN)