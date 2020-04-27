import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='m!')

@bot.command(name='compliment', help='Makes you feel better')
async def nine_nine(ctx):
    compliments = [
        'Everyone has imperfections, you\'re great!',
        'Don\'t be pessimistic, go enjoy life!',
        (
            'Think of the worst person you\'ve ever met and be happy you\'re not like him.'
            'Think of @! Allen#0001 giving you mod perms'
        ),
    ]

    response = random.choice(compliments)
    await ctx.send(response)

@bot.event
async def on_message_delete(message):
    await message.channel.send('Some mf deleted a message, who spotted him')

bot.run(TOKEN)