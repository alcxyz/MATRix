###########~ MATRix ~############
#Version: 1.0
#Author: Andre Lucas Carvalho,
#Email: droydi@alc.no
#Home: wwww.droydi.com
#
#The MIT License (MIT)
#
#Copyright (c) 2015 droydi		
#
#Thanks for the help guys!			
#Share with care!				
#################################

import sys, math
from fractions import Fraction
from decimal import Decimal


#Math definitions
e = math.e
pi = math.pi
cos = math.cos
sin = math.sin
tan = math.tan
arctan = math.atanh
arccos = math.acosh
arcsin = math.asinh
sqrt = math.sqrt
ln = math.log
log = math.log10

done = 0

p = "\n"+"." * 30


def is_fraction(value):
	if value % 2 == 0 or (value+1) % 2 == 0:
		return True
	else:
		return False

def handle_input(msg):
	s = raw_input(msg)
	numbers = s.split('/')
	val = Decimal(numbers[0])
	for num in numbers[1:]:
		val /= Decimal(num)

	return val

#Matrix Single Operation
def start():
	
	#Number to zero out
	a = handle_input("Input the number you wish to zero out (as written in the given matrix): ")

	#Pivot
	b = handle_input("Input the leading number, pivot (as written in the given matrix): ")

	#A loop
	done = False
	while done == False:
		print ("Let's work on the next number on this row.")
		done = sett_inn(a, b)
	
	quit = str(raw_input("Wanna quit? ")).lower()

	if quit == "y" or quit == "yes":
		sys.exit("k, thx bye")
	else:
		start()



def sett_inn(a, b):

	c = handle_input("What number are you changing? ")

	d = handle_input("What number affects your operation? ")

	print p
	print "Sending assassin to kill: ",c, "according to: ",d," orders..."
	print p

	return matrix(a,b,c,d)

def matrix(a, b, c, d):
	
	#Where the math happens
	answer = c-((a/b)*d)
	print "The number is changed to: ",Fraction(answer)
	
	return ifdone(a,b,c,d)


#Check if done
def ifdone(a,b,c,d):
	
	whilecount = 0

	#Another loop
	while 1:
		whilecount += 1

		if whilecount % 3 == 0:
			print "Please answer yes, or no...."+p+p


		doneq = (str(raw_input("Done with this row? (y/es / n/o) "))).lower()

		if doneq == "y" or doneq == "yes":
			done = 1
			return True
		elif doneq == "n" or doneq == "no":
			done = 0
			return False
		else:
			print "Let's try this again..."

		print p


print "Hi! This tool is a simple helper to speed up your matrix operations."
print "Just follow the yellow brick road! Feedbacks are welcomed."
print p

start()

