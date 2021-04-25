"""

You are given two positive integers a and b.

In one move, you can change a in the following way:

Choose any positive odd integer x (x>0) and replace a with a+x;
choose any positive even integer y (y>0) and replace a with a−y.
You can perform as many such operations as you want. You can choose the same numbers x and y in different moves.

Your task is to find the minimum number of moves required to obtain b from a. It is guaranteed that you can always obtain b from a.

You have to answer t independent test cases.

Input
The first line of the input contains one integer t (1≤t≤104) — the number of test cases.

Then t test cases follow. Each test case is given as two space-separated integers a and b (1≤a,b≤109).

Output
For each test case, print the answer — the minimum number of moves required to obtain b from a if you can perform any number of moves described in the problem statement. It is guaranteed that you can always obtain b from a.

"""

test_cases = int(input())
 
for i in range(test_cases) :
    a , b = map(int, input().split())
    if b > a:
        if (b - a) % 2 ==  0 :
            print(2)
        else :
            print(1)
    elif a > b :
        if (a - b) % 2 == 0 :
            print(1)
        else :
            print(2)
    else :
        print(0)
