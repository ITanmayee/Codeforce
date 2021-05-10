"""

Sayaka Saeki is a member of the student council, which has n other members (excluding Sayaka). The i-th member has a height of ai millimeters.

It's the end of the school year and Sayaka wants to take a picture of all other members of the student council. Being the hard-working and perfectionist girl as she is, she wants to arrange all the members in a line such that the amount of photogenic consecutive pairs of members is as large as possible.

A pair of two consecutive members u and v on a line is considered photogenic if their average height is an integer, i.e. au+av2 is an integer.

Help Sayaka arrange the other members to maximize the number of photogenic consecutive pairs.

"""

for _ in range(int(input())):
    no_of_members = int(input())
    heights = list(map(int, input().split()))
    odds, evens = [], []
 
    for i in heights:
        if i % 2 == 0:
            evens.append(str(i))
        else:
            odds.append(str(i))
    print(' '.join(odds + evens))
