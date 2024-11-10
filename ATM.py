# A Program that Simulating a Basic ATM Withdrawal
balance = float(input("Enter your balance:"))
while balance > 0:
  withdraw = int(input("Enter the value you want to withdraw:"))
  if withdraw <= balance:
    balance-=withdraw
    print("successful transaction , remaining balance is :", balance)
  else:
    print("not enough balance")

  if balance==0:
    print("balance is zero")
    break