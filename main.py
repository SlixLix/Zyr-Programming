import time
from webserver import keep_alive
import os
import meat import beat 
import discord
import asyncio
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='$', intents=intents)

@client.event
async def on_ready():
  print('Bot go brrr')
  while True:
    await client.change_presence(status=discord.Status.online, activity=discord.Game('League Of Legends'))
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Fornite'))
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Finding my father'))
@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send('you dont have the correct permissions to do that, retard.')
        await ctx.message.delete()
    elif isinstance(error,commands.MissingRequiredArgument):
        await ctx.send('you didnt provide the correct amount of arguments :skull:')
        await ctx.message.delete()


@client.command(aliases=['k'])
@commands.has_permissions(kick_members = True)  
async def kick(ctx, member : discord.Member, *, reason=None):
  await ctx.send(f'{member} has been kicked for: ' + reason + ' ' + 'lmfao what a L')
  await member.send('You have been kicked from Zyr Programming Language for:' + reason)
  await member.kick(reason=reason)



@client.command(aliases=['b'])
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason=None):
  await ctx.send(f'{member} has been banned for: ' + reason + ' ' + 'lmfao what a L')
  await member.send('You have been banned from Zyr Programming Language for:' + reason)
  await member.ban(reason=reason)





@client.command()
@commands.has_permissions(manage_messages = True)
async def warn(ctx, member : discord.Member, *, reason=None):
 await member.send(f'you were warned in Zyr Programming Language for: {reason}')
 await ctx.send(f'warned {member.mention} for {reason}.')



@client.command(aliases=["userinfo"])
async def whois(ctx, member: discord.Member = None):
    if not member:  # if member is no mentioned
        member = ctx.message.author  # set member as the author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=discord.Colour.red(), timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}")

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Display Name:", value=member.display_name)

    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name="Roles:", value="".join([role.mention for role in roles]))
    embed.add_field(name="Highest Role:", value=member.top_role.mention)
    print(member.top_role.mention)
    await ctx.send(embed=embed)


@client.command(aliases=['m'])
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)

    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(f"Muted {member.mention} for reason {reason}")
    await member.send(f"You were muted in Zyr Programming Language for: {reason}")

@client.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    await ctx.send(f"Unmuted {member.mention}")
    await member.send(f"You were unmuted in Zyr Programming Language.")

@client.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def purge(ctx,limit: int):
  if limit>100:
    await ctx.send("The limit is 100, so I can't delete more lmfao")
    return
  await asyncio.sleep(2)
  await ctx.channel.purge(limit=limit)

  await ctx.send(f"purged by {ctx.message.author.mention}")
  time.sleep(2)
  await ctx.message.delete()

@client.command(aliases=['av'])
async def avatar(ctx, member: discord.Member = None):
  if not member:
    member = ctx.message.author

  embed = discord.Embed(colour=discord.Colour.red())
  embed.set_image(url=member.avatar_url)
  await ctx.send(embed=embed)
  


@client.command(aliases=['git'])
async def github(ctx):
  await ctx.send("https://github.com/Slav-XpXz")



@client.command()
async def zyr(ctx):
  await ctx.send("https://github.com/Slav-XpXz/Zyr")


@client.command()
async def patreon(ctx):
  await ctx.send("https://www.patreon.com/slav_XpXz")

@client.command()
async def mwa(ctx, member: discord.Member = None):
  if not member:
    await     ctx.send(f'{ctx.message.author.mention} so lonely trying to kiss your self :skull:')

  await ctx.send(f'{ctx.message.author.mention} kissed {member.mention} pretty sexy')
@client.command()
async def colourchroma(ctx, member: discord.Member = None):
  if not member:
    member = ctx.message.author
  await member.edit(nick="Colourchroma")
  await ctx.send(f'Synth 2.0 that you?! {member.mention}')



@client.command(alias=['n'])
async def nick(ctx, member: discord.Member = None, *, nick):
  await member.edit(nick=nick)
  await ctx.send(f"Set {member.mention}'s nickname to {nick}")




@client.command()
async def ineedhelp(ctx):
  await ctx.send("I'd rather play Visual Studio Code retard")









TOKEN = os.environ['token']
keep_alive()
client.run(TOKEN)
