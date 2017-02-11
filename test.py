import discord
import asyncio
import xml.etree.ElementTree as ET

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
    
	elif message.content.startswith('*class'):
		tree = ET.parse('XMLs/Character Files/Classes 2.5.xml')
		root = tree.getroot()

		search = 'Barbarian'
		level = '1'
		abilities = []


		for clas in root.findall('class'):
			name = clas.get('name')
			if search == name:
				#print(name)
				for auto in clas.findall('autolevel'):
					lev = auto.get('level')
					if lev == level:
						#print('Level', lev, 'ability')
						for feature in auto.findall('feature'):
							ability = feature.get('name')
							#print(ability)
							abilities.append(ability)
						break
				break
		
		#print('```', name, lev, *abilities, '```', sep = '\n')
		output = '```' +'\n'+ name +'\n'+ lev +'\n'+ '\n'.join(abilities) +'\n'+ '```'
		await client.send_message(message.channel, output)


client.run('Mjc5NzA3MTI4NDQ3MzY5MjI1.C4A0ew.imNroIewdBK6uDysddZu-pmY-48')
