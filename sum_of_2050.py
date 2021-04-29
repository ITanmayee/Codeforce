"""

A number is called 2050-number if it is 2050, 20500, ..., (2050⋅10k for integer k≥0).

Given a number n, you are asked to represent n as the sum of some (not necessarily distinct) 2050-numbers. Compute the minimum number of 2050-numbers required for that.

"""

def can(num):
    if num < 2050:
        return - 1
    
    if num % 2050 != 0:
        return -1
    if len(str(num)) == 4:
        return num // 2050
    return sum([int(i) for i in str(num // 2050)])


for _ in range (int(input())):
    num = int(input())
    print(can(num))
