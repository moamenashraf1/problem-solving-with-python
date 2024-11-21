# finding the longest word in a list
def longest_word():
    lst = list(input("enter the values in the list : ").split())
    max=0
    for i in lst:
      if len(i)>max:
        max=len(i)
        res = i
    return i

print(longest_word())
