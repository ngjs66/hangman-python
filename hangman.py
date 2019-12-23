#!/usr/bin/env python3
# This is a Hangman program written in Python. 

import random
import sys

wordList = ["samsung", "apple", "huawei", "motorola" , "oneplus", "honor", "xiaomi", "google"]

def choose():
    # gets a random word from a list
    wordList = random.choice(word)

def hint(word):
    print("The length of the word is: %d" % len(word))

def main():
    print("Welcome to the program: Hangman!")
    name = input("Please enter your name: ")
    hint()




import random

l_word = ["secret","apple","mango"]
word = random.choice(l_word)
guesses = ''
turns = 10
while turns > 0:
failed = 0
for char in word:
if char in guesses:
print (char,end=" " )
else:
print ("-", end = " ")
failed += 1
if failed == 0:
print ("\n You won")
break
if turns == 10:
print("\nhint:The word is of ",+ len(word),"characters")
turns -= 1
guess = input("\nguess a character: ")

guesses += guess
if guess not in word:
turns -= 1
print ("\nWrong")
print ("\nYou have", + turns, 'more guesses' )
if turns == 0:
print ("\nYou Loose")