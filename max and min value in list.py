# max and min value in a list
def maxx(lst): # function for max value
  max = lst[0]
  for i in lst:
    if i>max:
      max=i
  return(max)

def minn(lst):  # function for min value
  min = lst[0]
  for i in lst:
    if i<min:
      min=i
  return(min)

lst = list(input("enter the values in the list : ").split())

print("maximum number is : " , maxx(lst))
print("minimum number is : " , minn(lst))

