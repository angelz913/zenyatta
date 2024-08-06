import os
import discord
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

# Set intents
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

# Initialize
client = discord.Client(intents=intents)

# When the bot is ready
@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

# When the bot gets a message
@client.event
async def on_message(message):
    # Ignore the bot's own messages
    if message.author == client.user:
        return

    tokens = message.content.split(' ')
    if tokens[0] == "rec":
        try:
            await message.channel.send(message.content)
        except discord.errors.HTTPException:
            print("Failed to send the message")

# Start the bot
client.run(BOT_TOKEN)
