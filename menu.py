
import requests
import socket
from six.moves.urllib.parse import urlparse
import threading
from sys import exit
import os
import pickle
import ftplib
import csv
import uuid
#import en
#from en import passwd
#from en import Email
#from psk2 import passwd
#from psk2 import Email
#import server_ftps
#from server_ftps import server1
#from server_ftps import RetrFile
#from RetrFile import server_ftps
import sys
import BeautifulSoup
import base64
import os
from googlevoice import Voice
from util import input
#from googlevoice import Voice
#from googlevoice.util import input
def Menu():
    os.system('cls')
    print("1. Encrypted Text")
    print("2. Decrypt TEXT")
    print("3. Send SMS")
    print("4. wget")
    print("5. cmd")
    print("6. SFTP server")
    print("7. SFTPS Client")
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
				break
			elif menu ==5:
				cmd()
				break
			elif menu ==6:
				main()
				break
			elif menu == 7:
				Ftps()
				break
			elif main == 8:
				break
			else:
				print ("Invalid")
				Menu()
		except ValueError:
			Menu()
			print ("Invalid Choice Enetr 1-4")
    exit		
def SMS():
#powershell -Command " wget htttp:\\example.com\p.e -OutFile p.pckl"
	PATH = cwd = os.getcwd() + "\p.pckl"
	print PATH
	if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
		print "File exists and is readable"
	else:

		print "Either file is missing or is not readable"
		dir = cwd = os.getcwd()
		print (dir)
		change = os.chdir(dir)
		url = 'http:\\example.com\store.pckl -OutFile store.pckl"'
		cmd = ('powershell -Command "')+'' + '' +'wget' + ' ' + url 
		print(cmd)
		os.system(cmd)
		url = 'https:\\example.com\p.pckl -OutFile p.pckl"'
		cmd = ('powershell -Command "')+'' + '' +'wget' + ' ' + url 
		print(cmd)
		os.system(cmd)

	'''
	url = 'https:\\example.com'
	#url2 = 'https:\\example.com' 
	target_path ='./'
	r = requests.get(url)
	with open("p.pckl",'wb') as f:
			f.write(r.content)
	url2 = 'https:\\example.com'		
	target_path ='./'
	r = requests.get(url2)
	with open("store.pckl",'wb') as f:
			f.write(r.content)
			'''
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

	offset = 5
	#print "File exists and is readable"
	f = open('store.pckl', 'rb')               #read file
	obj = pickle.load(f)                        #Email
	#print 'obj',obj
	f.close
	#print 'test'
		#Main()
	decode2 = base64.b64decode(obj)

	p = open('p.pckl', 'rb')                  #read file
	obj7 = pickle.load(p)                     #password
	p.close
	#print ' test',obj7


	decode = base64.b64decode(obj7)
	Email = decrypt(offset, decode2)
	#print('Decrypted:user', Email)
	passwd = decrypt(offset, decode)
	#print('Decrypted:pass', passwd)
	#print 'ok'
	while True:
		os.system('cls')
		n = raw_input("Please enter 'pass':")
		os.system('cls')
		if n.strip() == 'Dasher':
		 break
	voice = Voice()
	voice.login(Email,passwd)
	number = ""
	Ammi = ""
	print ("1. user1")
	print ("2. user2")
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
			os.system('cls')
			#print "create user"
			#print "remove user"
			#print "make user admin"
			#print "unadmin a user"
			#print "enable admin account/disable"
			#print "net localgroup Administrators Tom /add"
			print "net user /add [username] [password]"
			cwd = os.getcwd()
			a = ('powershell -Command "Start-Process cmd -Verb RunAs"')
			cmd = raw_input(cwd +'>')
			os.system(cmd + a)
			os.system(cmd)
			anyThing8 = int(input("Enter anything to return to man men222u: "))
			if anyThing8 == 1:
			   print ('OK')
			elif anyThing8 ==4:
				print 'jack'
			else:
				print ('exit')
				break
		
		
		
		
		
		
def server1 (name, sock):
    filename = sock.recv(2024)
    if os.path.isfile(filename):
        sock.send("EXISTS " + str(os.path.getsize(filename)))
        userResponse = sock.recv(2024)
        if userResponse[:2] == 'OK':
            with open(filename, 'rb') as f:
                bytesToSend = f.read(2024)
                sock.send(bytesToSend)
                while bytesToSend != "":
                    bytesToSend = f.read(2024)
                    sock.send(bytesToSend)
    else:
        sock.send("ERR ")

    sock.close()
	
def main():
    host = raw_input('Enter ip: ')
    port = 500


    s = socket.socket()
    s.bind((host,port))

    s.listen(5)

    print "Server Started."
    while True:
        c, addr = s.accept()
        print "client connedted ip:<" + str(addr) + ">"
        t = threading.Thread(target=server1, args=("RetrThread", c))
        t.start()
        anykey= raw_input("Enter anything to return to man menu: ")
        if anykey == 10:
			Menu()
			break
        elif anykey == 3:
		    print "TEST"
		    break
        else:
            Menu()
		#Menu()
    s.close()
	#anykey= raw_input("Enter anything to return to man menu: ")

#if __name__ == '__main__':
    #main()
#Menu()
#return ManinMenu


def Ftps():
#def Main():
    ip = raw_input('Enter IP address: ')
    host = ip
    port = 5000

    s = socket.socket()
    s.connect((host, port))
    file = 'setup.py'
    filename = raw_input("Filename? -> ")
    if filename != 'q':
        s.send(filename)
        data = s.recv(2024)
        if data[:6] == 'EXISTS':
            filesize = long(data[6:])
            message = raw_input("File exists, " + str(filesize) +"Bytes, download? (Y/N)? -> ")
            if message == 'Y':
                s.send("OK")
                f = open('new_'+filename, 'wb')
                data = s.recv(2024)
                totalRecv = len(data)
                f.write(data)
                while totalRecv < filesize:
                    data = s.recv(2024)
                    totalRecv += len(data)
                    f.write(data)
                    print "{0:.2f}".format((totalRecv/float(filesize))*100)+ "% Done"
                print "Download Complete!"
                f.close()
        else:
            print "File Does Not Exist!"

    s.close()

#if __name__ == '__main__':
 #   Main()







Menu()
	
	
#print(Menu())
