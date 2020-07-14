from optparse import OptionParser
from zipfile import ZipFile
from threading import Thread


def extractFile(zFile, password):
	try:
		zFile.extractall(pwd=bytes(password, 'utf-8'))
		print(f'[+] Found password {password}\n')
	except:
		pass


def main():
	# Creating flags for the program
	parser = OptionParser('usage%prog -f <zipfile> -d <dictionary>')
	parser.add_option('-f', dest='zname', type='string', help='specify zip file')
	parser.add_option('-d', dest='dname', type='string', help='specify dictionary file')
	# Stores the values of the two flags in this tuple
	(options, args) = parser.parse_args()
	# print(options)
	# print(args)
	if options.zname is None or options.dname is None:
		print(parser.usage)
		exit(0)
	else:
		zname = options.zname
		dname = options.dname

	zFile = ZipFile(zname)
	passwdFile = open(dname, 'r')

	for line in passwdFile.readlines():
		password = line.strip('\n')
		t = Thread(target=extractFile, args=(zFile, password))
		t.start()


if __name__ == '__main__':
	main()
