import discord
import time
from discord.ext import commands, tasks

from random import choice

client = commands.Bot(command_prefix='b!')

@client.event
async def on_ready():
    change_status.start()
    print('balls are on')

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='general')
    await channel.send(f'Welcome {member.mention}!  Ready to jam out? See `?help` command for details!')
        
@client.command(name='ping', help='balls')
async def ping(ctx):
    await ctx.send(f'**balls** latency: {round(client.latency * 1000)}ms')

@client.command(name='balls')
async def balls(ctx):
    while(True):
        await ctx.author.send('b a l l s')
        time.sleep(0.5)

@tasks.loop(seconds=20)
async def change_status():
    await client.change_presence(activity=discord.Game("with my balls"))

client.run(yo mama)