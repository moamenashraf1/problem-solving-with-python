#6. Write a Python program to count the number of even and odd numbers in a series of numbers
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13]
even_count=0
odd_count=0
for i in numbers:
  if i%2==0:
    even_count+=1
  else:
    odd_count+=1
print("Even numbers are :", even_count)
print("Odd numbers are  :", odd_count)

