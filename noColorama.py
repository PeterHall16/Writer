import os

url = str(input("Enter url: "))
display = str(input("Display file? "))
file = open(url, "r")
if (display == "yes"):
	print(file.read())
	file.close()

print("Replace or Delete?")
choice = str(input()).lower()

if (choice == "replace"):
	replacement = str(input("Enter replacement text: "))
	file = open(url, "w")
	file.write(replacement)

	print(replacement)
if (choice == "delete"):
	os.remove(url)
	print("File removed.")
else:
	print("Please enter a valid response.")
