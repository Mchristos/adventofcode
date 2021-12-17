from helpers import read_input, begin_part_one, begin_part_two, solution
import numpy as np


def simulate(velocity, x_target, y_target):
    x, y = 0, 0
    v_x, v_y = velocity
    max_y = y
    while (x < x_target[0] or x > x_target[1]) or (y < y_target[0] or y > y_target[1]):
        x = x + v_x
        y = y + v_y
        if y > max_y:
            max_y = y
        if x < x_target[0] and v_x <= 0:
            print("undershot to the left")
            return False, np.array([x, y]), max_y
        if x > x_target[1] and v_x >= 0:
            print("overshot to the right")
            return False, np.array([x, y]), max_y
        if y < y_target[0] and v_y <= 0:
            print("overshot at the bottom")
            return False, np.array([x, y]), max_y
        v_y = v_y - 1
        # -1 if positive, +1 if negative
        v_x = v_x - np.sign(v_x)
    return True, np.array([x, y]), max_y


x_target = [253, 280]
y_target = [-73, -46]

begin_part_one()
hits = True
velocity = np.array([23, 50])
max_y = -1
while hits:
    velocity[1] += 1
    hits, endpoint, max = simulate(velocity, x_target, y_target)
    if hits:
        max_y = max
solution(max_y)


begin_part_two()
solution()
