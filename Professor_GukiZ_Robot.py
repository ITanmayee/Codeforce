"""

Professor GukiZ makes a new robot. The robot are in the point with coordinates (x1, y1) and should go to the point (x2, y2). In a single step the robot can change any of its coordinates (maybe both of them) by one (decrease or increase). So the robot can move in one of the 8 directions. Find the minimal number of steps the robot should make to get the finish position.

"""


current_x, current_y = map(int, input().split())
reach_x, reach_y = map(int, input().split())

def find_min_steps(current_x, current_y, reach_x, reach_y):
    return max(abs(current_x - reach_x), abs(current_y - reach_y))

print(find_min_steps(current_x, current_y, reach_x, reach_y))
