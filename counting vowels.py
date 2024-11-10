#Counting Vowels in a String
word = input("Enter a word:")
count = 0
for char in word:
  if char=="o" or char=="i" or char=="u" or char=="a" or char=="e":
    count+=1
print(count)