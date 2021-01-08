import time, sys
words = "Hello World"
for letter in words:
	sys.stdout.write(letter)
	sys.stdout.flush()
	time.sleep(0.05)

def p (words):
    for letter in words:
        print(letter, end='', flush=True)
        time.sleep(delay)
    print("")
