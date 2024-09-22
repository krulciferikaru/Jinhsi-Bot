import discord
from discord.ext import commands
from discord import app_commands, ui
import asyncio
from data.ResonatorSkillsInfo import resonatorSkillsInfo
from data.ResonatorSkillsEmoji import resonatorSkillsEmoji
from data.ResonatorEmbedColors import resonatorEmbedColors, EmbedColors
from data.ResonatorInfo import resonatorInfo

class ResonatorSkills(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.resonatorSkills = resonatorSkillsInfo
        self.resonatorSkillsEmoji = resonatorSkillsEmoji

    @commands.Cog.listener()
    async def on_ready(self):
        print("Resonator Skills cog loaded.")

    async def resonator_autocomplete(self, interaction: discord.Interaction, current: str):
        if not current:
            return []

        resonators = self.resonatorSkills.keys()
        matches = [app_commands.Choice(name=resonator, value=resonator) for resonator in resonators if current.lower() in resonator.lower()]

        return matches[:25]

    async def skill_autocomplete(self, interaction: discord.Interaction, current: str):
        resonator = interaction.data.get('options', [{}])[0].get('value', "Forte Circuit")
        if resonator in self.resonatorSkills:
            skills = self.resonatorSkills[resonator]
            choices = [
                app_commands.Choice(
                    name=skill,
                    value=skill
                ) for skill in skills if current.lower() in skill.lower()
            ]
            choices.insert(0, app_commands.Choice(name="All", value="All"))
            return choices
        return []

    @app_commands.command(name='skill', description="Displays resonator skills")
    @app_commands.describe(resonator="Name of resonator", skill="Displays resonator skills. Default: Forte Circuit")
    @app_commands.autocomplete(resonator=resonator_autocomplete)
    @app_commands.autocomplete(skill=skill_autocomplete)
    async def skill(self, interaction: discord.Interaction, resonator: str, skill: str = "Forte Circuit"):
        
        resonator_data = resonatorInfo.get(resonator, {})
        weaponEmoji = resonator_data.get('weapon', '')
        elementEmoji = resonator_data.get('element', '')
        starEmoji = resonator_data.get('star', '')

        if resonator in self.resonatorSkills:
            skills = self.resonatorSkills[resonator]
            emojis = self.resonatorSkillsEmoji.get(resonator, {})
            color_key = resonatorEmbedColors.get(resonator, {}).get('color', 'defaultColor')
            embed_color = EmbedColors.get(color_key)  

            if skill == "All":
                categories = {
                    "Active Skills": ["Basic Attack", "Resonance Skill", "Resonance Liberation"],
                    "Passive Skills": ["Forte Circuit", "Inherent Skill 1", "Inherent Skill 2"],
                    "Concerto Skills": ["Intro Skill", "Outro Skill"],
                    "Resonance Chain": ["Sequence 1", "Sequence 2", "Sequence 3", "Sequence 4", "Sequence 5", "Sequence 6"]
                }
                
                category_descriptions = {
                    "Active Skills": "Basic Attack, Resonance Skill, Resonance Liberation",
                    "Passive Skills": "Forte Circuit, Inherent Skills",
                    "Concerto Skills": "Intro & Outro Skills",
                    "Resonance Chain": "Resonator Sequences"
                }
                default_category = "Active Skills"
                skills_list = categories[default_category]

                embed = discord.Embed(
                    title=f"{elementEmoji}  {weaponEmoji}  {starEmoji}  {default_category}",
                    description="\n\n".join(
                        f"{emojis.get(skill, '❓')} **{skills[skill]['name']} - {skill}**\n{skills[skill]['description']}"
                        for skill in skills_list if skill in skills
                    ),
                    color=embed_color
                ).set_author(name=f"{resonator}", icon_url=f"https://raw.githubusercontent.com/krulciferikaru/Database/main/WutheringWavesAssets/CharacterIcons/{resonator.replace(' ', '_')}.png")
                embed.set_thumbnail(url=f"https://raw.githubusercontent.com/krulciferikaru/Database/main/WutheringWavesAssets/CharacterIcons/{resonator.replace(' ', '_')}.png")

                # Creating category select menu
                category_menu = ui.Select(
                    placeholder="Select Skill Category",
                    options=[discord.SelectOption(
                        label=category, 
                        value=category,
                        description=category_descriptions.get(category, "")) 
                        for category in categories.keys()],
                    custom_id=f'category_select_{resonator}'
                )
                
                view = ui.View()
                view.add_item(category_menu)

                await interaction.response.send_message(embed=embed, view=view)
                message = await interaction.original_response()
                
                async def removeDropdown(message):
                    await asyncio.sleep(60)
                    view.remove_item(category_menu)
                    await message.edit(view=view)

                self.bot.loop.create_task(removeDropdown(message))
  
            else:
                if skill in skills:
                    embed = discord.Embed(
                        title=f"{elementEmoji}  {weaponEmoji}  {starEmoji}  {skill}",
                        description=(f"{emojis.get(skill, '❓')} **{skills[skill]['name']}**\n{skills[skill]['description']}"),
                        color=embed_color
                    ).set_author(name=f"{resonator}", icon_url=f"https://raw.githubusercontent.com/krulciferikaru/Database/main/WutheringWavesAssets/CharacterIcons/{resonator.replace(' ', '_')}.png")
                    embed.set_thumbnail(url=f"https://raw.githubusercontent.com/krulciferikaru/Database/main/WutheringWavesAssets/CharacterIcons/{resonator.replace(' ', '_')}.png")

                    skill_menu = ui.Select(
                        placeholder="Select Skill",
                        options=[discord.SelectOption(label=s, value=s, emoji=emojis.get(s, '❓')) for s in skills],
                        custom_id=f'skill_select_{resonator}'
                    )
                    
                    view = ui.View()
                    view.add_item(skill_menu)

                await interaction.response.send_message(embed=embed, view=view)
                message = await interaction.original_response()
                
                async def removeDropdown(message):
                    await asyncio.sleep(60)
                    view.remove_item(skill_menu)
                    await message.edit(view=view)

                self.bot.loop.create_task(removeDropdown(message))

    @commands.Cog.listener()
    async def on_interaction(self, interaction: discord.Interaction):
        if interaction.type == discord.InteractionType.component:
            custom_id = interaction.data.get('custom_id')
            if custom_id:
                resonator = custom_id.split('_')[-1]

                resonator_data = resonatorInfo.get(resonator, {})
                weaponEmoji = resonator_data.get('weapon', '')
                elementEmoji = resonator_data.get('element', '')
                starEmoji = resonator_data.get('star', '')

                await interaction.response.defer()

                if custom_id.startswith('category_select_'):
                    selected_category = interaction.data['values'][0]
                    categories = {
                        "Active Skills": ["Basic Attack", "Resonance Skill", "Resonance Liberation"],
                        "Passive Skills": ["Forte Circuit", "Inherent Skill 1", "Inherent Skill 2"],
                        "Concerto Skills": ["Intro Skill", "Outro Skill"],
                        "Resonance Chain": ["Sequence 1", "Sequence 2", "Sequence 3", "Sequence 4", "Sequence 5", "Sequence 6"]
                    }

                    if selected_category in categories:
                        skills_list = categories[selected_category]
                        skills = self.resonatorSkills[resonator]
                        emojis = self.resonatorSkillsEmoji.get(resonator, {})
                        embed_color = EmbedColors.get(resonatorEmbedColors.get(resonator, {}).get('color', 'defaultColor'), 0x000000)

                        embed = discord.Embed(
                            title=f"{elementEmoji}  {weaponEmoji}  {starEmoji}  {selected_category}",
                            description="\n\n".join(
                                f"{emojis.get(skill, '❓')} **{skills[skill]['name']} - {skill}**\n{skills[skill]['description']}"
                                for skill in skills_list if skill in skills
                            ),
                                                 
                            color=embed_color
                        ).set_author(name=f"{resonator}", icon_url=f"https://raw.githubusercontent.com/krulciferikaru/Database/main/WutheringWavesAssets/CharacterIcons/{resonator.replace(' ', '_')}.png")
                        embed.set_thumbnail(url=f"https://raw.githubusercontent.com/krulciferikaru/Database/main/WutheringWavesAssets/CharacterIcons/{resonator.replace(' ', '_')}.png")

                        try:
                            await interaction.edit_original_response(embed=embed)
                        except Exception as e:
                            print(f"Error editing message: {e}")

                elif custom_id.startswith('skill_select_'):
                    selected_skill = interaction.data['values'][0]
                    skills = self.resonatorSkills[resonator]
                    emojis = self.resonatorSkillsEmoji.get(resonator, {})
                    embed_color = EmbedColors.get(resonatorEmbedColors.get(resonator, {}).get('color', 'defaultColor'), 0x000000)

                    if selected_skill in skills:
                        embed = discord.Embed(
                            title=f"{elementEmoji}  {weaponEmoji}  {starEmoji}  {selected_skill}",
                            description=(f"{emojis.get(selected_skill, '❓')} **{skills[selected_skill]['name']}**\n{skills[selected_skill]['description']}"),
                            color=embed_color
                        ).set_author(name=f"{resonator}", icon_url=f"https://raw.githubusercontent.com/krulciferikaru/Database/main/WutheringWavesAssets/CharacterIcons/{resonator.replace(' ', '_')}.png")
                        embed.set_thumbnail(url=f"https://raw.githubusercontent.com/krulciferikaru/Database/main/WutheringWavesAssets/CharacterIcons/{resonator.replace(' ', '_')}.png")

                        try:
                            await interaction.edit_original_response(embed=embed)
                        except Exception as e:
                            print(f"Error editing message: {e}")
                    else:
                        await interaction.followup.send(f"Skill '{selected_skill}' not found for Resonator '{resonator}'.", ephemeral=True)

async def setup(bot: commands.Bot):
    await bot.add_cog(ResonatorSkills(bot))
