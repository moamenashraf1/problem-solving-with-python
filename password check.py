# Simulating a Simple Password Check
password = "DEPI_2024"
attempt_num = 3
while attempt_num>0:
  input_pass = input("enter the password : ")
  if input_pass != password:
    attempt_num -=1
    print("incorrect password , attempt left is " , attempt_num)
  else:
    print("correct password , unclocked")
    break

if attempt_num==0:
  print("access denied")