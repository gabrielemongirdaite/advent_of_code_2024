import time
import re


def find_indices(full_string, k1, k2):
    return full_string.index("mul(" + k1 + "," + k2 + ")")


def read_file(file_name):
    text_file = open(file_name, "r")
    full_string = text_file.read()
    lines = full_string.split('mul(')
    possible_instructions = []
    r = []
    for i in lines:
        if i[0].isdigit():
            possible_instructions.append(i)
    for i in possible_instructions:
        try:
            k1, k2 = i.split(')')[0].split(',')
            r.append((int(k1) * int(k2), find_indices(full_string, k1, k2)))
        except:
            pass
    return r, full_string


def find_all_indices(full_string, search_string):
    return [m.start() for m in re.finditer(search_string, full_string)]


def donts_intervals(donts, dos):
    intervals = []
    for ind, i in enumerate(dos):
        for j in donts:
            if ind == 0 and j < i:
                intervals.append(range(j, i))
            elif i > j > dos[ind - 1]:
                intervals.append(range(j, i))
    return intervals


start_time = time.time()
r, full_string = read_file('input_day3.txt')
result = 0
for i in r:
    result += i[0]
print('1st part answer: ' + str(result))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
donts = find_all_indices(full_string, "don't\(\)")
dos = find_all_indices(full_string, "do\(\)")
intervals = donts_intervals(donts, dos)
result2 = 0
for i in r:
    tmp = 0
    for k in intervals:
        if i[1] in k:
            tmp += 1
    if tmp == 0:
        result2 += i[0]
print('2nd part answer: ' + str(result2))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
