import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import Select, View
import asyncio
from data.Emojis import Emojis
from data.BuildInfo import buildInfo

EmbedColors = {
    'AeroColor': 0x34ebc0,
    'ElectroColor': 0x8c00ff,
    'FusionColor': 0xeb5c34,
    'GlacioColor': 0x69e1ff,
    'HavocColor': 0xe100ff,
    'SpectroColor': 0xfff200
}

ResonatorStar = {
    '4star': '4★',
    '5star': '5★'
}

async def ResonatorAutocomplete(interaction: discord.Interaction, current: str):
    if not current:
        return []
    
    resonators = buildInfo.keys()
    matches = [app_commands.Choice(name=resonator, value=resonator) for resonator in resonators if current.lower() in resonator.lower()]

    if not matches:
        return [app_commands.Choice(name="No options match your search", value="no_match")]

    return matches[:25]

class ResonatorBuild(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Builds cog loaded.")

    def CreateEmbed(self, resonator: str, build_name: str, is_rover: bool = False) -> discord.Embed:
        if not is_rover:
            if resonator not in buildInfo:
                raise ValueError('Resonator not found')
            
            details = buildInfo[resonator]['details'][build_name]
            color = EmbedColors.get(buildInfo[resonator]['color'])
            emb_title = (
                f"{Emojis['ElementType'][buildInfo[resonator]['element']]}  "
                f"{Emojis['WeaponType'][buildInfo[resonator]['weapon']]}  "
                f"{ResonatorStar[buildInfo[resonator]['star']]}  "
                f"{resonator}"
            )
        else:
            if resonator not in buildInfo['Rover']['details']:
                raise ValueError('Rover type not found')

            details = buildInfo['Rover']['details'][resonator]['details'][build_name]
            color = EmbedColors.get(buildInfo['Rover']['details'][resonator]['color'])
            emb_title = (
                f"{Emojis['ElementType'][buildInfo['Rover']['details'][resonator]['element']]}  "
                f"{Emojis['WeaponType'][buildInfo['Rover']['weapon']]}  "
                f"{ResonatorStar['5star']}  "
                f"Rover - {resonator.capitalize()}"
            )

        emb = discord.Embed(title=emb_title, color=color)
        emb.set_thumbnail(url=f"https://raw.githubusercontent.com/krulciferikaru/Database/main/WutheringWavesAssets/CharacterIcons/{resonator.replace(' ', '_')}.png"
                          if not is_rover else 
                               "https://raw.githubusercontent.com/krulciferikaru/Database/main/WutheringWavesAssets/CharacterIcons/Rover.png")

        emb.add_field(name="Echo Set", value=details['echo_set'], inline=False)
        emb.add_field(name="Primary Echo", value=details['main_echo'], inline=False)
        emb.add_field(name="", value=", ".join(details['main_stats']), inline=True)
        emb.add_field(name="Secondary Echo", value="".join(details['sub_echo1']), inline=False)
        emb.add_field(name="", value=", ".join(details['sub_stats1']), inline=False)
        emb.add_field(name="", value="".join(details['sub_echo2']), inline=False)
        emb.add_field(name="", value="".join(details['sub_stats2']), inline=False)
        emb.add_field(name="Sub Stats Priority", value=f"`{details['sub_stats_priority']}`", inline=False)

        return emb

    @app_commands.command(name='build', description='Choose a Resonator Build')
    @app_commands.autocomplete(name=ResonatorAutocomplete)
    async def build(self, interaction: discord.Interaction, name: str) -> None:
        if name == "no_match":
            await interaction.response.send_message("No options match your search. Please try a different query.", ephemeral=True)
            return
        
        name = name.strip()
        if name not in buildInfo:
            await interaction.response.send_message(f"Resonator '{name}' not found. Please try again.", ephemeral=True)
            return

        if name == 'Rover':
            options = buildInfo[name]['options']
            details = buildInfo[name]['details']

            async def rover_callback(rover_interaction: discord.Interaction):
                SelectedRover = rover_interaction.data['values'][0]
                RoverOptions = details[SelectedRover]['options']
                rover_details = details[SelectedRover]['details']

                async def SelectCallback(SelectInteraction: discord.Interaction):
                    SelectedBuild = SelectInteraction.data['values'][0]
                    emb = self.CreateEmbed(SelectedRover, SelectedBuild, is_rover=True)
                    await SelectInteraction.response.edit_message(embed=emb)

                select = Select(
                    placeholder='Choose a build',
                    options=[
                        discord.SelectOption(
                            label=option['label'], 
                            description=option['description'],
                            emoji=option.get('emoji')
                        ) for option in RoverOptions
                    ]
                )
                select.callback = SelectCallback

                view = View()
                view.add_item(select)

                DefaultBuild = RoverOptions[0]['label']
                emb = self.CreateEmbed(SelectedRover, DefaultBuild, is_rover=True)

                await rover_interaction.response.edit_message(content=None, embed=emb, view=view)
                message = await rover_interaction.original_response()

                async def RemoveDropdown(message):
                    await asyncio.sleep(30)
                    view.remove_item(select)
                    await message.edit(view=view)

                self.bot.loop.create_task(RemoveDropdown(message))

            RoverSelect = Select(
                placeholder='Elements',
                options=[
                    discord.SelectOption(
                        label=option['label'], 
                        value=option['value'],
                        emoji=option['emoji']
                    ) for option in options
                ]
            )
            RoverSelect.callback = rover_callback

            RoverView = View()
            RoverView.add_item(RoverSelect)

            await interaction.response.send_message(content='Choose Rover Element:', view=RoverView)
            return

        options = buildInfo[name]['options']
        details = buildInfo[name]['details']

        async def SelectCallback(SelectInteraction: discord.Interaction):
            SelectedBuild = SelectInteraction.data['values'][0]
            emb = self.CreateEmbed(name, SelectedBuild)
            await SelectInteraction.response.edit_message(embed=emb)

        select = Select(
            placeholder='Choose a build',
            options=[
                discord.SelectOption(
                    label=option['label'], 
                    description=option['description'],
                    emoji=option.get('emoji')
                ) for option in options
            ]
        )
        select.callback = SelectCallback

        view = View()
        view.add_item(select)

        DefaultBuild = options[0]['label']
        emb = self.CreateEmbed(name, DefaultBuild)

        await interaction.response.send_message(embed=emb, view=view)
        message = await interaction.original_response()

        async def RemoveDropdown(message):
            await asyncio.sleep(30)
            view.remove_item(select)
            await message.edit(view=view)

        self.bot.loop.create_task(RemoveDropdown(message))

async def setup(bot: commands.Bot):
    await bot.add_cog(ResonatorBuild(bot))