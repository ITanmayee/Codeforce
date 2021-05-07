"""

You have r red and b blue beans. You'd like to distribute them among several (maybe, one) packets in such a way that each packet:

has at least one red bean (or the number of red beans ri≥1);
has at least one blue bean (or the number of blue beans bi≥1);
the number of red and blue beans should differ in no more than d (or |ri−bi|≤d)
Can you distribute all beans?

"""

for _ in range(int(input())):
    red, blue, diff = map(int, input().split())

    if min(red, blue) * (diff + 1) < max(red, blue):
        print("NO")
    else:
        print("YES")
