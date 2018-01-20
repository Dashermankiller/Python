"""" Functions

def Menu():
    print("1. Encrypted Text")
    print("2. Send SMS")
    print("3. Quit")
selection = int(input("Enter an Option:"))
if selection == 1:
    good()
elif selection == 2:
    bad()
elif selection == 3:
	exit
else:
	print("Invalid Option. Enter 1-3")
	Menu()
"""	

from sys import exit
import os
from psk2 import passwd
from psk2 import Email
#from server_ftps import server
#from server_ftps import RetrFile
import sys
import BeautifulSoup
import base64
import os
from googlevoice import Voice
from googlevoice.util import input
def Menu():
    os.system('cls')
    print("1. Encrypted Text")
    print("2. Decrypt TEXT")
    print("3. Send SMS")
    print("4. wget")
    print("5. cmd")
    print("6. SFTP server")
    while True:
		try:
			menu = int(input("Enter your Choice: "))
			os.system('cls')
			if menu ==1:
				bad()
				break
			elif menu ==3:
				SMS()
				break
			elif menu ==2:
				Dc()
				break
			elif menu ==4:
				wget()
			elif menu ==5:
				cmd()
			elif menu ==6:
				RetrFile()
			elif menu == 7:
				break
			else:
				print ("Invalid")
				Menu()
		except ValueError:
			Menu()
			print ("Invalid Choice Enetr 1-4")
    exit		
def SMS():
	while True:
		os.system('cls')
		n = raw_input("Please enter 'pass':")
		os.system('cls')
		if n.strip() == 'Dasher':
		 break
	voice = Voice()
	voice.login(Email,passwd)
	number = "6467449809"
	Ammi = "3477530782"
	print ("1. Ammi")
	print ("2. user")
	print ("3. show text")
	phoneNumber = input('Enter your number : ')
	os.system('cls')
	phoneNumber = int(phoneNumber)
	def extractsms(htmlsms) :

		msgitems = []                                                                               
		tree = BeautifulSoup.BeautifulSoup(htmlsms)                
		conversations = tree.findAll("div",attrs={"id" : True},recursive=False)
		for conversation in conversations :
			
			rows = conversation.findAll(attrs={"class" : "gc-message-sms-row"})
			for row in rows :                                                              
				
				msgitem = {"id" : conversation["id"]}               
				spans = row.findAll("span",attrs={"class" : True}, recursive=False)
				for span in spans :                                                 
					cl = span["class"].replace('gc-message-sms-', '')
					msgitem[cl] = (" ".join(span.findAll(text=True))).strip()       
				msgitems.append(msgitem)                                    
		return msgitems
	voice = Voice()
	voice.login(Email, passwd)
	voice.sms()
	for msg in extractsms(voice.sms.html):
		print (str(msg))
		

	text = raw_input ('enter the text: ')
	os.system('cls')

	key = 'abcdefghijklmnopqrstuvwxyz'
	key2 = '123456789'
	def encrypt(n, plaintext):
		"""Encrypt the string and return the ciphertext"""
		result = ''

		for l in plaintext.lower():
			try:
				i = (key.index(l) + n) % 26
				result += key[i]
			except ValueError:
				result += l

		return result.lower()

	def decrypt(n, ciphertext):
		"""Decrypt the string and return the plaintext"""
		result = ''

		for l in ciphertext:
			try:
				i = (key.index(l) - n) % 26
				result += key[i]
			except ValueError:
				result += l

		return result
	if phoneNumber  == 1:
		phoneNumber = (Ammi)
	elif phoneNumber == 2:
		phoneNumber = (number)
	offset = 5
	encode = base64.b64encode(encrypt(offset, text))
	decode = base64.b64decode(encode)
	decrypted = decrypt(offset, decode)
	voice.send_sms(phoneNumber, decrypted)
	print "Your TEXT: " + text
	print "OK"
	anykey= raw_input("Enter anything to return to man menu: ")
	os.system('cls')
	Menu()
def bad():
	key = 'abcdefghijklmnopqrstuvwxyz'
	key2 = '123456789'
	def encrypt(n, plaintext):
		"""Encrypt the string and return the ciphertext"""
		result = ''

		for l in plaintext.lower():
			try:
				i = (key.index(l) + n) % 26
				result += key[i]
			except ValueError:
				result += l

		return result.lower()

	def decrypt(n, ciphertext):
		"""Decrypt the string and return the plaintext"""
		result = ''

		for l in ciphertext:
			try:
				i = (key.index(l) - n) % 26
				result += key[i]
			except ValueError:
				result += l

		return result

	text = raw_input(str('Enter your Text :'))


	offset = 5
	encode = base64.b64encode(encrypt(offset, text))
	decode = base64.b64decode(encode)
	#encrypted = encrypt(offset, text)
	os.system('cls')
	print('Encrypted:', encode)

	decrypted = decrypt(offset, decode)
	print('Decrypted:', decrypted)
	anykey= raw_input("Enter anything to return to man menu: ")
	os.system('cls')
	Menu()
import base64
def Dc():
	key = 'abcdefghijklmnopqrstuvwxyz'
	key2 = '123456789'
	def encrypt(n, plaintext):
		"""Encrypt the string and return the ciphertext"""
		result = ''

		for l in plaintext.lower():
			try:
				i = (key.index(l) + n) % 26
				result += key[i]
			except ValueError:
				result += l

		return result.lower()

	def decrypt(n, ciphertext):
		"""Decrypt the string and return the plaintext"""
		result = ''

		for l in ciphertext:
			try:
				i = (key.index(l) - n) % 26
				result += key[i]
			except ValueError:
				result += l

		return result

	text = raw_input(str('Enter your Text :'))


	offset = 5
	#encode = base64.b64encode(encrypt(offset, text))
	decode = base64.b64decode(text)
	#encrypted = encrypt(offset, text)
	#print('Encrypted:', encode)

	decrypted = decrypt(offset, decode)
	decrypted_T = decrypt(offset, text)
	print('Decrypted:', decrypted_T)
	print('Decrypted:', decrypted)

	print('Decrypted:', decode)
	anykey= raw_input("Enter anything to return to man menu: ")
	os.system('cls')
	Menu()
	os.system('cls')
	
def wget():
	dir = raw_input('Change DIR: ')
	print (dir)
	change = os.chdir(dir)
	url = raw_input('Enter URL: ')
	cmd = ('c:\python27\python.exe -m ')+'' + '' +'wget' + ' ' + url 
	print(cmd)
	os.system(cmd)
	Menu()
def cmd():
	while True:
		print "create user"
		print "remove user"
		print "make user admin"
		print "unadmin a user"
		print "enable admin account/disable"
		print "net localgroup Administrators Tom /add"
		print "net user /add [username] [password]"
		cwd = os.getcwd()
		a = ('powershell -Command "Start-Process cmd -Verb RunAs"')
		cmd = raw_input(cwd +'>')
		os.system(cmd + a)
		print ('exit')
		Menu()
		break
		Menu()
#return ManinMenu
Menu()
	
	
#print(Menu())
