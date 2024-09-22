import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()
        print("Ping cog loaded.")

    @commands.hybrid_command(name="ping", description="Shows the bot's latency in ms.")
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)
        emb = discord.Embed(title="Ping", description="Latency in ms", color=0xf2f2f2)
        emb.add_field(name='Latency:', value=f'{latency}ms', inline=False)
        emb.set_footer(text=f'Requested by {ctx.author}.', icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed=emb)

async def setup(bot: commands.Bot):
    await bot.add_cog(Ping(bot))