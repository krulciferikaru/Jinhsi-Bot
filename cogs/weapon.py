import discord
from discord import app_commands
from discord.ext import commands
from data.WeaponData import weaponInfo


EmbedColors = {
    '1StarColor': 0xc7c7c7,
    '2StarColor': 0x9cf3b0,
    '3StarColor': 0xa9eeff,
    '4StarColor': 0xffbdfd,
    '5StarColor': 0xeae387,
}

async def weaponAutocomplete(interaction: discord.Interaction, current: str):
    if not current:
        return []
    
    weapons = [weapon for weaponType in weaponInfo.values() for weapon in weaponType['details'].keys()]
    matches = [app_commands.Choice(name=weapon, value=weapon) for weapon in weapons if current.lower() in weapon.lower()]
    
    if not matches:
        return [app_commands.Choice(name="No options match your search", value="no_match")]

    return matches[:25] 

class Weapons(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("weapons cog loaded.")

    @app_commands.command(name="weapon", description="Select a weapon")
    @app_commands.autocomplete(name=weaponAutocomplete)
    async def weapon(self, interaction: discord.Interaction, name: str):
        if name == "no_match":
            await interaction.response.send_message("No options match your search. Please try a different query.", ephemeral=True)
            return

        weaponDetails = None
        for weaponType in weaponInfo.values():
            if name in weaponType['details']:
                weaponDetails = weaponType['details'][name]
                break

        if not weaponDetails:
            await interaction.response.send_message(f"{name} not found. Please try again.", ephemeral=True)
            return

        star = weaponDetails['star']
        EmbedTitle = f"{star}  {name}"
        starRank = star.split('★')[0]
        EmbedColor = EmbedColors.get(f'{starRank}StarColor', discord.Color.blue())

        emb = discord.Embed(title=EmbedTitle, color=EmbedColor)

        emb.set_thumbnail(url=f"https://raw.githubusercontent.com/krulciferikaru/Database/main/WutheringWavesAssets/WeaponIcons/{name.replace(' ', '_')}.png")
        emb.add_field(name='', value=weaponDetails['description'], inline=False)
        emb.add_field(name=f"{weaponDetails['atk']['icon']} {weaponDetails['atk']['title']}", value=f"(Lv.90): {weaponDetails['atk']['stats']}", inline=True)
        emb.add_field(name=f"{weaponDetails['mainstat']['icon']} {weaponDetails['mainstat']['title']}", value=f"(Lv.90): {weaponDetails['mainstat']['stats']}", inline=True)

        await interaction.response.send_message(embed=emb, ephemeral=False)

async def setup(bot: commands.Bot):
    await bot.add_cog(Weapons(bot))
