import os
import sys
import subprocess
import hashlib

def theUserEnteredOneOfTheOptions(the_option):
    if the_option == "protect":
       return True
    if the_option == "unprotect":
       return True
    return False

# encrypts and sets permissions to owner ownly; removes the original file; results in a file like (test.txt.gpg)
def protectFile(file):
    md5sum_result = subprocess.run(["md5sum", file], stderr=subprocess.DEVNULL, text=True)
    if md5sum_result.returncode != 0:
       print("md5 hash for file failed! The file was tampered with.")
       sys.exit()
    else:
       print("Please copy the preceding md5 hash value for your file to check file integrity. It should be the same after unprotect is executed.")

    gpg_result = subprocess.run(["gpg", "-c", file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if gpg_result.returncode != 0:
       print("gpg passphrase encryption failed!")
       sys.exit()

    rm_result = subprocess.run(["rm", file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if rm_result.returncode != 0:
       print("removing the original file failed!")
       sys.exit()

    chmod_result = subprocess.run(["chmod", "700", file + ".gpg"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if chmod_result.returncode != 0:
       print("setting permissions to owner only on encrypted file failed!")
       sys.exit()
	
	############################################ This is the code that includes metadata in the hash
	password = input("Please give the password: ")
	to_hash = md5sum_result.stdout + os.stat(file) + password
	new_hash = hashlib.md5(new_hash.encode()).digest()
	f = open(file + "hash.txt", "w")
	f.write(new_hash)
	f.close()

# decrypts and sets permissions to owner only; removes a file like (test.txt.gpg); results in a file like (test.txt)
def unprotectFile(file):
    gpg_result = subprocess.run(["gpg", file + ".gpg"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if gpg_result.returncode != 0:
       print("gpg passphrase decryption failed!")
       sys.exit()

    md5sum_result = subprocess.run(["md5sum", file], stderr=subprocess.DEVNULL)
    if md5sum_result.returncode != 0:
       print("md5 hash for file failed!")
       sys.exit()
    else:
       print("Please compare your previously generated md5 hash with the preceding md5 hash. If they are NOT the same, then file contents have likely been compromised.")

    rm_result = subprocess.run(["rm", file + ".gpg"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if rm_result.returncode != 0:
       print("removing the encrypted file failed!")
       sys.exit()

    chmod_result = subprocess.run(["chmod", "700", file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if chmod_result.returncode != 0:
       print("setting permissions to owner only on decrypted file failed!")
       sys.exit()
	
	password = input("Please give the password: ")
	to_hash = md5sum_result.stdout + os.stat(file) + password
	new_hash = hashlib.md5(new_hash.encode()).digest()
	f = open(file + "hash.txt", "r")
	
	if f.read() != md5sum_result.stdout:
		print("If you typed in the password correctly, then this message means that the file has been tampered with!")
		sys.exit()
	
	f.close()
	
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

if option == "protect":
   print("What is the name of the file you want to protect?")
if option == "unprotect":
   print("What is the name of the file you want to unprotect? Please enter the original name of the file.")

file = input()

executeOption(option, file)