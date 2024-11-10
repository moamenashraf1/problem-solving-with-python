# Finding the Sum of Digits of a Number
num = int(input("enter a number"))
sum_of_digits = 0

while num > 0:
    sum_of_digits += num % 10
    num //= 10

print("Sum of digits is:", sum_of_digits)