## Write a Python program to guess a number between 1 and 9
##User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a \"Well guessed!\" message, and the program will exit
import random
random_num = random.randint(1,10)
while True:
  num = int(input("Guess a number between 1 and 9:"))
  if num == random_num:
    print("Well guessed!")
    break
  else:
    print(" guesses wrong , Try Again")