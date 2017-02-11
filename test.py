import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

@client.event
async def on_message(message):
	if message.content.startswith('*ping'):
		await client.send_message(message.channel, 'Pong!')
	elif message.content.startswith('*sleep'):
		await asyncio.sleep(5)
		await client.send_message(message.channel, 'Done sleeping')
	elif

client.run('Mjc5NzA3MTI4NDQ3MzY5MjI1.C3-xEg.Y-eE6T8HtbILiIDe0BvE2few87k')
