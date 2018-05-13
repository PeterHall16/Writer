import os
# Import Colorama library (https://github.com/tartley/colorama)
from colorama import init
init()
from colorama import Fore, Back, Style
print(Style.RESET_ALL)


url = str(input("Enter url: "))
display = str(input("Display file? "))
file = open(url, "r")
if (display == "yes"):
	print(file.read())
	file.close()

print(Style.BRIGHT + Fore.GREEN + "Replace" ,Style.RESET_ALL + "or",Style.BRIGHT + Fore.RED + "Delete?", Style.RESET_ALL )
choice = str(input()).lower()

if (choice == "replace"):
	replacement = str(input("Enter replacement text: "))
	file = open(url, "w")
	file.write(replacement)

	print(Fore.CYAN + Style.BRIGHT + replacement)
if (choice == "delete"):
	os.remove(url)
	print(Fore.CYAN + Style.BRIGHT + "File removed.")
else:
	print("Please enter a valid response.")
