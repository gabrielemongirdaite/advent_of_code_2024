import time
import re
import matplotlib.pyplot as plt


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    robots = []
    for i in lines:
        robots.append([int(m) for m in re.findall(r'-?\d+', i)])
    return robots


def get_coordinates_after_n_steps(n, robots, max_x, max_y):
    coord = []
    for i in robots:
        coord.append(((i[0] + i[2] * n) % max_x, (i[1] + i[3] * n) % max_y))
    return coord


def robots_in_quadrants(coordinates, mid_x, mid_y):
    quadrant_1 = []
    quadrant_2 = []
    quadrant_3 = []
    quadrant_4 = []

    for i in coordinates:
        x, y = i
        if x < mid_x and y < mid_y:
            quadrant_1.append(i)
        elif x > mid_x and y < mid_y:
            quadrant_2.append(i)
        elif x < mid_x and y > mid_y:
            quadrant_3.append(i)
        elif x > mid_x and y > mid_y:
            quadrant_4.append(i)
    return quadrant_1, quadrant_2, quadrant_3, quadrant_4


start_time = time.time()
robots = read_file('input_day14.txt')

max_x = 101
max_y = 103
coordinates_after_100 = get_coordinates_after_n_steps(100, robots, max_x, max_y)

mid_x = (max_x - 1) / 2
mid_y = (max_y - 1) / 2
quadrant_1, quadrant_2, quadrant_3, quadrant_4 = robots_in_quadrants(coordinates_after_100, mid_x, mid_y)
result = len(quadrant_1) * len(quadrant_2) * len(quadrant_3) * len(quadrant_4)

print('1st part answer: ' + str(result))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
result2 = 0

# to get the sequence
# for i in range(1, 1000):
#     print(i)
#     coordinates = get_coordinates_after_n_steps(i, robots, max_x, max_y)
#     xs = []
#     ys = []
#     for i in coordinates:
#         xs.append(i[0])
#         ys.append(i[1])
#
#     plt.scatter(xs,ys)
#     plt.show()

vertical = [11]
horizontal = [89]
for i in range(1, 100):
    vertical.append(vertical[0] + i * 101)
    horizontal.append(horizontal[0] + i * 103)

for ind, i in enumerate(vertical):
    if i in horizontal:
        result2 = i if result2 == 0 or result2 > i else result2
        coordinates = get_coordinates_after_n_steps(i, robots, max_x, max_y)
        xs = []
        ys = []
        for i in coordinates:
            xs.append(i[0])
            ys.append(i[1])

        plt.scatter(xs, ys)
        plt.show()

print('2nd part answer: ' + str(result2))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
