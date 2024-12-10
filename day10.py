import time


def check_value(value, target_value, x, y, lst):
    if value == target_value:
        lst.append((x, y))
    return lst


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    zeros = []
    ones = []
    twos = []
    threes = []
    fours = []
    fives = []
    sixs = []
    sevens = []
    eights = []
    nines = []
    for y, i in enumerate(lines):
        for x, j in enumerate(i):
            check_value(j, '0', x, y, zeros)
            check_value(j, '1', x, y, ones)
            check_value(j, '2', x, y, twos)
            check_value(j, '3', x, y, threes)
            check_value(j, '4', x, y, fours)
            check_value(j, '5', x, y, fives)
            check_value(j, '6', x, y, sixs)
            check_value(j, '7', x, y, sevens)
            check_value(j, '8', x, y, eights)
            check_value(j, '9', x, y, nines)
    return zeros, ones, twos, threes, fours, fives, sixs, sevens, eights, nines


def nearby_coordinations(x, y):
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]


def update_trail(trail_updated, next_step, step):
    trail = trail_updated.copy()
    for ind, i in enumerate(trail):
        for j in nearby_coordinations(i[-1][0], i[-1][1]):
            if j in next_step:
                trail[ind].append(j)

    trail_updated = []
    for i in trail:
        if len(i) == step:
            trail_updated.append(i)
        elif len(i) > step:
            for j in i[step - 1:]:
                tmp = i[:step - 1]
                tmp.append(j)
                trail_updated.append(tmp)
    return trail_updated


start_time = time.time()
zeros, ones, twos, threes, fours, fives, sixs, sevens, eights, nines = read_file('input_day10.txt')
trail = zeros.copy()
for ind, i in enumerate(trail):
    trail[ind] = [trail[ind]]
    for j in nearby_coordinations(i[0], i[1]):
        if j in ones:
            trail[ind].append(j)

trail_updated = []
for i in trail:
    if len(i) == 2:
        trail_updated.append(i)
    elif len(i) > 2:
        for j in i[1:]:
            tmp = i[:1]
            tmp.append(j)
            trail_updated.append(tmp)

trail_updated = update_trail(trail_updated, twos, 3)
trail_updated = update_trail(trail_updated, threes, 4)
trail_updated = update_trail(trail_updated, fours, 5)
trail_updated = update_trail(trail_updated, fives, 6)
trail_updated = update_trail(trail_updated, sixs, 7)
trail_updated = update_trail(trail_updated, sevens, 8)
trail_updated = update_trail(trail_updated, eights, 9)
trail_updated = update_trail(trail_updated, nines, 10)

distinct_9 = []
for i in trail_updated:
    distinct_9.append((i[0], i[-1]))
result = len(set(distinct_9))

print('1st part answer: ' + str(result))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()

result2 = len(trail_updated)

print('2nd part answer: ' + str(result2))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
