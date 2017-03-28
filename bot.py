import discord
import asyncio
import xml.etree.ElementTree as ET
from functions.Class import Class
from functions.Help import Help
from functions.config import prefix, game

client = discord.Client()


@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
	await client.change_presence(game=game)

@client.event
async def on_message(message):

	if message.content.startswith(prefix+'ping'):
		await client.send_message(message.channel, 'Pong!')

	elif message.content.startswith(prefix+'kill'):
		if message.author.id == '90455370073391104':
			await client.send_message(message.channel, 'Goodbye!')
			await client.logout()

	elif message.content.startswith(prefix+'sleep'):
		await asyncio.sleep(5)
		await client.send_message(message.channel, 'Done sleeping')

	elif message.content.startswith(prefix+'class'):
		text = message.content.split()
		search = text[1]
		level = text[2]
		
		output = Class(search, level)

		await client.send_message(message.channel, output)

	elif message.content.startswith(prefix+'help'):
		text = message.content.split()
		if len(text) == 1:
			output = Help()
		else:
			output = Help(text[1])
		await client.send_message(message.channel, output)


client.run('Mjc5NzA3MTI4NDQ3MzY5MjI1.C4A0ew.imNroIewdBK6uDysddZu-pmY-48')