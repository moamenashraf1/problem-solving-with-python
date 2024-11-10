# Write a Python program to construct the following pattern, using a nested for loop

for i in range(1,6):                             # *
  print("*"*i)                                   # **
  if(i==5):                                      # ***
    for j in range(i-1,0,-1):                    # ****
      print("*"*j)                               # *****
                                                 # ****
                                                 # ***
                                                 # **
                                                 # *

