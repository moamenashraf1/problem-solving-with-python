# Checking for Palindrome Strings
string = input("enter a word:")
length=len(string)//2
is_palindrome = True
for i in range(0,length):
  if string[0]!=string[length-1]:
    is_palindrome=False

if is_palindrome==True:
  print("string is palindrome")
else:
  print("string is not palindrome")

