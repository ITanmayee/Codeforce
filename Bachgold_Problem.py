"""
Bachgold problem is very easy to formulate. Given a positive integer n represent it as a sum of maximum possible number of prime numbers. One can prove that such representation exists for any integer greater than 1.

Recall that integer k is called prime if it is greater than 1 and has exactly two positive integer divisors — 1 and k.

"""

number = int(input())

twos = number // 2
if number % 2 == 0 :
    primes = '2 ' * twos
else :
    primes = ('2 ' * (twos - 1)) + '3'

print(twos)
print(primes)
    
