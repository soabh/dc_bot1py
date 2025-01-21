import discord
import json
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True 
intents.guilds = True  

bot = commands.Bot(command_prefix='!', intents=intents)

# 載入和保存資料的函數
def load_data():
    try:
        with open("data.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("資料已儲存:", data)  # 輸出確認資料
    


data_store = load_data()

@bot.event
async def on_ready():
    print(">>bot is online<<")
    print("已註冊的指令：",  [command.name for command in bot.commands])


@bot.command()
async def hello(ctx):
    await ctx.send("寶寶你來了")

@bot.command()
async def learn(ctx,key:str,value:str):
    data_store[key] = value  # 更新資料庫
    save_data(data_store)  # 儲存資料到檔案
    await ctx.send(f"喔")  # 回傳確認訊息

@bot.command()
async def check(ctx, key: str):
    value = data_store.get(key, "不知道")
    await ctx.send(f"{value}")

@bot.command()
async def remove(ctx,key:str):
    if key in data_store:
        del data_store[key]
        save_data(data_store)
        await ctx.send(f"已刪除{key}的資料")
    else:
        await ctx.send(f"不知道{key}")

bot.run('token找我要')
