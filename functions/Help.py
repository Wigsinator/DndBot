#help function
prefix = '$'

GENERAL = ("The DnD bot is here for a quick and easy reference to information found in the player's handbook." +'\n'+ 
			"*Created by Wigsinator*"+'\n'+'\n'+
			"__**Available commands are:**__" +'\n'+
			prefix+"class: Lists the abilities gained by a given class at a given level" +'\n'+
			prefix+"feature: Gives a description of an ability granted by a certain class **Not currently functioning**" +'\n'+
			prefix+"race: Lists the attributes of a given race **Not currently functioning**" +'\n'+'\n'+  
			"For more details on a particular command, use:" +'\n'+ 
			"`"+prefix+"help [command]`"
			)

CLASS = ("The class command lists the abilities gained by a given class at a given level"+'\n'+
		"Format:"+'\n'+
		"`"+prefix+"class [class] [level]`"
		)

FEATURE = "I'm working on it, cool ya jets"

def Help(function = 'general'):
	if function == 'general':
		return GENERAL
	if function == 'class':
		return CLASS
	if function == 'feature':
		return FEATURE