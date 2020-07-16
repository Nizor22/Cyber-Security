import socket, sys, os

# After connecting reads the banner.
def retBanner(ip, port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip, port))
		banner = s.recv(1024)
		return banner
	except:
		return


''' Compares the banners with the one in the file.
	Checks if any specific banner list file was given during the run-time and use that instead. 
	Otherwise, the vuln-banners.txt will be used. 
	Checks if the file is in the current working directory and if the user has permission to it use it.
	If the banner returned had been found in the list of vulnerable banners, print it.
'''
def checkVulns(banner):
	banner = banner.decode('utf-8')
	if len(sys.argv) == 2:
		filename = sys.argv[1]
	else:
		filename = open('vuln-banners.txt', 'r')
	if not os.path.isfile(filename):
		print(f'[-] {filename} does not exist.')
		exit(0)
	if not os.access(filename, os.R_OK):
		print(f'[-] {filename} access denied.')
		exit(0)
	print(f'[+] Reading vulnerabilities from {filename}')
	for line in filename.readlines():
		if line.strip('\n') in banner:
			print('[+] Server is vulnerable: ' + banner.strip('\n'))
	print('[-] FTP Server is not vulnerable')


def main():
	portList = [21, 22, 25, 80, 110, 443]
	
	for x in range(1, 255):
		ip = f'192.168.1.{x}'
		for port in portList:
			banner = retBanner(ip, port)
			if banner:
				print(f'[+] {ip}: {banner.decode("utf-8")}')
				checkVulns(banner)


if __name__ == '__main__':
	main()
