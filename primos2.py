import math
def isPrime(number):
    if number == 2:
        return True
    if number<=1 or (number%2)==0:
        return False
    for check in range(3,int(math.sqrt(number))):
        if (number%check) == 0:
            return False
    return True

def isPrime2(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    max_divisor = int(math.sqrt(number)) + 1
    for i in range(3, max_divisor, 2):
        if number % i == 0:
            return False
    return True