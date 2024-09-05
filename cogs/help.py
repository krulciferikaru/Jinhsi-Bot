import discord
from discord.ext import commands
from discord import app_commands
import asyncio

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Help cog loaded.")

    class HelpView(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=60)
            self.add_item(self.HelpSelect())

        class HelpSelect(discord.ui.Select):
            def __init__(self):
                options = [
                    discord.SelectOption(label="Main", description="Home Page"),
                    discord.SelectOption(label="Information", description="Information Page")
                ]
                super().__init__(placeholder="Category View", min_values=1, max_values=1, options=options)

            async def callback(self, interaction: discord.Interaction):
                if self.values[0] == "Main":
                    embed = HelpCog.embedMainPage()
                elif self.values[0] == "Information":
                    embed = HelpCog.embedInformationPage()
                else:
                    embed = discord.Embed(title="Error", description="Invalid selection.", color=0xff0000)
                
                # Update the message with the new embed and keep the view
                await interaction.response.edit_message(embed=embed, view=self.view)

    @staticmethod
    def embedMainPage():
        emb = discord.Embed(title="🗂️ Main Help", color=0xf2f2f2)
        emb.add_field(name='', value='An information bot for **Wuthering Waves**.\n'
                                     'Inspired by **Cogs Bot**.\n\n'
                                     'Use slash commands to start using this bot.\n'
                                     'Use the dropdown menu to view other commands by category\n', inline=False)
        emb.add_field(name='Changelog', value='```Added Zhezhi Build\nAdded Zhezhi & Xiangli Yao Weapon```', inline=False)

        emb.set_footer(text='Made by krulciferr', icon_url='https://cdn.discordapp.com/avatars/651246582150201345/00c44c51ef208cff88b625c3bc4d6cf6.png?size=4096')
        emb.set_author(name="Jinhsi Bot#1616", icon_url="https://cdn.discordapp.com/avatars/1252690441896460389/93f3c99d8711c7dadca8e1526492ea91.png?size=1024")
        return emb

    @staticmethod
    def embedInformationPage():
        emb = discord.Embed(title=":brain: Information Help", color=0xf2f2f2)
        emb.add_field(name='**/build**', value='Shows a resonator\'s build information.', inline=False)
        emb.add_field(name='**/echo**', value='Shows echo information.', inline=False)
        emb.add_field(name='**/weapon**', value='Shows weapon information.', inline=False)
        emb.add_field(name='**/skill**', value='Shows a resonator skills.', inline=False)
        emb.add_field(name='**/resonatorlist**', value='List of all resonators.', inline=False)
        emb.add_field(name='**/echolist**', value='List of all echoes.', inline=False)
        emb.add_field(name='**/weaponlist**', value='Lists of all weapons.', inline=False)
        emb.set_footer(text='Made by krulciferr', icon_url='https://cdn.discordapp.com/avatars/651246582150201345/00c44c51ef208cff88b625c3bc4d6cf6.png?size=4096')
        emb.set_author(name="Jinhsi Bot#1616", icon_url="https://cdn.discordapp.com/avatars/1252690441896460389/93f3c99d8711c7dadca8e1526492ea91.png?size=1024")
        return emb

    @app_commands.command(name="help", description="Displays all available bot commands")
    async def help(self, interaction: discord.Interaction):
        embed = self.embedMainPage()
        view = self.HelpView()
        # Ensure message is saved correctly
        message = await interaction.response.send_message(embed=embed, view=view)
        self.bot.loop.create_task(self.removeDropdown(message))

async def setup(bot: commands.Bot):
    await bot.add_cog(HelpCog(bot))
