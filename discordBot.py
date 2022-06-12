import discord
import discord.guild
from discord.ext import commands

TOKEN = #"yourTokenHere"

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@client.event
async def on_message(msg):
    if msg.author != client.user.name:
        print(f"{msg.author} sayed: {msg.content}")
    else:
        pass
    await client.process_commands(msg)

@client.command()
async def message(ctx, user:discord.Member, *, message=None):
    embed = discord.Embed(title=message)
    print(user)
    await user.send(embed=embed)

@client.command()
@commands.has_role("test")
async def memberslist(ctx):
    text: str = ""
    for guild in client.guilds:
        text = text + f"\n {str(guild).upper()}"
        for member in guild.members:
            text = text + f"\n      {str(member)}"
            print(member)
    await ctx.send(text)

@client.command()
@commands.has_role("test")
async def spam(ctx, *, message=""):
    memberList = []
    sendList: str = ""
    embed = discord.Embed(title=f"{message}")
    for guild in client.guilds:
        sendList = sendList + f"\n{str(guild).upper()}"
        for member in guild.members:
            if member not in memberList:
                try:
                    await member.send(embed=embed)
                    print(f"Message successfully sent to {member}")
                    sendList = sendList + f"\n      Message successfully sent to {str(member)}"
                    memberList.append(member)
                except Exception:
                    print(f"Failed to send message to {member}")
                    sendList = sendList + f"\n      Failed to send message to {str(member)}"
    await ctx.send(sendList)

client.run(TOKEN)
