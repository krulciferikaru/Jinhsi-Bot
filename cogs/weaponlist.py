import discord
from discord.ext import commands
from discord.ui import View, Button
from discord import app_commands
from data.Emojis import Emojis
from data.WeaponData import weaponInfo

def sort_weapons(by):
    sorted_data = {}

    for weapon_type, weapon_data in weaponInfo.items():
        for weapon_name, attributes in weapon_data['details'].items():
            sort_key = attributes.get(by) if by != "weapon_type" else weapon_type

            if sort_key not in sorted_data:
                sorted_data[sort_key] = []
            sorted_data[sort_key].append((weapon_name, attributes['star'])) 
    
    for key in sorted_data:
        sorted_data[key].sort(key=lambda x: x[0])
        
    return sorted_data

def chunk_list(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

class Pagination(View):
    def __init__(self, pages: list):
        super().__init__()
        self.pages = pages
        self.current_page = 0

        self.add_item(PaginationButton(label="◀", style=discord.ButtonStyle.secondary, action="previous"))
        self.add_item(PaginationButton(label="▶", style=discord.ButtonStyle.secondary, action="next"))

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        return interaction.user is not None

    async def update_message(self, message: discord.Message):
        try:
            embed = self.pages[self.current_page]
            embed.set_footer(text=f"Page {self.current_page + 1}/{len(self.pages)}")
            await message.edit(embed=embed, view=self)
        except Exception as e:
            print(f"Failed to update message: {e}")

class PaginationButton(Button):
    def __init__(self, label: str, style: discord.ButtonStyle, action: str):
        super().__init__(label=label, style=style)
        self.action = action

    async def callback(self, interaction: discord.Interaction):
        view = self.view
        if self.action == "previous":
            view.current_page = (view.current_page - 1) % len(view.pages)
        elif self.action == "next":
            view.current_page = (view.current_page + 1) % len(view.pages)
        await view.update_message(interaction.message)
        await interaction.response.defer()

class WeaponCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="weaponlist", description="List of weapons")
    @app_commands.choices(
        sort_by=[
            app_commands.Choice(name="Weapon Type", value="weapon_type"),
            app_commands.Choice(name="Star", value="star"),
        ]
    )
    async def weaponlist(self, interaction: discord.Interaction, sort_by: str = "weapon_type"):
        try:
            sorted_data = sort_weapons(sort_by)

            pages = []
            for key, weapons in sorted_data.items():
                chunks = chunk_list(weapons, 20)
                for chunk in chunks:
                    description = ""
                    for weapon_name, weapon_star in chunk:
                        star_rating = weapon_star  
                        weapon_type = None
                        for w_type, w_data in weaponInfo.items():
                            if weapon_name in w_data['details']:
                                weapon_type = w_type
                                break

                        # Get emoji for weapon
                        emoji = Emojis.get(star_rating, {}).get(weapon_type.lower(), {}).get(weapon_name, '')

                        description += f"`{weapon_star}` {emoji} `{weapon_name}`\n"
                    
                    if sort_by == "star":
                        title = f"{key}" 
                    elif sort_by == "weapon_type":
                        # Ensure Emojis['WeaponType'] exists and is correct
                        emoji = Emojis.get('WeaponType', {}).get(key.lower(), '')
                        title = f"{emoji} {key}"

                    embed = discord.Embed(
                        title=title,
                        description=description,
                        color=discord.Color.blue()
                    )
                    embed.set_author(name="Weapon List")
                    pages.append(embed)

            if pages:
                view = Pagination(pages)
                embed = pages[0]
                embed.set_footer(text=f"Page 1/{len(pages)}")
                await interaction.response.send_message(embed=embed, view=view)
            else:
                await interaction.response.send_message("No weapons found.")
        except Exception as e:
            await interaction.response.send_message(f"An error occurred: {e}")

async def setup(bot: commands.Bot):
    await bot.add_cog(WeaponCog(bot))