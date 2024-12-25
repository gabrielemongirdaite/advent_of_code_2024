import time


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    locks = []
    keys = []
    s = 0
    while s < len(lines):
        print(lines[s])
        if lines[s] == '#####':
            dct = {}
            dct[0] = 0
            dct[1] = 0
            dct[2] = 0
            dct[3] = 0
            dct[4] = 0
            for i in range(1, 7):
                for ind, j in enumerate(lines[s + i]):
                    if j == '#':
                        dct[ind] += 1
            locks.append(list(dct.values()))
        else:
            dct = {}
            dct[0] = 0
            dct[1] = 0
            dct[2] = 0
            dct[3] = 0
            dct[4] = 0
            for i in range(0, 6):
                for ind, j in enumerate(lines[s + i]):
                    if j == '#':
                        dct[ind] += 1
            keys.append(list(dct.values()))
        s += 8
    return locks, keys


start_time = time.time()
locks, keys = read_file('input_day25.txt')
fits = 0
for i in locks:
    for j in keys:
        if i[0] + j[0] <= 5 and i[1] + j[1] <= 5 and i[2] + j[2] <= 5 and i[3] + j[3] <= 5 and i[4] + j[4] <= 5:
            fits += 1

print('1st part answer: ' + str(fits))
print("--- %s seconds for 1st part---" % (time.time() - start_time))
