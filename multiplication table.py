#9. Write a Python program to create the multiplication table (from 1 to 12) of a number
num = int(input("enter the multiplication table that you want:"))
for i in range(0,13):
  print(f" {num} * {i} = {num*i}")