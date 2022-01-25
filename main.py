import discord
import os
from dotenv import load_dotenv

load_dotenv('.env')

client = discord.Client()

@client.event
async def on_ready():
    print('Logged into {1} as {0.user}'.format(client, "XXXSERVER"))

client.run(os.getenv('TOKEN'))