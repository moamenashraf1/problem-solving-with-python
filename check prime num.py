#chechking if the numbers is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True
num = int(input())
is_prime(num)