#Finding the Maximum Value in a List
lst = [1 , 5 , 4 , 7 , 2 , 11]
max = lst[0]
for i in lst:
  if i>max:
    max=i

print(max)

#another method
#lst = [1 , 5 , 4 , 7 , 2 , 11]
#lst.sort()
#print(lst[-1])