#calculating avr of numbers
def calculate_average():
    lst = list(map(float,input("enter the values in the list : ").split()))
    total = sum(lst)
    average = total / len(lst)
    return average

print(calculate_average())