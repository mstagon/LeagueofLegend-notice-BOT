import discord
from discord.ext import commands
import requests
from discord.ext import tasks
import asyncio
import random
f = open('token.txt', 'r')
token = f.readline()
apitoken = "RGAPI-d9fac770-ae6d-4e8e-9311-ad9b6704c7ba"

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description="안녕하세요", intents=intents)
summonername = ""
@bot.event
async def on_ready():
    print("띠리링")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

async def get_summonerinfo():
    r = requests.get("https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+summonername+"/?apu_key/"+apitoken)

bot.run(token)