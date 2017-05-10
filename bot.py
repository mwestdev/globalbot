from discord.ext import commands
import discord
import json, asyncio

try:
    import uvloop
except ImportError:
    pass
else:
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

initial_extensions = [
    'cogs.reddit',
    'cogs.raid',
    'cogs.aqual',
    'cogs.roll',
    'cogs.chucknorris',
    'cogs.youtube',
    'cogs.trivia.trivia',
    'cogs.blackjack'
    # 'cogs.help'
]

description = """
Hello! I am a bot written by Globalelite, giving you raid information and more!
"""
help_attrs = dict(hidden=True)
prefix = ['!', '\N{HEAVY EXCLAMATION MARK SYMBOL}']
bot = commands.Bot(command_prefix=prefix, description=description, pm_help=None, help_attrs=help_attrs)

def load_credentials():
    with open('credentials.json') as f:
        return json.load(f)

@bot.event
async def on_read():
    print("Client logged in")

if __name__ == '__main__':
    credentials = load_credentials()
    token = credentials['BOT_TOKEN']
    bot.CLIENT_ID = credentials['CLIENT_ID']
    bot.CLIENT_SECRET = credentials['CLIENT_SECRET']
    bot.PRAW_CLIENT_ID = credentials['PRAW']['CLIENT_ID']
    bot.PRAW_CLIENT_SECRET = credentials['PRAW']['CLIENT_SECRET']
    bot.PRAW_USER_AGENT = credentials['PRAW']['USER_AGENT']
    bot.RAID_HEADERS = credentials['RAID']['HEADERS']
    bot.RAID_DATA = credentials['RAID']['DATA']

    # bot.remove_command('help')

    for extension in initial_extensions:
        bot.load_extension(extension)

    bot.run(token)
