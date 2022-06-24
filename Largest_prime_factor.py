# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ? 

from math import ceil


def isPrime(n):
    isprime = 0
    i = 2
    while i <= n:
        if n%i != 0:
            isprime = 1
        else:
            isprime = 0

        i+=1
        
    return isprime


# def LarPrimeFactor(number):
#     largest_pfactor = 1
        
#     return largest_pfactor

print(isPrime(2))
# print(ceil(5/2))



