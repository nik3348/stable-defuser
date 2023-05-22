import discord
import os

from io import BytesIO
from defuse.unclip import generate
from dotenv import load_dotenv

load_dotenv()

bot = discord.Bot()


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.slash_command(description="Generate an image from a prompt")
async def imagine(ctx: discord.ApplicationContext, prompt: discord.Option(str)):
    await ctx.defer()
    b = BytesIO()
    generate(prompt).save(b, 'PNG')
    await ctx.send_followup(file=discord.File(fp=BytesIO(b.getvalue()), filename="image.jpg"))

bot.run(os.getenv("API_KEY"))
