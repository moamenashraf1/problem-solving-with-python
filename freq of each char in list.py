# Counting the Frequency of Each Character in a String
def count(x):
  dic = {}
  for char in x:
    if char in dic:
      dic[char]+=1
    else:
      dic[char]=1
  return(dic)


string = input("enter the string : ")
print(count(string))