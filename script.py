import os
import sys

def theUserEnteredOneOfTheOptions(the_option):
   if the_option == "protect":
      return True
   if the_option == "unprotect":
      return True
   return False

"""encrypts and sets permissions to owner ownly; removes the original file; results in a file like (test.txt.gpg)"""
def protectFile(file):
   os.system("gpg -c" + " " + file)
   os.system("rm" + " " + file)
   os.system("chmod 700" + " " + file + ".gpg")

"""decrypts and sets permissions to owner only; removes a file like (test.txt.gpg); results in a file like (test.txt)"""
def unprotectFile(file):
   os.system("gpg" + " " + file + ".gpg")
   os.system("rm" + " " + file + ".gpg")
   os.system("chmod 700" + " " + file)

def executeOption(ex_option, ex_file):
   if ex_option == "protect":
      protectFile(ex_file)
   if ex_option == "unprotect":
      unprotectFile(ex_file)

print("Type one of the following options: protect, unprotect")

option = input()

if theUserEnteredOneOfTheOptions(option) == False:
   print("You did not enter one of the options!")
   sys.exit()

print("What is the name of the file you want to:" + " " + option)

file = input()

executeOption(option, file)
