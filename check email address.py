# Checking if a String is a Valid Email Address 
def check_email(mail):
  if mail.count("@")!=1:
    return False
  local_part , domain_part = mail.split("@")
  if len(local_part)==0 or len(domain_part)==0:
    return False
  elif mail.startswith(".") or mail.endswith(".") or domain_part.startswith("."):
    return False
  elif "." not in domain_part:
    return False
  return True    


mail= input("enter your gmail address : ")
if check_email(mail) :
  print("Its a valid email")
else :
  print("Its invalid email")