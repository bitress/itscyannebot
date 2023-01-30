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

    scheduler = AsyncIOScheduler()

    # sends "Your Message" at 12PM and 18PM (Local Time)
    scheduler.add_job(sayGoodNight, CronTrigger(hour="23", minute="00", second="00"))
    scheduler.add_job(sayGoodMorning, CronTrigger(hour="8", minute="00", second="00"))

    # starting the scheduler
    scheduler.start()


async def sayGoodNight():
    await bot.wait_until_ready()
    c = bot.get_channel(1015869733809176638)
    await c.send("good night, babe!")


async def sayGoodMorning():
    await bot.wait_until_ready()
    c = bot.get_channel(1015869733809176638)
    await c.send("good morning, babe!")


@bot.command()
async def calc(ctx, operation: str):
    await ctx.send(eval(operation))


@bot.command()
async def love(ctx, times: int, name=''):
    c = bot.get_channel(1015869733809176638)
    for i in range(times):
        await c.send("i love you, babe! " + name)


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


token = ("MTAzNjI1MjMyNjAxMDMwNjU5MQ.GBDM6X.JxP7dVPT__GvGrbpnajaLZFwLtuZapS-3L3OwU")
bot.run(token)
