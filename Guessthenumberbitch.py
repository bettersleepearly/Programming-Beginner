#!/usr/bin/env python3

import random

number = random.randint(1, 10)
tries = 1

welcome = "Hello Mr."
print ("Hello my friend, give me your name mate:")

name = input()

print()
print (welcome + " " + name)

print()
question = input("Would you like a little game bruh? [Y/N] ")
if question == "N":
    print("Well then... fuck you mate!") 

if question == "Y":
    print()
    print("let's fucking go then :) ") 
    print("Now, on a scale from 1 to 10")
    print("How much of an asshole u think u are? :)")
    guess = int(input("guess quick:"))
    
    if guess == number:
        print()
        print("Wew WTF! You got it spot on @@")
    
    if guess > number: 
        print()
        print("Sikeeee! That's way too high nigger :) ")
        print("Go easy on yourself")
        print("Now dropIt!")


    if guess < number:
        print()
        print("That number is gonna be way up there bitchh LMAO")
        print("Can't believe you underated yourself :) ")
        print("Higher now!")

while guess != number:
    tries += 1
    print()
    guess = int(input("Quick! Again: "))
    
    if guess < number:
        print()
        print("Nope! still not high enough")
        print("Again!")

    if guess > number:
        print()
        print("Nope! still not low enough")
        print("Again!")

    if guess == number:
        print()
        print("Fine fine! You win! The number was", number, "and it was only", tries, "tries!")
        print()

        
        
        
question1 = input("Wanna try again? [Y/N]")

if question1 == "N":
    print()
    print("Fine fuck off then :)")

    
if question1 == "Y":
    print("let's fucking go then")
    print()
    print("Now, on a scale from 1 to 10")
    print("How much of an asshole u think u are? :)")
    guess = int(input("guess quick:"))
