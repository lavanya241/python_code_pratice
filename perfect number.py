"""A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself.
A divisor of an integer x is an integer that can divide x evenly.
Given an integer n, return true if n is a perfect number, otherwise return false."""


n = int(input("enter the number:"))
def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5)+1): # check for composite number that are not prime
        if n % i == 0:
            return False
    else:
        return True
    
def perfect_number(n):
    if isprime(n): # if number is prime it returns false
        return False
    perfect_num = 0
    for i in range(1,n):
        if n % i == 0:
            perfect_num += i
            return True

print(perfect_number(n))
