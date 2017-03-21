import xml.etree.ElementTree as ET

def Class(c,l):
	"""Takes a class and a level, and returns the abilities gained at that level"""

	tree = ET.parse('XMLs/Character Files/Classes 2.5.xml')
	root = tree.getroot()
	abilities = []

	for clas in root.findall('class'):
		name = clas.get('name')
		if c.lower() == name.lower():
			#print(name)
			for auto in clas.findall('autolevel'):
				level = auto.get('level')
				if level == l:
					#print('Level', lev, 'ability')
					for feature in auto.findall('feature'):
						ability = feature[0].text
						#print(ability)
						abilities.append(ability)
					break
			break
	output = '```' +'\n'+ name +'\n'+ level +'\n'+ '\n'.join(abilities) +'\n'+ '```'
	return output

