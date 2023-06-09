import discord
from discord.ext import commands as cmds
from dotenv import load_dotenv
import random as rand
import os

load_dotenv()

class Mention(cmds.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cmds.hybrid_command(description="simply sends the text to a member")
    async def mention(self, ctx, text: str, to: discord.Member = None):
        if to is None:
            to = rand.choice(ctx.guild.members)
        
        await ctx.send(f"> {ctx.author.mention} wanted to tell {to.mention} that '{text}'")

async def setup(bot):
    await bot.add_cog(Mention(bot))