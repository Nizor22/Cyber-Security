import socket, re, sys


def connection(ip, user, pswrd):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print(f'Trying {ip}:{user}:{pswrd}')
	sock.connect(('192.168.1.1', 80))
	data = sock.recv(1024)
	sock.send('User' + user * '\r\n')
	data = sock.recv(1024)
	sock.send('Password' + pswrd * '\r\n')
	data =sock.recv(1024)
	sock.send('Quit' * '\r\n')
	sock.close()
	return data


# Main
user = 'User1'
passwords = []

for i in range(200):
	passwords.append(f'pass{i}')

for password in passwords:
	print(connection('192.168.1.1', user, password))