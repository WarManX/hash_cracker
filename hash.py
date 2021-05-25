#!/usr/bin/python
import sys
import signal
import os
import time
import socket
import hashlib

# Console colors
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray

#def check_root():
#	if not os.geteuid() == 0:
#		print("Run as root.")
#		exit(1)
#main
def start(htype):
	logo1()
	print (B + '[' + P + '*' + B + '] ' + P + 'You have selected ' + G + htype + P + ' hashes type')
	print (B + '\n[' + P + '*' + B + '] ' + GR + 'Decrypt Menu:')
	print (B + '[' + P + '*' + B + '] ' + P + 'Press 1 for ' + GR + 'Hashes file')
	print(B + '[' + P + '*' + B + '] ' + P + 'Press 2 for ' + GR + 'One hash')
	print (B + '\n[' + P + '*' + B + '] ' + GR + 'Encrypt Menu:')
	print(B + '[' + P + '*' + B + '] ' + P + 'Press 3 to ' + GR + 'Encrypt to hash')
	print(B + '\n[' + P + '*' + B + '] ' + P + 'Press 0 for ' + GR + 'hashes menu')
	os = input(B + '\n[' + P + '*' + B + '] ' + GR)
	if os == "1":
		hashcracker1(htype)
	elif os == "2":
		hashcracker2(htype)
	elif os == "3":
		converterh(htype)
	elif os == "0":
		hashtype()
	else:
		print(B + '\n[' + P + '*' + B + '] ' + R + 'Wrong Number, please try again.')
		time.sleep(2)
		start(htype)


def hashtype():
	logo1()
	print (B + '\n[' + P + '*' + B + '] ' + P + 'Press 1 for ' + GR + 'MD5    Hashes')
	print(B + '[' + P + '*' + B + '] ' + P + 'Press 2 for ' + GR + 'SHA1   Hashes')
	print(B + '[' + P + '*' + B + '] ' + P + 'Press 3 for ' + GR + 'SHA224 Hashes')
	print(B + '[' + P + '*' + B + '] ' + P + 'Press 4 for ' + GR + 'SHA256 Hashes')
	print(B + '[' + P + '*' + B + '] ' + P + 'Press 5 for ' + GR + 'SHA384 Hashes')
	print(B + '[' + P + '*' + B + '] ' + P + 'Press 6 for ' + GR + 'SHA512 Hashes')
	print(B + '[' + P + '*' + B + '] ' + P + 'Press 7 for ' + GR + 'All    Hashes')
	print(B + '[' + P + '*' + B + '] ' + P + 'Press 0 to ' + GR + 'Exit')
	hhtype = input(B + '\n[' + P + '*' + B + '] ' + GR)
	if hhtype == "1":
		htype = 'md5'
		start(htype)
	elif hhtype == "2":
		htype = 'sha1'
		start(htype)
	elif hhtype == "3":
		htype = 'sha224'
		start(htype)
	elif hhtype == "4":
		htype = 'sha256'
		start(htype)
	elif hhtype == "5":
		htype = 'sha384'
		start(htype)
	elif hhtype == "6":
		htype = 'sha512'
		start(htype)
	elif hhtype == "7":
		alltypes()
	elif hhtype == "0":
		quiting()
		exit()
	else:
		print(B + '\n[' + P + '*' + B + '] ' + R + 'Wrong Number, please try again.')
		time.sleep(2)
		hashtype()


def alltypes():
	logo1()
	print (B + '[' + P + '*' + B + '] ' + P + 'Press 1 for ' + GR + 'Hashes file')
	print(B + '[' + P + '*' + B + '] ' + P + 'Press 2 for ' + GR + 'One hash')
	print(B + '\n[' + P + '*' + B + '] ' + P + 'Press 0 for ' + GR + 'hashes menu')
	hhtype = input(B + '\n[' + P + '*' + B + '] ' + GR)
	if hhtype == "1":
		allhashes2()
	elif hhtype == "2":
		allhashes1()
	elif hhtype == "0":
		hashtype()
	else:
		print(B + '\n[' + P + '*' + B + '] ' + R + 'Wrong Number, please try again.')
		time.sleep(2)
		alltypes()


