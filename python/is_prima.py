import math


def isPrime(n):
    if n < 2:
        return False
    # for i in range(2, n):
    #     if n % i == 0:
    #         return False
    # return True

    # for i in range(2, n // 2):

    #     if n % i == 0:
    #         return False
    # return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


print("1", isPrime(1))
print("2", isPrime(2))
print("5", isPrime(5))
print("10", isPrime(10))
print("19", isPrime(19))
print("35", isPrime(35))
