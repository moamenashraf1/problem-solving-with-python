#converting temperature units
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

x = int(input("if you want to change from : cel --> fahr enter 1 , cel --> kelv enter 2 , fahr --> cel enter 3 , fahr --> kelv enter 4 , kelv --> cel enter 5 , kelv --> fahr enter 6 : "))
temp = float(input("enter the temp : "))
match x:
  case 1:
    print(celsius_to_fahrenheit(temp))
  case 2:
    print(celsius_to_kelvin(temp))
  case 3:
    print(fahrenheit_to_celsius(temp))
  case 4:
    print(fahrenheit_to_kelvin(temp))
  case 5:
    print(kelvin_to_celsius(temp))
  case 6:
    print(kelvin_to_fahrenheit(temp))
