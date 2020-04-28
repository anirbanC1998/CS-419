import os
import shutil
import sys

def userEnteredOptions(option):
	if option == "new":
		return True
	if option == "read":
		return True
	if option == "write":
		return True
	if option == "delete":
		return True
	if option == "exit":
		return True
	return False

def newFile(new_file):
	if os.path.exists(new_file):
		print("\n~File already exists.")
	else:
		print("\n~File created.")
		myFile = open(new_file,"w+")
		myFile.close()

def readFile(file_name):
	#Check if file exists
	try:
		myFile = open(file_name,"r")
		print("\n~Contents of \'",file_name,"\':")
		print(myFile.read())
		myFile.close()
	except FileNotFoundError:
		print("\n~File does not exist.")

def writeFile(file_name):
	try:
		myFile = open(file_name,"a")
		print("\n~Enter text to write: ")
		new_text = input()
		#Check if empty
		if os.stat(file_name).st_size == 0:
			myFile.write(new_text)
		else:
			myFile.write('\n' + new_text)
		myFile.close()
	except FileNotFoundError:
		print("\n~File does not exist.")
def deleteFile(file_name):
	if os.path.exists(file_name):
		os.remove(file_name)
		print("\n~File deleted.")
	else:
		print("\n~File does not exist.")

def executeOptions(option_ex,fileName_ex):
	if option_ex == "new":
		newFile(fileName_ex)
	if option_ex == "read":
		readFile(fileName_ex)
	if option_ex == "write":
		writeFile(fileName_ex)
	if option_ex == "delete":
		deleteFile(fileName_ex)

print("~File System~ \nEnter a command: {new, read, write, delete, exit}")
option = input()

if userEnteredOptions(option) == False:
	print("\n~Unknown option, try again.")
	sys.exit()

if option == "new":
	print("\n~Enter new file name:")
if option == "read":
	print("\n~Enter file name to read:")
if option == "write":
	print("\n~Enter file name to write to:")
if option == "delete":
	print("\n~Enter file name to delete:")
if option == "exit":
	sys.exit()

fileName = input()
if not fileName.endswith('.txt'):
	fileName = fileName+".txt"

executeOptions(option,fileName)


