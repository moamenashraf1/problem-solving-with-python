# Calculating Factorial of a Number
num = int(input("Enter the number"))
factorial=1
for i in range(1, num + 1):
    factorial *= i
print("the factorial of the",num,"is",factorial )