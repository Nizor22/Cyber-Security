import crypt


# Attempts a dictionary attack by encrypting words from dictionary
# and comparing it to the user's hashed password.
def testPass(cryptPass):
	salt = cryptPass[0:2]
	dictFile = open('dictionary.txt', 'r')

	for word in dictFile.readlines():
		word = word.strip('\n')
		cryptWord = crypt.crypt(word, salt)
		if cryptWord == cryptPass:
			print(f'[+] Found Password: {word}\n')
			return
	print('[-] Password Not Found.\n')
	return


def main():
	# File containing the user name and its UNIX hashed password
	passFile = open('passwords.txt')
	# Calls the testPass function for every password in the dictionary.
	for line in passFile.readlines():
		if ':' in line:
			user = line.split(':')[0]
			# User's hashed password
			cryptPass = line.split(':')[1].strip(' ')
			print(f'[*] Cracking Password For {user}')
			testPass(cryptPass)


if __name__ == '__main__':
	main()
