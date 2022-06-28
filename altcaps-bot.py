from re import M
import discord
from discord.ext import commands 

client = commands.Bot(command_prefix = '!')

@client.event 
async def on_ready():
    general_channel = client.get_channel(932165139053035623)
    await general_channel.send('hi im the altcaps bot! :D')

@client.command(name = 'altcaps')
async def altcaps(ctx, *, input):
    general_channel = client.get_channel(932165139053035623)
    res = ""
    for idx in range(len(input)):
        if idx % 2 == 0:
            res = res + input[idx].upper()
        else:
            res = res + input[idx].lower()
    await ctx.message.channel.send(res)

client.run('OTMyNTM0NzE4NjYxMDIxNzA2.YeUYog.6GJDPrZsZwWBVNEjioSh0dz0mFc')
