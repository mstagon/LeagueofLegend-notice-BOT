import datetime

import discord
from discord.ext import commands
import requests
import json
import datetime as dt
from discord.ext import tasks
import asyncio
import random
import schedule
import time

f1 = open('token.txt', 'r')
token = f1.readline()



intents = discord.Intents.default()
intents.members = True
intents.message_content = True


bot = commands.Bot(command_prefix='?', description="안녕하세요", intents=intents)


@bot.event
async def on_ready(self):
    print("띠리링")


@bot.command()
async def startnotice(ctx):

    while True:
        schedule.run_pending()
        time.sleep(1)


async def get_summonerinfo():
    f2 = open('summoner.txt', 'r')
    apitoken = "RGAPI-2e0ba4e1-8781-4e9d-a793-d71bead579f5"
    while True :
        strline = f2.readline()
        if strline == '':

            break
        else:
            summonername = strline
            res1 = requests.get("https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+summonername+"?api_key="+apitoken)
            status1 = res1.status_code
            if status1 == 200:
                summoner_data = json.loads(res1.content)
                summoner_id = summoner_data["id"]
                res2 = requests.get(
                    "https://kr.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/" + summoner_id + "?api_key=" + apitoken)
                status2 = res2.status_code
                if status2 == 200:
                    game_data = json.loads(res2.content)
                    game_mode = game_data["gameMode"]
                    #game_type = game_data["gameType"] I don't know what this mean
                    game_starttimems = game_data["gameStartTime"]
                    game_length = game_data["gameLength"]
                    queue_type = game_data["gameQueueConfigId"]
                    now = datetime.datetime.now()
                    game_time = dt.datetime.fromtimestamp(game_starttimems/1000)
                    playing_time = now.replace(microsecond=0) - game_time.replace(microsecond=0)
                    print(game_mode)
                    #print(game_type) XD
                    print(playing_time)
                    print(game_length)
                    print(queue_type)
            else:
                print(summonername + "소환사 정보를 찾을 수 없습니다.")
            f2.close()

bot.run(token)
