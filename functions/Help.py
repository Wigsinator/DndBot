#help function
try:
	from functions.config import prefix
except:
	pass
try:
	from config import prefix
except:
	pass


GENERAL = ("The DnD bot is here for a quick and easy reference to information found in the player's handbook." +'\n'+ 
			"{i}Created by Wigsinator{i}"+'\n'+'\n'+
			"{u}{b}Available commands are:{b}{u}" +'\n'+'\n'+
			"{prefix}class{`}: Lists the abilities gained by a given class at a given level." +'\n'+
			"{prefix}feature{`}: Gives a description of an ability granted by a certain class. {b}Not currently functioning{b}" +'\n'+
			"{prefix}race{`}: Lists the attributes of a given race. {b}Not currently functioning{b}" +'\n'+'\n'+  
			"For more details on a particular command, use:" +'\n'+ 
			"{prefix}help [command]{`}"
			)

CLASS = ("The class command lists the abilities gained by a given class at a given level"+'\n'+
		"Format:"+'\n'+
		"{prefix}class [class] [level]{`}"
		)

FEATURE = "I'm working on it, cool ya jets"

ONLINE = {'i': "*", "b":"**", "u":"__", "prefix":"`"+prefix, "`":"`"}
OFFLINE = {'i': "", "b":"", "u":"", "prefix":"", "`":""}

def Help(function = 'general', online = True):
	if online:
		dic = ONLINE
	else:
		dic = OFFLINE
	if function == 'general':
		return GENERAL.format(**dic)
	if function == 'class':
		return CLASS.format(**dic)
	if function == 'feature':
		return FEATURE