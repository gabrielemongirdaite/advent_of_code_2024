import time
import re


def read_file(file_name, part=1):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    walls = []
    boxes = []
    boxes_start = []
    boxes_end = []
    movements = []
    robot = []
    empty_line = lines.index('')
    for y, i in enumerate(lines):
        if y > empty_line:
            movements.extend(i)
        if part == 1:
            for x, j in enumerate(i):
                if j == '#':
                    walls.append((x, y))
                elif j == 'O':
                    boxes.append((x, y))
                elif j == '@':
                    robot.append((x, y))
        else:
            if y < empty_line:
                i_tmp = re.sub('O', '[', i)
                shifted_i = re.sub('O', ']', i)
                new_i = [k for l in zip(i_tmp, shifted_i) for k in l]
                for x, j in enumerate(new_i):
                    if j == '#':
                        walls.append((x, y))
                    elif j == '[':
                        boxes_start.append((x, y))
                    elif j == ']':
                        boxes_end.append((x, y))
                    elif j == '@':
                        robot.append((x, y))

    return walls, boxes, min(robot), movements, boxes_start, boxes_end


def find_closest_wall(robot, walls, direction):
    possible_walls = []
    if direction == '^':
        for i in walls:
            if robot[0] == i[0] and robot[1] > i[1]:
                possible_walls.append(i)
        if possible_walls:
            return max((possible_walls))
    elif direction == '>':
        for i in walls:
            if robot[1] == i[1] and robot[0] < i[0]:
                possible_walls.append(i)
        if possible_walls:
            return min((possible_walls))
    elif direction == 'v':
        for i in walls:
            if robot[0] == i[0] and robot[1] < i[1]:
                possible_walls.append(i)
        if possible_walls:
            return min((possible_walls))
    else:
        for i in walls:
            if robot[1] == i[1] and robot[0] > i[0]:
                possible_walls.append(i)
        if possible_walls:
            return max((possible_walls))


def find_closest_empty_space(robot, closest_wall, direction, boxes):
    if direction == '^':
        for y in range(robot[1] - 1, closest_wall[1], -1):
            if (robot[0], y) not in boxes:
                return (robot[0], y)
    elif direction == '>':
        for x in range(robot[0] + 1, closest_wall[0]):
            if (x, robot[1]) not in boxes:
                return (x, robot[1])
    elif direction == 'v':
        for y in range(robot[1] + 1, closest_wall[1]):
            if (robot[0], y) not in boxes:
                return (robot[0], y)
    else:
        for x in range(robot[0] - 1, closest_wall[0], -1):
            if (x, robot[1]) not in boxes:
                return (x, robot[1])


def move_boxes(robot, closest_empty, direction, boxes):
    if direction == '^':
        for i in range(closest_empty[1], robot[1]):
            if (robot[0], i) in boxes:
                boxes[boxes.index((robot[0], i))] = (robot[0], i - 1)
        robot = (robot[0], robot[1] - 1)
    elif direction == '>':
        for i in range(closest_empty[0], robot[0], -1):
            if (i, robot[1]) in boxes:
                boxes[boxes.index((i, robot[1]))] = (i + 1, robot[1])
        robot = (robot[0] + 1, robot[1])
    elif direction == 'v':
        for i in range(closest_empty[1], robot[1], -1):
            if (robot[0], i) in boxes:
                boxes[boxes.index((robot[0], i))] = (robot[0], i + 1)
        robot = (robot[0], robot[1] + 1)
    else:
        for i in range(closest_empty[0], robot[0]):
            if (i, robot[1]) in boxes:
                boxes[boxes.index((i, robot[1]))] = (i - 1, robot[1])
        robot = (robot[0] - 1, robot[1])
    return boxes, robot


