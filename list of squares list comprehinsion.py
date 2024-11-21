# Generating a list of squares using list comprehension and func
def square(a):
  return a**2

n=int(input("enter the end of range "))
lst=[square(i) for i in range(1,n+1)]
print(lst)
