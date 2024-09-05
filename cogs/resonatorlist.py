import discord
from discord.ext import commands
from discord.ui import View, Button
from discord import app_commands
from data.Emojis import Emojis
from data.ResonatorInfo import resonatorInfo

def sort_resonators(by):
    sorted_data = {}
    for key, value in resonatorInfo.items():
        sort_keys = value[by] if isinstance(value[by], list) else [value[by]]
        for sort_key in sort_keys:
            if sort_key not in sorted_data:
                sorted_data[sort_key] = []
            sorted_data[sort_key].append(key)
    return sorted_data

def chunk_list(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

def keytext(key, sort_by=None):
    if key.startswith("<:") and key.endswith(">"):
        start_index = key.find(":") + 1
        end_index = key.rfind(":")
        return key[start_index:end_index]

    emoji = ""
    if sort_by == "element" and key in Emojis['ElementType']:
        emoji = Emojis['ElementType'][key]
    elif sort_by == "weapon" and key in Emojis['WeaponType']:
        emoji = Emojis['WeaponType'][key]
    elif sort_by == "sonataeffect" and key in Emojis['SonataEffects']:
        emoji = Emojis['SonataEffects'][key]

    return f"{emoji} {key}" if emoji else key

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

class ResonatorCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="resonatorlist", description="List of resonators")
    @app_commands.choices(
        sort_by=[
            app_commands.Choice(name="Element", value="element"),
            app_commands.Choice(name="Weapon", value="weapon"),
            app_commands.Choice(name="Star", value="star"),
        ]
    )
    async def resonatorlist(self, interaction: discord.Interaction, sort_by: str = "element"):
        try:
            sorted_data = sort_resonators(sort_by)

            pages = []
            for key, resonators in sorted_data.items():
                chunks = chunk_list(resonators, 20)
                for chunk in chunks:
                    description = "\n".join(
                        f"`{resonatorInfo[res]['star']}` "
                        f"{resonatorInfo[res]['weapon']} "
                        f"{resonatorInfo[res]['element']} "
                        f"{Emojis['ResonatorIcons'].get(res, '')} "
                        f"`{res}`"  
                        for res in chunk
                    )

                    if sort_by == "star":
                        title = f"{keytext(key, sort_by)}"
                    else:
                        title = f"{key} {keytext(key, sort_by)}"

                    embed = discord.Embed(
                        title=title,
                        description=description,
                        color=discord.Color.blue()
                    )
                    embed.set_author(name="Resonator List")
                    pages.append(embed)

            if pages:
                view = Pagination(pages)
                embed = pages[0]
                embed.set_footer(text=f"Page 1/{len(pages)}")
                await interaction.response.send_message(embed=embed, view=view)
            else:
                await interaction.response.send_message("No resonators found.")
        except Exception as e:
            await interaction.response.send_message(f"An error occurred: {e}")

async def setup(bot: commands.Bot):
    await bot.add_cog(ResonatorCog(bot))