def find_all_touching_boxes(robot, direction, boxes_start, boxes_end):
    touching_boxes_start = []
    touching_boxes_end = []
    if direction == '^':
        if (robot[0], robot[1] - 1) in boxes_start:
            touching_boxes_start.append((robot[0], robot[1] - 1))
            touching_boxes_end.append((robot[0] + 1, robot[1] - 1))
        elif (robot[0], robot[1] - 1) in boxes_end:
            touching_boxes_end.append((robot[0], robot[1] - 1))
            touching_boxes_start.append((robot[0] - 1, robot[1] - 1))
        added = True
        len_boxes = len(touching_boxes_start)
        while added:
            tmp_start = []
            tmp_end = []
            for j in touching_boxes_start + touching_boxes_end:
                if (j[0], j[1] - 1) in boxes_start:
                    tmp_start.append((j[0], j[1] - 1))
                    tmp_end.append((j[0] + 1, j[1] - 1))
                elif (j[0], j[1] - 1) in boxes_end:
                    tmp_end.append((j[0], j[1] - 1))
                    tmp_start.append((j[0] - 1, j[1] - 1))
            touching_boxes_start.extend(tmp_start)
            touching_boxes_end.extend(tmp_end)
            touching_boxes_start = list(set(touching_boxes_start))
            touching_boxes_end = list(set(touching_boxes_end))
            if len(touching_boxes_start) > len_boxes:
                len_boxes = len(touching_boxes_start)
            else:
                added = False
    elif direction == '>':
        if (robot[0] + 1, robot[1]) in boxes_start:
            touching_boxes_start.append((robot[0] + 1, robot[1]))
            touching_boxes_end.append((robot[0] + 2, robot[1]))
        added = True
        len_boxes = len(touching_boxes_start)
        while added:
            tmp_start = []
            tmp_end = []
            for j in touching_boxes_start + touching_boxes_end:
                if (j[0] + 1, j[1]) in boxes_start:
                    tmp_start.append((j[0] + 1, j[1]))
                    tmp_end.append((j[0] + 2, j[1]))
            touching_boxes_start.extend(tmp_start)
            touching_boxes_end.extend(tmp_end)
            touching_boxes_start = list(set(touching_boxes_start))
            touching_boxes_end = list(set(touching_boxes_end))
            if len(touching_boxes_start) > len_boxes:
                len_boxes = len(touching_boxes_start)
            else:
                added = False
    if direction == 'v':
        if (robot[0], robot[1] + 1) in boxes_start:
            touching_boxes_start.append((robot[0], robot[1] + 1))
            touching_boxes_end.append((robot[0] + 1, robot[1] + 1))
        elif (robot[0], robot[1] + 1) in boxes_end:
            touching_boxes_end.append((robot[0], robot[1] + 1))
            touching_boxes_start.append((robot[0] - 1, robot[1] + 1))
        added = True
        len_boxes = len(touching_boxes_start)
        while added:
            tmp_start = []
            tmp_end = []
            for j in touching_boxes_start + touching_boxes_end:
                if (j[0], j[1] + 1) in boxes_start:
                    tmp_start.append((j[0], j[1] + 1))
                    tmp_end.append((j[0] + 1, j[1] + 1))
                elif (j[0], j[1] + 1) in boxes_end:
                    tmp_end.append((j[0], j[1] + 1))
                    tmp_start.append((j[0] - 1, j[1] + 1))
            touching_boxes_start.extend(tmp_start)
            touching_boxes_end.extend(tmp_end)
            touching_boxes_start = list(set(touching_boxes_start))
            touching_boxes_end = list(set(touching_boxes_end))
            if len(touching_boxes_start) > len_boxes:
                len_boxes = len(touching_boxes_start)
            else:
                added = False
    elif direction == '<':
        if (robot[0] - 1, robot[1]) in boxes_end:
            touching_boxes_end.append((robot[0] - 1, robot[1]))
            touching_boxes_start.append((robot[0] - 2, robot[1]))
        added = True
        len_boxes = len(touching_boxes_start)
        while added:
            tmp_start = []
            tmp_end = []
            for j in touching_boxes_start + touching_boxes_end:
                if (j[0] - 1, j[1]) in boxes_end:
                    tmp_end.append((j[0] - 1, j[1]))
                    tmp_start.append((j[0] - 2, j[1]))
            touching_boxes_start.extend(tmp_start)
            touching_boxes_end.extend(tmp_end)
            touching_boxes_start = list(set(touching_boxes_start))
            touching_boxes_end = list(set(touching_boxes_end))
            if len(touching_boxes_start) > len_boxes:
                len_boxes = len(touching_boxes_start)
            else:
                added = False
    return touching_boxes_start, touching_boxes_end


def wall_in_the_way(direction, robot, touching_boxes, walls):
    k = 0
    if direction == '^':
        # print('tb', touching_boxes)
        for i in [robot] + touching_boxes:
            # print('touching_walls', i, walls)
            if (i[0], i[1] - 1) in walls:
                k += 1
    elif direction == '>':
        for i in [robot] + touching_boxes:
            if (i[0] + 1, i[1]) in walls:
                k += 1
    elif direction == 'v':
        for i in [robot] + touching_boxes:
            if (i[0], i[1] + 1) in walls:
                k += 1
    elif direction == '<':
        # print('tb', touching_boxes)
        for i in [robot] + touching_boxes:
            if (i[0] - 1, i[1]) in walls:
                k += 1
    return k


start_time = time.time()
walls, boxes, robot, movement, _, _ = read_file('input_day15.txt')

for i in movement:
    closest_wall = find_closest_wall(robot, walls, i)
    closest_empty = find_closest_empty_space(robot, closest_wall, i, boxes)
    if closest_empty:
        boxes, robot = move_boxes(robot, closest_empty, i, boxes)

result = 0
for i in boxes:
    result += i[1] * 100 + i[0]

print('1st part answer: ' + str(result))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
result2 = 0
walls, _, robot, _, boxes_start, boxes_end = read_file('input_day15.txt', 2)

for i in movement:
    # print(i, boxes_start, robot)
    touching_boxes_start, touching_boxes_end = find_all_touching_boxes(robot, i, boxes_start, boxes_end)
    k = wall_in_the_way(i, robot, touching_boxes_start + touching_boxes_end, walls)
    if k == 0:
        if i == '^':
            robot = (robot[0], robot[1] - 1)
            for l in touching_boxes_start:
                boxes_start[boxes_start.index(l)] = (l[0], l[1] - 1)
            for l in touching_boxes_end:
                boxes_end[boxes_end.index(l)] = (l[0], l[1] - 1)
        elif i == '>':
            robot = (robot[0] + 1, robot[1])
            for l in touching_boxes_start:
                boxes_start[boxes_start.index(l)] = (l[0] + 1, l[1])
            for l in touching_boxes_end:
                boxes_end[boxes_end.index(l)] = (l[0] + 1, l[1])
        elif i == 'v':
            robot = (robot[0], robot[1] + 1)
            for l in touching_boxes_start:
                boxes_start[boxes_start.index(l)] = (l[0], l[1] + 1)
            for l in touching_boxes_end:
                boxes_end[boxes_end.index(l)] = (l[0], l[1] + 1)
        elif i == '<':
            robot = (robot[0] - 1, robot[1])
            for l in touching_boxes_start:
                boxes_start[boxes_start.index(l)] = (l[0] - 1, l[1])
            for l in touching_boxes_end:
                boxes_end[boxes_end.index(l)] = (l[0] - 1, l[1])

xs = []
ys = []
for i in walls:
    xs.append(i[0])
    ys.append(i[1])

max_x = max(xs)
max_y = max(ys)

for i in boxes_start:
    result2 += i[1] * 100 + i[0]

print('2nd part answer: ' + str(result2))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
