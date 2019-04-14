#Created by: Matsuru Hoshi
#Created on: Apr 13, 2019
#This file will guess your age

print("Welcome!")

name = raw_input("What is your name? ")
print( "Hello, " + str(name) + ". You will have to guess my age.")
guess = int(raw_input("What is your guess? "))

age = 15

while age != guess:
	if age < guess:
		print("You guessed bigger. Try again!")
		guess = int(raw_input())
	elif age > guess:
		print("You guessed smaller. Try again!")
		guess = int(raw_input())
	elif age == guess:
		print("You guessed it!")

		break
	
print("Your guessed it! Thank you for playing, " + str(name) + ".")


