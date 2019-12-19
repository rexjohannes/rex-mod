import discord
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("Powered by rexjohannes98"))
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
    if member == None:
        member = ctx.author
    nickname = ' '.join(name)
    await member.edit(nick=nickname)
    if nickname:
        msg = f':ok: Changed nick from {member} to: **{nickname}**'
    else:
        msg = f':ok: Reseted nick from {member} to: **{member.name}**'
    await ctx.send(msg)
    
@bot.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("Please specify a member")
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
    if not member:
        await ctx.send("Please specify a member")
        return
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(role)
    await ctx.send(f"Unmuted {member}")
@mute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to unmute people")
    
@bot.command(aliases=['purge'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, menge=100):
    await ctx.channel.purge(limit=menge)
    await ctx.send(f"Cleared {menge} messages")
    
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"Kicked {member}")
    
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"Banned {member}")
    
@bot.command()
@commands.has_permissions(manage_messages=True)
async def warn(ctx, member:str, grund:str):
    await ctx.send(f"{ctx.author} has warned {member} for Reason: {grund}")
    

@bot.command()
@commands.has_permissions(administrator=True)
async def say(ctx, *, message:str):
    await ctx.send(f"{message}")

bot.run('TOKEN')
