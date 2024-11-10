#5. Write a Python program that accepts a word from the user and reverses it
word = input("enter a word and i will reverse it :")
length = len(word)
reversed_word=""
for i in range(length-1,-1,-1):
  reversed_word+=word[i]
print(reversed_word)
