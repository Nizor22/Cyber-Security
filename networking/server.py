import socket
import sys


# Create a socket to connect 2 computers
def create_socket():
	try:
		global host, PORT, s
		host = ''
		PORT = 9999
		s = socket.socket()

	except socket.error as msg:
		print("Socket creation error: " + str(msg))


# Binding the socket and listening for connections
def bind_socket():
	try:
		print("Binding the Port: " + str(PORT))
		s.bind((host, PORT))
		s.listen(5)
	except socket.error as msg:
		print("Socket binding error: " + str(msg))
		print("Retrying...")
		# Recursion
		bind_socket()


def socket_accept():
	conn, address = s.accept()
	print("Connection has been established! | IP " + address[0] + " | Port" + str(address[1]))
	send_commands(conn)
	conn.close()


# Send commands to the client.py
def send_commands(conn):
	while True:
		cmd = input()
		if cmd == 'quit':
			conn.close()
			s.close()
			sys.exit()
		if len(str.encode(cmd)) > 0:
			conn.send(str.encode(cmd))
			client_response = str(conn.recv(1024), 'utf-8')
			print(client_response, end='')


def main():
	create_socket()
	bind_socket()
	socket_accept()


main()
