import time
from sympy import solve
from sympy.abc import x, y
import re


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    parameters = []
    k = 0
    while k + 4 <= len(lines):
        tmp = []
        for i in range(k, k + 4):
            tmp.extend(re.findall(r'\d+', lines[i]))
        k += 4
        parameters.append([int(m) for m in tmp])
    return parameters


start_time = time.time()
result = 0
eq_param = read_file('input_day13.txt')
for i in eq_param:
    dct_tmp = solve([i[0] * x + i[2] * y - i[4], i[1] * x + i[3] * y - i[5]], (x, y), dict=True)[0]
    if float(dct_tmp[x]).is_integer() and float(dct_tmp[y]).is_integer():
        result += dct_tmp[x] * 3 + dct_tmp[y]

print('1st part answer: ' + str(result))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
result2 = 0
for i in eq_param:
    dct_tmp = solve([i[0] * x + i[2] * y - (10000000000000 + i[4]), i[1] * x + i[3] * y - (10000000000000 + i[5])] \
                    , (x, y), dict=True)[0]
    if float(dct_tmp[x]).is_integer() and float(dct_tmp[y]).is_integer():
        result2 += dct_tmp[x] * 3 + dct_tmp[y]

print('2nd part answer: ' + str(result2))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
