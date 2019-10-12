import discord
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix=':')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("Powered by Open-Media.tk"))
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(discord.utils.oauth_url(bot.user.id))

    
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing Argument!")
        
@bot.command()
@commands.bot_has_permissions(manage_nicknames = True)
async def nick(ctx, member: discord.Member=None, *name):
    '''Ändert den Nickname eines Benutzer'''
    if member == None:
        member = ctx.author
    nickname = ' '.join(name)
    await member.edit(nick=nickname)
    if nickname:
        msg = f':ok: Ändere Nickname von {member} zu: **{nickname}**'
    else:
        msg = f':ok: Reset von Nickname für {member} auf: **{member.name}**'
    await ctx.send(msg)
    
@bot.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member=None):
    '''Muted einen Benutzer'''
    if not member:
        await ctx.send("Bitte gib einen User an!")
        return
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(role)
    await ctx.send("Muted!")
@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to mute people")
 

@bot.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, member: discord.Member=None):
    '''Entmuted einen Benutzer'''
    if not member:
        await ctx.send("Please specify a member")
        return
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(role)
    await ctx.send("Unmuted!")
@mute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to unmute people")
    
@bot.command(aliases=['purge'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, menge=100):
    '''Leert den Chat'''
    await ctx.channel.purge(limit=menge)
    await ctx.send("Cleared!")
    
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    '''Kickt einen Benutzer'''
    await member.kick(reason=reason)
    await ctx.send("Kicked!")
    
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    '''Bannt einen Benutzer'''
    await member.ban(reason=reason)
    await ctx.send("Banned!")
    
@bot.command()
@commands.has_permissions(manage_messages=True)
async def warn(ctx, member:str, grund:str):
    '''Warnt einen Benutzer'''
    await ctx.send(f"{ctx.author} has warned {member} for Reason: {grund}")
    

@bot.command()
@commands.has_permissions(administrator=True)
async def say(ctx, *, message:str):
    '''Wiederhohlt die Nachricht vom Bot!'''
    await ctx.send(f"{message}")

        
#bot.remove_command('help')

#@bot.command()
#async def help(ctx):
#  await ctx.send("Commands: \nhelp - View this message.")
  
  
bot.run('NjMyNTM5NjgwOTU2NzQzNjgy.XaG4xg.uCp0iUMetGQMBVRIvpK0-CD4lpk')
