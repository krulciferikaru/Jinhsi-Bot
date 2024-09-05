import discord
from discord.ext import commands
from discord.ui import View, Button
from discord import app_commands
from data.Emojis import Emojis
from data.EchoData import echoInfo

def sort_echoes(by):
    sorted_data = {}
    for effect, echoes in echoInfo['SonataEffects'].items():
        for name, attributes in echoes.items():
            sort_key = attributes.get(by)
            if sort_key not in sorted_data:
                sorted_data[sort_key] = []
            sorted_data[sort_key].append((name, effect, attributes))
    return sorted_data

def chunk_list(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

def remove_duplicates(echoes):
    seen = set()
    unique_echoes = []
    for name, effect, attributes in echoes:
        identifier = (name, attributes['cost'])
        if identifier not in seen:
            seen.add(identifier)
            unique_echoes.append((name, effect, attributes))
    return unique_echoes

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

class EchoList(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="echolist", description="List of echoes")
    @app_commands.choices(
        sort_by=[
            app_commands.Choice(name="Class", value="class"),
            app_commands.Choice(name="Cost", value="cost"),
            app_commands.Choice(name="Sonata Effect", value="sonataeffect"),
        ]
    )
    async def echolist(self, interaction: discord.Interaction, sort_by: str = "sonataeffect"):
        try:
            sorted_data = sort_echoes(sort_by)
            pages = []

            #Sonata Effects
            if sort_by == "sonataeffect":
                for effect, echoes in echoInfo['SonataEffects'].items():
                    sorted_echoes = list(echoes.items())  # Ensure it's a list
                    chunks = chunk_list(sorted_echoes, 20)  # Limit to 20 echoes per page

                    for chunk in chunks:
                        description = "\n".join(
                            f"`[{attributes['cost']}]` {Emojis['SonataEffects'].get(effect, '')} {Emojis[f'{attributes['cost']}Cost'].get(name, '')} `{name}`"
                            for name, attributes in chunk
                        )

                        title = f"{Emojis['SonataEffects'].get(effect, '')} {effect}"
                        embed = discord.Embed(
                            title=title,
                            description=description,
                            color=discord.Color.blue()
                        )
                        embed.set_author(name="Echo List")
                        pages.append(embed)
                    
            elif sort_by == "cost":
                for key, echoes in sorted_data.items():
                    echoes = remove_duplicates(echoes)  # Remove duplicates here
                    chunks = chunk_list(echoes, 20)  # Limit to 20 echoes per page

                    for chunk in chunks:
                        description = "\n".join(
                            f"`[{attributes['cost']}]` {Emojis.get(f'{attributes['cost']}Cost', {}).get(name, '')} `{name}`"
                            for name, attributes in chunk
                        )

                        icon = Emojis['Icons'].get(f"Cost{key}", "")
                        title = f"{icon} Cost {key}"

                        embed = discord.Embed(
                            title=title,
                            description=description,
                            color=discord.Color.blue()
                        )
                        embed.set_author(name="Echo List")
                        pages.append(embed)

            # Class
            elif sort_by == "class":
                for key, echoes in sorted_data.items():
                    echoes = remove_duplicates(echoes)  # Remove duplicates here
                    chunks = chunk_list(echoes, 20)  # Limit to 20 echoes per page

                    for chunk in chunks:
                        description = "\n".join(
                            f"`[{attributes['cost']}]` {Emojis.get(f'{attributes['cost']}Cost', {}).get(name, '')} `{name}`"
                            for name, attributes in chunk
                        )
                        icon = Emojis['Icons'].get("ClassIcon", "")
                        title = f"{icon} {key}"

                        embed = discord.Embed(
                            title=title,
                            description=description,
                            color=discord.Color.blue()
                        )
                        embed.set_author(name="Echo List")
                        pages.append(embed)


            if pages:
                view = Pagination(pages)
                embed = pages[0]
                embed.set_footer(text=f"Page 1/{len(pages)}")
                await interaction.response.send_message(embed=embed, view=view)
            else:
                await interaction.response.send_message("No echoes found.")
        except Exception as e:
            await interaction.response.send_message(f"An error occurred: {e}")

async def setup(bot: commands.Bot):
    await bot.add_cog(EchoList(bot))
