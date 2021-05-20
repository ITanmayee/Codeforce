"""

Lord Omkar has permitted you to enter the Holy Church of Omkar! To test your worthiness, Omkar gives you a password which you must interpret!

A password is an array a of n positive integers. You apply the following operation to the array: pick any two adjacent numbers that are not equal to each other and replace them with their sum. Formally, choose an index i such that 1≤i<n and ai≠ai+1, delete both ai and ai+1 from the array and put ai+ai+1 in their place.

For example, for array [7,4,3,7] you can choose i=2 and the array will become [7,4+3,7]=[7,7,7]. Note that in this array you can't apply this operation anymore.

Notice that one operation will decrease the size of the password by 1. What is the shortest possible length of the password after some number (possibly 0) of operations?

"""


def shortest_password_length(arr):
    if len(set(arr)) == 1:
        return len(arr)
    return 1
 
for _ in range(int(input())):
    arr_size = int(input())
    arr = list(map(int, input().split()))
 
    print(shortest_password_length(arr))
