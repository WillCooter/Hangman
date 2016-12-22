import re
import time
from functions import *
import os

def run():
	total = 0
	guesses = []
	done = []
	win = False
	clear = lambda: os.system('cls')
	os.system("mode con: cols=60 lines=20")

	word, x = choose_word()
	for _ in range(x):
		done.append("_")
	save = word

	print("\n" * 2)
	print("                          WELCOME")
	time.sleep(1)
	print("\n")
	print("                            TO")
	time.sleep(1)
	print("\n")
	print("                          HANGMAN")
	print("\n" * 2)
	time.sleep(1)
	input("                (press enter to continue...)")
	clear()
	time.sleep(0.4)
	print("\n" * 5)
	print("                The word has", x, "letters.")
	time.sleep(2)
	clear()
	print("\n")
	print(' '.join(map(str, done)))
	print("\n")
	print("What is your first guess?")
	userinput = input(">>> ")

	while total < 11 and win == False:
		userinput = normalise(userinput)
		while len(userinput) != 1 or userinput in guesses:
			if len(userinput) != 1:
				clear()
				print("\n")
				print(' '.join(map(str, done)))
				print("\n")
				print("You can only pick 1 letter. Please choose again...")
			if userinput in guesses:
				clear()
				print("\n")
				print(' '.join(map(str, done)))
				print("\n")
				print("You have already guessed", userinput, ". Please choose again...")
			userinput = input(">>> ")
			userinput = normalise(userinput)
		guesses.append(userinput)
		time.sleep(0.2)
		if userinput in word:
			while userinput in word:
				position = word.index(userinput)
				done.pop(position)
				done.insert(position, userinput)
				word = list(word)
				word[position] = '.'
				word = "".join(word)
			print("\n")
			time.sleep(0.2)
			clear()
			print("\n")
			print(' '.join(map(str, done)))
			print("\n")
			print(userinput.upper(), "is in the word.")
		else:
			total += 1
			print("\n")
			clear()
			print("\n")
			print(' '.join(map(str, done)))
			print("\n")
			print(userinput.upper(), "is not in the word.")
		if len(normalise(word)) == 0:
			win = True
		else:
			time.sleep(0.4)
			print(hangStatus(total))
			print("Guess again...")
			userinput = input(">>> ")
			

	print("\n")
	time.sleep(0.4)
	if win == True:
		print("You Win! The word was", save)
		print("Congratulations")
	else:
		print("You took too many guesses! The word was", save)
		print("Prepare to be hung...")
		total += 1
		print(hangStatus(total))