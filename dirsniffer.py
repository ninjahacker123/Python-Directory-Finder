"""

	Written in Python Version: 3.7.6

	This is a programme written to find directories within a web page by requesting names of common directories
	of websites provided by a wordlist by a user. A for loop iterates through words given by the wordlist to check 
	if they return a status code of 200 if a GET request has been send. A deafault wordlist has been provided 
	in the directory.

	- Joseph Marc Antony

"""

import requests

print('')

print("[!] NOTE: While entering do not add '/' to the end of a url")
print('')

default = "wordlists/wordlist.txt"

url = input("[*] Enter url to scan: ")
print('')

change = input("[*] Do you want to use default wordlist (y/ n): ")
print('')

wordlist = open(default, "r")

if change.lower() == "y":

	print("-" * 50 + " Searching " + "-" * 50)
	print('')

	print("Directories Found:")
	print('')

	for word in wordlist:
		if requests.get(url + "/" + word.rstrip()).status_code == 200 or requests.get(url + "/" + word.rstrip()).status_code == 301:
			print(f"	[+] Status Code: {requests.get(url + '/' + word.rstrip()).status_code} / Directory: {word}")
			print('')
		elif 1 + 1 == 2: # Elif statement written to fix else statement issue I was facing
			a = 2
		elif requests.get(url + "/" + word.rstrip()).status_code >= 500:
			print("[-] Server is down!")
		else:
			break

else:
	path = input("[*] Wordlist Path: ")
	print('')

	try:
		wordlist = open(path, "r")
	except:
		print("Error:")
		print(f"	{path} was not found, enter an existing wordlist!")
		quit()

	print("-" * 50 + " Searching " + "-" * 50)
	print('')

	print("Directories Found:")
	print('')

	for word in wordlist:
		if requests.get(url + "/" + word.rstrip()).status_code == 200 or requests.get(url + "/" + word.rstrip()).status_code == 301:
			print(f"	[+] Status Code: {requests.get(url + '/' + word.rstrip()).status_code} / Directory: {word}")
		elif 1 + 1 == 2: # Elif statement written to fix else statement issue I was facing
			a = 2
		else:
			break
