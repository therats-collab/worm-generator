# == Code by 21 rats#2113 | Worms by verenacafern#8203 == #
# Free to use, provided all derivatives are free & open source
# Appreciated but not required if you show me what you're using my code for owo


# == What The Heck is This? == #
# Right now? Not much. Soon it will link in with discord, and use the images
# pregenerated by wormgenerator.py to do cool things!


# === Imports === #

import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix="$")

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'[INFO] {bot.user} is connected to the following guild:\n'
        f'[INFO] {guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'[INFO] Guild Members:\n - {members}')

        
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')
        print("[WARN] The adminping command failed, user did not have the correct role.")
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to hell, aka the test server!'
    )
    print(
        f'[INFO] {member.name} joined the guild:\n'
        f'[INFO] {guild.name}(id: {guild.id})'
    )


@bot.command(name="ping", help="Responds with a random message. For checking if the bot is working.")
async def ping(ctx):
    random_messages = [
        'I declare you 99% valid.',
        'Do you ever just...scream into the void',
    ]

    response = random.choice(random_messages)
    await ctx.send(response)    
    print("[INFO] The ping command was used.")

@bot.command(name="adminping", help="Admin only ping.")
@commands.has_role('admin worm')
async def adminping(ctx):
    random_messages = [
        'henlo admin worm, you are admin',
        'this is just for testing admin worm perms',
    ]

    response = random.choice(random_messages)
    await ctx.send(response)
    print("[INFO] The admin ping command was used.")

bot.run(TOKEN)
