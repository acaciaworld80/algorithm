import requests
import getopt
import sys
import time
from termcolor import colored

def banner():
	print "*************************************"
	print "fuzz-buster"
	print "*************************************"	

def count_line(website_sourcecode):
	
	data = website_sourcecode.split("\n")
	line = len(data)
	return line

def usage():
	print "-t <target>"
	print "-w <wordlist>"

def return_size_packet(website_packet):
	b = sys.getsizeof(website_packet)
	return b

def print_banner():
	print "status\t|time\t\t\t|line\t\t|bytes\t\t|url"

def query_url(url):
	start = time.time()
	r = requests.get(url)
	end = time.time() - start
	status = r.status_code
	
	line = 	count_line(r.text)
	byte_size = return_size_packet(r.text)

	if 200 <= status < 300:
		print str(colored(status,"green"))+"\t:\t"+str(end)+"\t:\t"+str(line)+"\t:\t"+str(byte_size)+"\t:\t"+str(url)
	if 400 <= status < 500:
		print str(colored(status,"red"))+"\t:\t"+str(end)+"\t:\t"+str(line)+"\t:\t"+str(byte_size)+"\t:\t"+str(url)
	if 300 <= status < 400:
		print str(colored(status,"blue"))+"\t:\t"+str(end)+"\t:\t"+str(line)+"\t:\t"+str(byte_size)+"\t:\t"+str(url)
	

if len(sys.argv[1:]) >= 2:
	try:
		opts,args = getopt.getopt(sys.argv[1:],"t:w:")
	except getopt.GetoptError as err:
		print str(err)

	for o,a in opts:
		if o == "-t":
			target = a
		if o == "-w":
			url_list = open(a,"r").readlines()
	banner()
	print_banner()
	for url in url_list:
		test_url = target+url.rstrip("\n")
		query_url(test_url)
