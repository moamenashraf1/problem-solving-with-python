# Creating a Dictionary from Two Lists
keys = ["name" , "age" , "gender"]
values = ["moamen", "23" , "male"]
dic = {}
for i in range(0,len(keys)):
  dic[keys[i]]=values[i]
print(dic)