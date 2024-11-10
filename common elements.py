# Finding Common Elements in Two Lists
def input_list():
  
    user_input = input("Enter elements of the list: ")
    return list(map(int, user_input.split()))


lst_1 = input_list()
lst_2 =  input_list()
common_elements = list(set(lst_1) & set(lst_2))
print(common_elements)