def converterh(htype):
	logo1()
	print (B + '[' + P + '*' + B + '] ' + P + 'You have selected ' + G + htype + P + ' hashes type')
	text = input(B + '\n[' + P + '*' + B + '] ' + P + 'Enter text to encode: ' + GR )

	if htype == 'md5':
		hash_object = (hashlib.md5(text.encode())).hexdigest()
	elif htype == 'sha1':
		hash_object = (hashlib.sha1(text.encode())).hexdigest()
	elif htype == 'sha224':
		hash_object = (hashlib.sha224(text.encode())).hexdigest()
	elif htype == 'sha256':
		hash_object = (hashlib.sha256(text.encode())).hexdigest()
	elif htype == 'sha384':
		hash_object = (hashlib.sha384(text.encode())).hexdigest()
	elif htype == 'sha512':
		hash_object = (hashlib.sha512(text.encode())).hexdigest()
	else:
		print(B + '[' + P + '*' + B + '] ' + R + 'Error, No Hash type selected!!!')
		time.sleep(2)
		hashtype()

	print(B + '\n[' + P + '*' + B + '] ' + P + 'Your Text: ' + G + text )
	print(B + '[' + P + '*' + B + '] ' + P + 'Your Hash: ' + G + hash_object )

	again = input(B + '\n[' + P + '*' + B + '] ' + P + 'Do you want to run again?:(y/n) ' + GR)
	if again == 'y' or again == 'Y':
		converterh(htype)
	else:
		hashtype()

#Function to handle Crtl+C
def signal_handler(signal, frame):
	print(B + '\n[' + P + '*' + B + ']' + P + ' Exiting the tool, Thanks for using the tool')
	time.sleep(1)
	quiting()
	os.system("kill -9 " + str(os.getpid()))
	sys.exit(1)

def signal_exit(signal, frame):
	print( "Signal exit")
	sys.exit(1)


def allhashes1():
	pass_hash1 = input(B + '\n[' + P + '*' + B + '] ' + P + 'Enter hash: ' + GR)
	wordlist1 = input(B + '[' + P + '*' + B + '] ' + P + 'Enter wordlist file path: ' + GR)
	print(B + '[' + P + '*' + B + '] ' + P + 'To stop the loop press' + O + ' CTRL+C\n')

	pass_hash = pass_hash1.replace(" ","")
	wordlist = wordlist1.replace(" ","")

	try:
		pass_file = open(wordlist, "r")
	except:
		print(B + '[' + P + '*' + B + '] ' + R + 'Error, No File found for the wordlist')
		time.sleep(2)
		allhashes1()

	flag = 0
	counter = 0
	for word in pass_file:
		enc_word = word.encode('utf-8')
		digest1 = hashlib.md5(enc_word.strip()).hexdigest()
		digest2 = hashlib.sha1(enc_word.strip()).hexdigest()
		digest3 = hashlib.sha224(enc_word.strip()).hexdigest()
		digest4 = hashlib.sha256(enc_word.strip()).hexdigest()
		digest5 = hashlib.sha384(enc_word.strip()).hexdigest()
		digest6 = hashlib.sha512(enc_word.strip()).hexdigest()

		counter += 1
		typeh = ""
		if digest1 == pass_hash:
			typeh = "md5"
		elif digest2 == pass_hash:
			typeh = "sha1"
		elif digest3 == pass_hash:
			typeh = "sha224"
		elif digest4 == pass_hash:
			typeh = "sha256"
		elif digest5 == pass_hash:
			typeh = "sha384"
		elif digest6 == pass_hash:
			typeh = "sha512"

		if digest1 == pass_hash or digest2 == pass_hash or digest3 == pass_hash or digest4 == pass_hash or digest5 == pass_hash or digest6 == pass_hash:
			print(B + '[' + P + '*' + B + '] ' + G + 'Password Found!!')
			print(B + '[' + P + '*' + B + '] ' + P + 'Hash type is: ' + G + typeh)
			print(B + '[' + P + '*' + B + '] ' + P + 'Your password is: ' + G + word + P + ' -- ' + G + pass_hash)
			flag = 1
			time.sleep(0.1)
			break
		else:
			continue

	if flag == 0:
		print(B + '[' + P + '*' + B + '] ' + R + 'No Password found from wordlist')
	print(B + '\n[' + P + '*' + B + '] ' + P + 'You have tried ' + G + str(counter) + P + " Passwords")
	counter = 0
	again = input(B + '[' + P + '*' + B + '] ' + P + 'Do you want to run again?:(y/n) ' + GR)
	if again == 'y' or again == 'Y':
		allhashes1()
	else:
		alltypes()


