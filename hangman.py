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