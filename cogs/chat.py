import discord
from discord.ext import commands

class Chat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        
        if message.content.lower() in ["this changes everything", "devs listened"]:
            await message.channel.send("https://i.imgur.com/pqgEtPZ.jpeg")

async def setup(bot):
    await bot.add_cog(Chat(bot))