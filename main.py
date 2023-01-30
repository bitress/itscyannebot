import discord
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

intents = discord.Intents.default()

intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def calc(ctx, operation: str):
    await ctx.send(eval(operation))



@bot.command()
async def send(ctx, *, message=""):
    c = bot.get_channel(1015869733809176638)
    await c.send(f"{message}")


@bot.command()
async def sendTest(ctx, *, message=""):
    c = bot.get_channel(1036290766290563114)
    await c.send(f"{message}")


@bot.command()
async def sayHere(ctx, *, message=""):
    await ctx.send(f"{message}")


@bot.command()
async def sendDM(ctx, user: discord.User, *, message=""):
    await user.send(f"{message}")


token = ("TOKEN")
bot.run(token)
