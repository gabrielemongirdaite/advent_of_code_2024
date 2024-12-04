import time


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    return lines


def find_all_x(puzzle, searc_ch):
    x_coordinates = []
    for y, l in enumerate(puzzle):
        for x, s in enumerate(l):
            if s == searc_ch:
                x_coordinates.append((x, y))
    return x_coordinates


def east_from_x(x_coordinate, puzzle):
    max_x = len(puzzle[0])
    max_y = len(puzzle)
    if x_coordinate[0] + 3 < max_x:
        if puzzle[x_coordinate[1]][x_coordinate[0] + 1] == 'M' \
                and puzzle[x_coordinate[1]][x_coordinate[0] + 2] == 'A' \
                and puzzle[x_coordinate[1]][x_coordinate[0] + 3] == 'S':
            return 1
    return 0


def south_east_from_x(x_coordinate, puzzle):
    max_x = len(puzzle[0])
    max_y = len(puzzle)
    if x_coordinate[0] + 3 < max_x and x_coordinate[1] + 3 < max_y:
        if puzzle[x_coordinate[1] + 1][x_coordinate[0] + 1] == 'M' \
                and puzzle[x_coordinate[1] + 2][x_coordinate[0] + 2] == 'A' \
                and puzzle[x_coordinate[1] + 3][x_coordinate[0] + 3] == 'S':
            return 1
    return 0


def south_from_x(x_coordinate, puzzle):
    max_x = len(puzzle[0])
    max_y = len(puzzle)
    if x_coordinate[1] + 3 < max_y:
        if puzzle[x_coordinate[1] + 1][x_coordinate[0]] == 'M' \
                and puzzle[x_coordinate[1] + 2][x_coordinate[0]] == 'A' \
                and puzzle[x_coordinate[1] + 3][x_coordinate[0]] == 'S':
            return 1
    return 0


def south_west_from_x(x_coordinate, puzzle):
    max_x = len(puzzle[0])
    max_y = len(puzzle)
    if x_coordinate[0] - 3 >= 0 and x_coordinate[1] + 3 < max_y:
        if puzzle[x_coordinate[1] + 1][x_coordinate[0] - 1] == 'M' \
                and puzzle[x_coordinate[1] + 2][x_coordinate[0] - 2] == 'A' \
                and puzzle[x_coordinate[1] + 3][x_coordinate[0] - 3] == 'S':
            return 1
    return 0


def west_from_x(x_coordinate, puzzle):
    max_x = len(puzzle[0])
    max_y = len(puzzle)
    if x_coordinate[0] - 3 >= 0:
        if puzzle[x_coordinate[1]][x_coordinate[0] - 1] == 'M' \
                and puzzle[x_coordinate[1]][x_coordinate[0] - 2] == 'A' \
                and puzzle[x_coordinate[1]][x_coordinate[0] - 3] == 'S':
            return 1
    return 0


def north_west_from_x(x_coordinate, puzzle):
    max_x = len(puzzle[0])
    max_y = len(puzzle)
    if x_coordinate[0] - 3 >= 0 and x_coordinate[1] - 3 >= 0:
        if puzzle[x_coordinate[1] - 1][x_coordinate[0] - 1] == 'M' \
                and puzzle[x_coordinate[1] - 2][x_coordinate[0] - 2] == 'A' \
                and puzzle[x_coordinate[1] - 3][x_coordinate[0] - 3] == 'S':
            return 1
    return 0


def north_from_x(x_coordinate, puzzle):
    max_x = len(puzzle[0])
    max_y = len(puzzle)
    if x_coordinate[1] - 3 >= 0:
        if puzzle[x_coordinate[1] - 1][x_coordinate[0]] == 'M' \
                and puzzle[x_coordinate[1] - 2][x_coordinate[0]] == 'A' \
                and puzzle[x_coordinate[1] - 3][x_coordinate[0]] == 'S':
            return 1
    return 0


def north_east_from_x(x_coordinate, puzzle):
    max_x = len(puzzle[0])
    max_y = len(puzzle)
    if x_coordinate[0] + 3 < max_x and x_coordinate[1] - 3 >= 0:
        if puzzle[x_coordinate[1] - 1][x_coordinate[0] + 1] == 'M' \
                and puzzle[x_coordinate[1] - 2][x_coordinate[0] + 2] == 'A' \
                and puzzle[x_coordinate[1] - 3][x_coordinate[0] + 3] == 'S':
            return 1
    return 0


def x_mas(a_coordinate, puzzle):
    max_x = len(puzzle[0])
    max_y = len(puzzle)
    # M.M M.S S.S S.M
    # .A. .A. .A. .A.
    # S.S M.S M.M S.M
    if a_coordinate[0] + 1 < max_x and a_coordinate[1] + 1 < max_y \
            and a_coordinate[0] - 1 >= 0 and a_coordinate[1] - 1 >= 0:
        if (puzzle[a_coordinate[1] - 1][a_coordinate[0] - 1] == 'M' \
            and puzzle[a_coordinate[1] - 1][a_coordinate[0] + 1] == 'M'\
            and puzzle[a_coordinate[1] + 1][a_coordinate[0] - 1] == 'S' \
            and puzzle[a_coordinate[1] + 1][a_coordinate[0] + 1] == 'S') \
            or (puzzle[a_coordinate[1] - 1][a_coordinate[0] - 1] == 'M' \
            and puzzle[a_coordinate[1] - 1][a_coordinate[0] + 1] == 'S'\
            and puzzle[a_coordinate[1] + 1][a_coordinate[0] - 1] == 'M' \
            and puzzle[a_coordinate[1] + 1][a_coordinate[0] + 1] == 'S') \
            or (puzzle[a_coordinate[1] - 1][a_coordinate[0] - 1] == 'S' \
            and puzzle[a_coordinate[1] - 1][a_coordinate[0] + 1] == 'S'\
            and puzzle[a_coordinate[1] + 1][a_coordinate[0] - 1] == 'M' \
            and puzzle[a_coordinate[1] + 1][a_coordinate[0] + 1] == 'M') \
            or (puzzle[a_coordinate[1] - 1][a_coordinate[0] - 1] == 'S' \
            and puzzle[a_coordinate[1] - 1][a_coordinate[0] + 1] == 'M'\
            and puzzle[a_coordinate[1] + 1][a_coordinate[0] - 1] == 'S' \
            and puzzle[a_coordinate[1] + 1][a_coordinate[0] + 1] == 'M'):
            return 1
    return 0

start_time = time.time()
puzzle = read_file('input_day4.txt')
all_x = find_all_x(puzzle, 'X')
r = 0
for i in all_x:
    r += east_from_x(i, puzzle)
    r += south_east_from_x(i, puzzle)
    r += south_from_x(i, puzzle)
    r += south_west_from_x(i, puzzle)
    r += west_from_x(i, puzzle)
    r += north_west_from_x(i, puzzle)
    r += north_from_x(i, puzzle)
    r += north_east_from_x(i, puzzle)

print('1st part answer: ' + str(r))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
all_a = find_all_x(puzzle, 'A')
r2 = 0
for i in all_a:
    r2 += x_mas(i, puzzle)
print('2nd part answer: ' + str(r2))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
