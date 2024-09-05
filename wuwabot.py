import os
import asyncio
import discord
import config
from discord.ext import commands
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="=", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print("Bot is connected to Discord")

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
                print(f'Loaded extension: cogs.{filename[:-3]}')
            except Exception as e:
                print(f'Failed to load extension {filename[:-3]}: {type(e).__name__} - {e}')
            
async def main():
    await load()
    await bot.start(config.TOKEN)

if __name__ == "__main__":
    asyncio.run(main())