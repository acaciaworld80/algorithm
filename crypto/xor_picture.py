import sys
import getopt
from itertools import cycle
import binascii

def banner():
	print "******************************************"
	print "XOR PICTURE"
	print "******************************************"

def check_png(file_name):
	file_bytes = open(file_name,"rb")
	magic = "89504e470d0a1a0a"
	data_hex = binascii.hexlify(file_bytes.read())
	if magic == data_hex[:16]:
		return True
	else:
		return False

def usage():
	print "\t\t-i <picture input>"
	print "\t\t-o <output name file>"
	print "\t\t-k <key>"
	print "\t\t\tpython xor_picture.py -i file.png -o output.png -k abc"
	print "\t\t\tuse .png picture"

def xor_calculation(file,key):
	result = ""
	for f,k in zip(file[16:],cycle(key)):
		result += chr(ord(f) ^ ord(k))
	return file[:16]+result

def main():
	if len(sys.argv[1:]) == 6:
		banner()
		try:
			opts,args = getopt.getopt(sys.argv[1:],"i:o:k:")
		except getopt.GetoptError as err:
			print str(err)

		for o,a in opts:
			if o == "-i":
				pic = a
				if check_png(pic) == False:
					print "not png picture"
					sys.exit()
			if o == "-o":
				output = a
			if o == "-k":
				key = a
		file_plain = file(pic,"rb")
		encrypted_png = xor_calculation(file_plain.read(),key)
		file_en = open(output,"wb")							
		file_en.write(encrypted_png)

	else:
		banner()
		usage()
main()
