# Python Program to Print the Fibonacci sequence
terms = int(input("enter the number of terms you want to see in fibonacci sequence"))
x=0
y=1
for i in range(terms):
  print(x , end=" ")
  x,y=y,x+y
  