import random
import re
from data import *


def choose_word():
	chosen = random.choice(words)
	return chosen, len(chosen)

def normalise(userinput):

	"""
	>>> normalise("1234567890!£$%^&*-+={[}]:;@~#<,>.?/a B c")
	'abc'
	"""

	userinput = re.sub(r'\W+', '', userinput)
	userinput = ''.join([i for i in userinput if not i.isdigit()])
	userinput = userinput.lower()
	return userinput

def hangStatus(x):
	return figures[x]