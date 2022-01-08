import discord
from discord.ext import commands
import Selector

class AssistentBot(discord.Client):

    async def on_ready(self):
        print("a")

    async def on_message(self):
        pass
