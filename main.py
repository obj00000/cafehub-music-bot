import discord
from discord.ext import commands

# Set up the bot
intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Load cogs
@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

# Start the bot
if __name__ == '__main__':
    bot.run('YOUR_TOKEN_HERE')
