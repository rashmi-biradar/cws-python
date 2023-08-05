a = [11, 2, 19, 96, "rashmi", "biradar"]
# print(len(a)-1)

"""
a=0
while i<=len(a)-1
while i<len(a)
or
for i in range(0,len(a))

"""
# for i in range(0, len(a)):
# i=0
# while i<len(a):
#      print(a[i], end=" ")
#      i=i+1
# Ask the user to enter a word
word = input("Enter a word: ")

# Check if the word exists in the file
exists = False
for i in lines:
    if word in i:
        exists = True

if exists:
    print("Yes")
else:
    print("No")
    # Open the file in read mode
f = open("abc.txt", "r")

# Read all the lines from the file
lines = f.readlines()
print(lines)
f = open("abc.txt", "r")
lines = f.readlines()
x = []
for i in lines:
    p = i.strip()
    x.append(int(p))
print(x)
print(sum(x))
f.close()


import random
import sys

word_choices = ["anirudh", "sanjay", "jignesh", "aeroplane"]


while True:
    number_of_try = 5
    secret_word = random.choice(word_choices)
    user_char = []
    guessed_word = []
    for i in secret_word:
        guessed_word.append("_")
    while True:
        w = " ".join(i for i in guessed_word)
        print(f"\n\nCurrent word: {w}")
        char = input("Enter a character = ").lower()

        if char in user_char:
            print("You already have chosen this character")
            continue
        else:
            user_char.append(char)
        if char in secret_word:
            for i in range(0, len(secret_word)):
                if secret_word[i] == char:
                    guessed_word[i] = char
            if guessed_word.count("_") == 0:
                print("You have guessed the word correctly")
                x = input("Do you want to continue? [yes/no]").lower()
                if x == "yes":
                    break
                else:
                    sys.exit()
        else:
            number_of_try -= 1
            print(f"Wrong guess. You have {number_of_try} tries left")
            if number_of_try == 0:
                print(f"You have lost the game. The word was {secret_word}")
                x = input("Do you want to continue? [yes/no]").lower()
                if x == "yes":
                    break
                else:
                    sys.exit()
