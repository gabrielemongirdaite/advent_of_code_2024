import time
from collections import Counter


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    return lines[0].split(' ')


def stones_rules(stones):
    new_stones = []
    for i in stones:
        if i == '0':
            new_stones.append('1')
        elif len(i) % 2 == 0:
            new_stones.extend([str(int(i[:(len(i) // 2)])), str(int(i[(len(i) // 2):]))])
        else:
            new_stones.append(str(int(i) * 2024))
    return new_stones


def single_stone(stone):
    new_stones = []
    if stone == '0':
        new_stones.append('1')
    elif len(stone) % 2 == 0:
        new_stones.extend([str(int(stone[:(len(stone) // 2)])), str(int(stone[(len(stone) // 2):]))])
    else:
        new_stones.append(str(int(stone) * 2024))
    return new_stones


start_time = time.time()
stones = read_file('input_day11.txt')
result = 0

for i in stones:
    tmp_stones = [i]
    for k in range(0, 25):
        tmp_stones = stones_rules(tmp_stones)
    result += len(tmp_stones)

print('1st part answer: ' + str(result))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
result2 = 0
dct_stones = Counter(stones)
for k in range(0, 75):
    tmp_stones = {}
    for l in dct_stones:
        ss = single_stone(l)
        if ss[0] in tmp_stones:
            tmp_stones[ss[0]] += dct_stones[l]
        else:
            tmp_stones[ss[0]] = dct_stones[l]
        if len(ss) == 2:
            if ss[1] in tmp_stones:
                tmp_stones[ss[1]] += dct_stones[l]
            else:
                tmp_stones[ss[1]] = dct_stones[l]
    dct_stones = tmp_stones

for i in dct_stones:
    result2 += dct_stones[i]

print('2nd part answer: ' + str(result2))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
