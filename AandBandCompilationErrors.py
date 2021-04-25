"""
A and B are preparing themselves for programming contests.

B loves to debug his code. But before he runs the solution and starts debugging, he has to first compile the code.

Initially, the compiler displayed n compilation errors, each of them is represented as a positive integer. After some effort, B managed to fix some mistake and then another one mistake.

However, despite the fact that B is sure that he corrected the two errors, he can not understand exactly what compilation errors disappeared — the compiler of the language which B uses shows errors in the new order every time! B is sure that unlike many other programming languages, compilation errors for his programming language do not depend on each other, that is, if you correct one error, the set of other error does not change.

Can you help B find out exactly what two errors he corrected?
"""

n = int(input())
error_list1 = list(map(int , input().split()))
error_list2 = list(map(int , input().split()))
error_list3 = list(map(int , input().split()))

error1 = sum(error_list1) - sum(error_list2)
error2 = sum(error_list2) - sum(error_list3)

print(error1)
print(error2)
