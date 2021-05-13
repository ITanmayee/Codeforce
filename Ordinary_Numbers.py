"""

Let's call a positive integer n ordinary if in the decimal notation all its digits are the same. For example, 1, 2 and 99 are ordinary numbers, but 719 and 2021 are not ordinary numbers.

For a given number n, find the number of ordinary numbers among the numbers from 1 to n.

"""

def same(num):
    if num < 10:
        return num
    all_same = 0
    if num < int(str(num)[0] * len(str(num))):
        all_same += int(str(num)[0]) - 1
    else:
        all_same += int(str(num)[0])
    all_same += ((len(str(num)) - 1) * 9)
    return all_same
 
for _ in range(int(input())):
    num = int(input())
    print(same(num))
