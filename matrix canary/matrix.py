import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix="|")

async def on_ready():
    print ("Ready")

@bot.command(pass_context=True)
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.event
async def on_message(message):
    if message.content.startswith('!hello'):
        embed = discord.Embed(title="Title", description="Desc", color=0x851199)
        embed.add_field(name="Field1", value="hi", inline=False)
        embed.add_field(name="Field2", value="hi2", inline=False)
        await message.channel.send(embed=embed)

bot.run(TOKEN)