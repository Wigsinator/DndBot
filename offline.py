from functions.Class import Class
from functions.Help import Help

while True:
	text = input("Give a command, or $ to stop..."+"\n").split()
	
	if text[0] == "$":
		break

	elif text[0] == 'class':
		print(Class(text[1],text[2], False))

	elif text[0] == 'help':
		if len(text) == 1:
			print(Help(online = False))
		else:
			print(Help(text[1], False))

print("Goodbye")