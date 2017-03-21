from functions.Class import Class
from functions.Help import HelpOffline as Help

while True:
	text = input("Give a command, or $ to stop..."+"\n").split()
	
	if text[0] == "$":
		break

	elif text[0] == 'class':
		print(Class(text[1],text[2]))

	elif text[0] == 'help':
		if len(text) == 1:
			print(Help())
		else:
			print(Help(text[1]))

print("Goodbye")