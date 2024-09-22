import discord
from discord.ext import commands

class Sync(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()
        print("Sync cog loaded.")

    @commands.hybrid_command(name="sync", description="Sync Commands")
    async def sync(self, ctx):
        await ctx.send(f'Synced')

async def setup(bot: commands.Bot):
    await bot.add_cog(Sync(bot))