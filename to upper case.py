#convert a list of strings to uppercase
def to_upper():
    return list(map(lambda i: i.upper() , input("Enter the list: ").split()))
x = to_upper()
print(x)
