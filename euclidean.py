#!/usr/bin/python

def euclidean(a,b):
	quotient = a / b
	remainder = a % b
	
	return b,remainder
	
def main():
	a = input("input the a:")
	b = input("input the b:")	
		

	while True:
	
		if a == 0:
			print "GCD = %d" % b
			break
		elif b == 0:
			print "GCD = %d" % a
			break
		else:
			a,b = euclidean(a,b) 	
		
main()
