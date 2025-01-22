import discord,subprocess,os,json
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

"""開啟指定應用程式"""
    # 限制可以開啟的應用程式（白名單）
ALLOWED_APPS = {
    "notepad":"C:\Windows\notepad.exe", 
    "c++":"C:\Program Files (x86)\Dev-Cpp\devcpp.exe",
    "街霸":"C:\\Users\\User\\Desktop\\Street Fighter 6.url",
    "kk":"C:\\Users\\User\\AppData\\Local\\Programs\\@universalelectron-shell\\KKBOX.exe",
    "打牌":"C:\\Users\\User\\Desktop\\Yu-Gi-Oh!  Master Duel.url",
    "初音":"C:\\Users\\User\\Desktop\\Desktop Mate.url"
    }

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
async def 欸(ctx, key: str):
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
@bot.command()
async def open(ctx,app_name:str):
    app_path = ALLOWED_APPS.get(app_name.lower()) #lower強制轉換成小寫
    if app_path:
        try:
            os.startfile(app_path)
            await ctx.send(f"開搞")
        except Exception as e:
           await ctx.send(f"無法開啟應用程式 {app_name}，錯誤：{str(e)}")
    else:
        await ctx.send("未找到指定應用程式，請確認名稱是否正確。")

bot.run('your token')
