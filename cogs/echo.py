import discord
from discord.ext import commands
from discord import app_commands
from data.EchoInfo import echoInfo

EmbedColors = {
    'Common': 0xffffff,
    'Elite': 0x7cbf8e, 
    'Overlord': 0xf2ffa1, 
    'Calamity': 0xff3636
}

async def EchoAutocomplete(interaction: discord.Interaction, current: str):
    if not current:
        return []

    echoes = echoInfo.keys()
    matches = [app_commands.Choice(name=echo, value=echo) for echo in echoes if current.lower() in echo.lower()]

    if not matches:
        return [app_commands.Choice(name="No options match your search", value="no_match")]

    return matches[:25]

class Echoes(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Echo cog loaded.")

    @app_commands.command(name="echo", description="Select an Echo")
    @app_commands.autocomplete(name=EchoAutocomplete)
    async def echo(self, interaction: discord.Interaction, name: str):
        if name == "no_match":
            await interaction.response.send_message("No options match your search. Please try a different query.", ephemeral=True)
            return

        echoDetails = echoInfo.get(name)
        
        if not echoDetails:
            await interaction.response.send_message(f"{name} not found. Please try again.", ephemeral=True)
            return

        EmbedTitle = f"{name}"
        EmbedColor = EmbedColors.get(echoDetails['Class'])

        emb = discord.Embed(title=EmbedTitle, color=EmbedColor)
        emb.set_thumbnail(url=f"https://raw.githubusercontent.com/krulciferikaru/Database/main/WutheringWavesAssets/EchoIcons/{name.replace(' ', '_')}.png")
        emb.add_field(name="Cost", value=echoDetails['Cost'], inline=True)
        emb.add_field(name="Class", value=echoDetails['Class'], inline=True)
        emb.add_field(name="Sonata Effect", value=" ".join(echoDetails['SonataEffects']), inline=True)
        emb.add_field(name="Description", value=echoDetails['Description'], inline=False)

        await interaction.response.send_message(embed=emb, ephemeral=False)

async def setup(bot: commands.Bot):
    await bot.add_cog(Echoes(bot))