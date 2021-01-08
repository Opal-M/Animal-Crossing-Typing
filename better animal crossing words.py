import time
import sys
delay = 0.5
def p (word):
  for letter in words:
	  print(letter, end='', flush=True)
	  time.sleep(delay)
  print("")

def better_p (*arguments):
	#print the list
	#print(arguments)
	#print(len(arguments))
	#print each thing in the list
	for i in range(len(arguments)):
		print(arguments[i])
	#make a string that starts w the first value of the list
	longstring = arguments[0]
	print(longstring)
	#concatenate every value in the list to the string
	for i in range(len(arguments)):
		longstring += arguments[i]
		print(longstring)
	#for every character in the long string print the character and then wait
	for letter in longstring:
	  print(letter, end='', flush=True)
	  time.sleep(delay)
better_p("hello1","hello2","hello3")