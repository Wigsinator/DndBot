import xml.etree.ElementTree as ET

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

output = '```' +'\n'+ name +'\n'+ lev +'\n'+ '\n'.join(abilities) +'\n'+ '```'
#print('```', name, lev, *abilities, '```', sep = '\n')

print(output)