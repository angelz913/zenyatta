import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

# Set intents
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

# Create the bot
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logged in as {bot.user}")

@bot.tree.command(name="rec", description="Give book recommendations based on your prompt")
async def rec(interaction: discord.Interaction, prompt: str):
    await interaction.response.send_message(f"Your prompt was '{prompt}'")

# Start the bot
bot.run(BOT_TOKEN)
