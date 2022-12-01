"""
Simulate the trajectory of probe launcher in a discrete 2D space. 
Friction in the x direction slows down the velocity by 1 at every step
Gravity in the y direction decreases velocity by 1 at every step - allowing 
y velocity to change sign 
"""

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
            # print("undershot to the left")
            return False, np.array([x, y]), max_y
        if x > x_target[1] and v_x >= 0:
            # print("overshot to the right")
            return False, np.array([x, y]), max_y
        if y < y_target[0] and v_y <= 0:
            # print("overshot at the bottom")
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
    hits, endpoint, max_ = simulate(velocity, x_target, y_target)
    if hits:
        max_y = max_
solution(max_y)


begin_part_two()
# range of valid x velocities can be worked out a priori
# end(v_x) = 1 + 2 + 3 + ... + v_x = sum(range(v_x + 1))
# { 22: 253, 23: 276, 24: 300, 25: 325, 26: 351, 27: 378, 28: 406, 29: 435}
# Only a velocity of 22 or 23 will END in [253 ... 280] - but higher values may still pass thru the region
valid_starts = []
for v_x in range(21, 400):
    for v_y in range(-200, 200):
        velocity = np.array([v_x, v_y])
        hits, endpoint, max_y = simulate(velocity, x_target, y_target)
        if hits:
            valid_starts.append(velocity)
solution(len(valid_starts))
