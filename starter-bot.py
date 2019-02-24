import discord
import asyncio
from discord.ext.commands import Bot

BOT_PREFIX = ('!', '?')
TOKEN = 'NDI4MDE4MDA4NTkwNjQ3Mjk4.DZwnnw.7p9Ky69lgnhqpFg_bEUTAm1N7Pw'
bot = Bot(command_prefix=BOT_PREFIX)

# On user message example.
@bot.event
async def on_message(message):
    await bot.wait_until_ready()
    msg = message.content.split()

# Background task example.
@bot.event
async def my_background_task():
    await bot.wait_until_ready()
    channel = bot.get_channel(id='428635006072520704')
    while not bot.is_closed:
        current_time = time.time()

# On startup message example.
@bot.event
async def on_ready():
    print('Bot online. Beep. Boop.')
    print(bot.user.name)
    print(bot.user.id)
    print('-----------------')


# Starts bot with token
bot.loop.create_task(my_background_task())
bot.run(TOKEN)
