# Write a Python program to construct the diamond pattern, using a nested for loop
x=6
for i in range(1,x+1):
  print(' ' * (x-i) + "* " * i )

  if(i==x):
    for j in range(x-1,0,-1):
      print(' ' * (x-j) + "* " * j)