def allhashes2():
	pass_hash1 = input(B + '\n[' + P + '*' + B + '] ' + P + 'Enter hashes file path: ' + GR)
	wordlist1 = input(B + '[' + P + '*' + B + '] ' + P + 'Enter wordlist file path: ' + GR)
	print(B + '[' + P + '*' + B + '] ' + P + 'To stop the loop press' + O + ' CTRL+C\n')

	pass_hash = pass_hash1.replace(" ","")
	wordlist = wordlist1.replace(" ","")

	try:
		pass_file = open(wordlist, "r")
	except:
		print(B + '[' + P + '*' + B + '] ' + R + 'Error, No File found for the wordlist')
		time.sleep(2)
		allhashes2()

	try:
		hash_file = open(pass_hash, "r")
		hash_read = hash_file.readlines()
	except:
		print(B + '[' + P + '*' + B + '] ' + R + 'Error, No File found for the hashes file')
		time.sleep(2)
		allhashes2()

	flag = 0
	counter = 0
	for word in pass_file:
		for hashed in hash_read:
			enc_word = word.encode('utf-8')
			digest1 = hashlib.md5(enc_word.strip()).hexdigest()
			digest2 = hashlib.sha1(enc_word.strip()).hexdigest()
			digest3 = hashlib.sha224(enc_word.strip()).hexdigest()
			digest4 = hashlib.sha256(enc_word.strip()).hexdigest()
			digest5 = hashlib.sha384(enc_word.strip()).hexdigest()
			digest6 = hashlib.sha512(enc_word.strip()).hexdigest()

			typeh = ""
			hashed_wrd = hashed.strip()

			if digest1 == hashed_wrd:
				typeh = "md5"
			elif digest2 == hashed_wrd:
				typeh = "sha1"
			elif digest3 == hashed_wrd:
				typeh = "sha224"
			elif digest4 == hashed_wrd:
				typeh = "sha256"
			elif digest5 == hashed_wrd:
				typeh = "sha384"
			elif digest6 == hashed_wrd:
				typeh = "sha512"

			if digest1 == hashed_wrd or digest2 == hashed_wrd or digest3 == hashed_wrd or digest4 == hashed_wrd or digest5 == hashed_wrd or digest6 == hashed_wrd:
				print(B + '\n[' + P + '*' + B + '] ' + G + 'Password Found!!')
				print(B + '[' + P + '*' + B + '] ' + P + 'Hash type is: ' + G + typeh)
				print(B + '[' + P + '*' + B + '] ' + P + 'Your password is: ' + G + word + P + ' -- ' + G + hashed_wrd)
				flag = 1
				time.sleep(0.1)
				continue
		counter += 1

	if flag == 0:
		print(B + '[' + P + '*' + B + '] ' + R + 'No Password found from wordlist')
	print(B + '\n[' + P + '*' + B + '] ' + P + 'You have tried ' + G + str(counter) + P + " Passwords")
	counter = 0
	again = input(B + '[' + P + '*' + B + '] ' + P + 'Do you want to run again?:(y/n) ' + GR)
	if again == 'y' or again == 'Y':
		allhashes2()
	else:
		alltypes()


def hashcracker1(htype):
	counter = 0
	flag = 0
	pass_hash1 = input(B + '\n[' + P + '*' + B + '] ' + P + 'Enter ' + G + htype + P + ' hashes file path: ' + GR)
	wordlist1 = input(B + '[' + P + '*' + B + '] ' + P + 'Enter wordlist file path: ' + GR)
	print(B + '[' + P + '*' + B + '] ' + P + 'To stop the loop press' + O + ' CTRL+C\n')

	pass_hash = pass_hash1.replace(" ","")
	wordlist = wordlist1.replace(" ","")

	try:
		pass_file = open(wordlist, "r")
	except:
		print(B + '[' + P + '*' + B + '] ' + R + 'Error, No File found for the wordlist')
		time.sleep(2)
		hashcracker1(htype)

	try:
		hash_file = open(pass_hash, "r")
		hash_read = hash_file.readlines()
	except:
		print(B + '[' + P + '*' + B + '] ' + R + 'Error, No File found for the hashes file')
		time.sleep(2)
		hashcracker1(htype)

	for word in pass_file:
		for hashed in hash_read:
			enc_word = word.encode('utf-8')
			if htype == 'md5':
				digest = hashlib.md5(enc_word.strip()).hexdigest()
			elif htype == 'sha1':
				digest = hashlib.sha1(enc_word.strip()).hexdigest()
			elif htype == 'sha224':
				digest = hashlib.sha224(enc_word.strip()).hexdigest()
			elif htype == 'sha256':
				digest = hashlib.sha256(enc_word.strip()).hexdigest()
			elif htype == 'sha384':
				digest = hashlib.sha384(enc_word.strip()).hexdigest()
			elif htype == 'sha512':
				digest = hashlib.sha512(enc_word.strip()).hexdigest()
			else:
				print(B + '[' + P + '*' + B + '] ' + R + 'Error, No Hash type selected!!!')
				time.sleep(2)
				hashtype()
		
			hashed_wrd = hashed.strip()

			if digest == hashed_wrd:
				print(B + '[' + P + '*' + B + '] ' + G + 'Password Found!!')
				print(B + '[' + P + '*' + B + '] ' + P + 'Your password is: ' + G + word + P + ' -- ' + G + hashed_wrd + '\n')
				flag = 1
				time.sleep(0.1)
				continue
		counter += 1

	if flag == 0:
		print(B + '[' + P + '*' + B + '] ' + R + 'No Password found from wordlist')
		time.sleep(0.1)

	print(B + '\n[' + P + '*' + B + '] ' + P + 'You have tried ' + G + str(counter) + P + " Passwords")
	counter = 0

	again = input(B + '[' + P + '*' + B + '] ' + P + 'Do you want to run again?:(y/n) ' + GR)
	if again == 'y' or again == 'Y':
		hashcracker1(htype)
	else:
		hashtype()

