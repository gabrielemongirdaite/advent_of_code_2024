import time
from itertools import combinations


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    antennas = []
    for i in lines:
        antennas.extend(list(set(i)))
    antennas = list(set(antennas))
    antennas.remove('.')
    d = {}
    for i in antennas:
        d[i] = []
        for y, k in enumerate(lines):
            for x, l in enumerate(k):
                if l == i:
                    d[i].append((x, y))
    return d, len(lines[0]), len(lines)


def antinode(antenna_coord, max_x, max_y, part=1):
    comb = list(combinations(antenna_coord, 2))
    antinodes = []
    for i in comb:
        x1 = i[0][0]
        y1 = i[0][1]
        x2 = i[1][0]
        y2 = i[1][1]
        x3 = x1 + (x1 - x2)
        x4 = x2 + (x2 - x1)
        y3 = y1 + (y1 - y2)
        y4 = y2 + (y2 - y1)
        if part == 1:
            if 0 <= x3 < max_x and 0 <= y3 < max_y:
                antinodes.append((x3, y3))
            if 0 <= x4 < max_x and 0 <= y4 < max_y:
                antinodes.append((x4, y4))
        else:
            step = 1
            while 0 <= x3 < max_x and 0 <= y3 < max_y:
                antinodes.append((x3, y3))
                step += 1
                x3 = x1 + step * (x1 - x2)
                y3 = y1 + step * (y1 - y2)
            step = 1
            while 0 <= x4 < max_x and 0 <= y4 < max_y:
                antinodes.append((x4, y4))
                step += 1
                x4 = x2 + step * (x2 - x1)
                y4 = y2 + step * (y2 - y1)
    return antinodes


        # slope = (y1 - y2) / (x1 - x2)
        # b = (x1 * y2 - x2 * y1) / (x1 - x2)
        # for x in range(0, max_x):
        #     y = slope * x + b
        #     if float(y).is_integer() and 0 <= y < max_y:
        #         antinodes.append((x, y))


start_time = time.time()
antennas_dict, max_x, max_y = read_file('input_day8.txt')
all_antinodes = []
for i in antennas_dict:
    all_antinodes.extend(antinode(antennas_dict[i], max_x, max_y, part=1))
result = len(list(set(all_antinodes)))
print('1st part answer: ' + str(result))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
all_antinodes_part2 = []
antennas = 0
for i in antennas_dict:
    all_antinodes_part2.extend(antinode(antennas_dict[i], max_x, max_y, part=2))
    all_antinodes_part2.extend(antennas_dict[i])
result2 = len(list(set(all_antinodes_part2)))

print('2nd part answer: ' + str(result2))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
