"""
T
here is a n×m grid. You are standing at cell (1,1) and your goal is to finish at cell (n,m).

You can move to the neighboring cells to the right or down. In other words, suppose you are standing at cell (x,y). You can:

move right to the cell (x,y+1) — it costs x burles;
move down to the cell (x+1,y) — it costs y burles.

Can you reach cell (n,m) spending exactly k burles?


"""

for _ in range(int(input())):
    x, y, burles = map(int, input().split())

    one_direction  = max(x, y) - 1
    other_direction = (min(x,y) - 1) * max(x,y)

    if one_direction + other_direction == burles:
        print("YES")
    else:
        print("NO")