def hashcracker2(htype):
	counter = 0
	flag = 0
	pass_hash1 = input(B + '\n[' + P + '*' + B + '] ' + P + 'Enter ' + G + htype + P + ': ' + GR)
	wordlist1 = input(B + '[' + P + '*' + B + '] ' + P + 'Enter wordlist file path: ' + GR)
	print(B + '[' + P + '*' + B + '] ' + P + 'To stop the loop press' + O + ' CTRL+C\n')

	pass_hash = pass_hash1.replace(" ","")
	wordlist = wordlist1.replace(" ","")

	try:
		pass_file = open(wordlist, "r")
	except:
		print(B + '[' + P + '*' + B + '] ' + R + 'Error, No File found for the wordlist')
		time.sleep(2)
		hashcracker2(htype)

	for word in pass_file:
		enc_word = word.encode('utf-8')
		if htype == 'md5':
			digest = hashlib.md5(enc_word.strip()).hexdigest()
		elif htype == 'sha1':
			digest = hashlib.sha1(enc_word.strip()).hexdigest()
		elif htype == 'sha224':
			digest = hashlib.sha224(enc_word.strip()).hexdigest()
		elif htype == 'sha256':
			digest = hashlib.sha256(enc_word.strip()).hexdigest()
		elif htype == 'sha384':
			digest = hashlib.sha384(enc_word.strip()).hexdigest()
		elif htype == 'sha512':
			digest = hashlib.sha512(enc_word.strip()).hexdigest()
		else:
			print(B + '[' + P + '*' + B + '] ' + R + 'Error, No Hash type selected!!!')
			time.sleep(2)
			hashtype()

		counter += 1

		if digest == pass_hash:
			print(B + '[' + P + '*' + B + '] ' + G + 'Password Found!!')
			print(B + '[' + P + '*' + B + '] ' + P + 'Your password is: ' + G + word + P + ' -- ' + G + pass_hash)
			flag = 1
			time.sleep(0.1)
			break
	if flag == 0:
		print(B + '[' + P + '*' + B + '] ' + R + 'No Password found from wordlist')

	print(B + '\n[' + P + '*' + B + '] ' + P + 'You have tried ' + G + str(counter) + P + " Passwords")
	counter = 0

	again = input(B + '[' + P + '*' + B + '] ' + P + 'Do you want to run again?:(y/n) ' + GR)
	if again == 'y' or again == 'Y':
		hashcracker2(htype)
	else:
		hashtype()

def logo1():
    os.system("clear")
    print(P + "          _____   ")
    print("        /  ___  \ ")
    print("      /  /  _  \  \ ")
    print("    /( /( /(_)\ )\ )\ ")
    print("   (  \  \ ___ /  /  ) ")
    print("   (    \ _____ /    ) ")
    print("   /(               )\   " + O + 'This tool can be used' + P)
    print("  |  \             /  |  " + O + 'for multiple hashes!!' + P)
    print("  |    \ _______ /    | ")
    print("   \    / \   / \    / ")
    print("     \/    | |    \/ ")
    print("           | |  ")
    print("           | | ")
    print("           | | ")
    print(" _   _    __    ___  _   _ ")
    print("( )_( )  /__\  / __)( )_( )")
    print(" ) _ (  /(__)\ \__ \ ) _ ( ")
    print("(_) (_)(__)(__)(___/(_) (_)")
    print()

def quiting():
    os.system("clear")
    print(P + "          _____   ")
    print("        /  ___  \ ")
    print("      /  /  _  \  \ ")
    print("    /( /( /(_)\ )\ )\ ")
    print("   (  \  \ ___ /  /  ) ")
    print("   (    \ _____ /    ) ")
    print("   /(               )\   " + O + 'Thank you for using the tool' + P)
    print("  |  \             /  |  " + O + 'https://github.com/ShyGorilla' + P)
    print("  |    \ _______ /    | ")
    print("   \    / \   / \    / ")
    print("     \/    | |    \/ ")
    print("           | |  ")
    print("           | | ")
    print("           | | ")
    print(" _   _    __    ___  _   _ ")
    print("( )_( )  /__\  / __)( )_( )")
    print(" ) _ (  /(__)\ \__ \ ) _ ( ")
    print("(_) (_)(__)(__)(___/(_) (_)")
    print()

if __name__ == "__main__":
	signal.signal(signal.SIGINT, signal_handler)
	#check_root()
	hashtype()