import time
import collections


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    group_1 = []
    group_2 = []
    for i in lines:
        k1, k2 = i.split('   ')
        group_1.append(int(k1))
        group_2.append(int(k2))
    return group_1, group_2


start_time = time.time()
g1, g2 = read_file('input_day1.txt')
g1.sort()
g2.sort()
r = 0
for ind, i in enumerate(g1):
    r += abs(i - g2[ind])
print('1st part answer: ' + str(r))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
r2 = 0
dict_g2 = collections.Counter(g2)
for i in g1:
    try:
        r2 += i * dict_g2[i]
    except:
        pass
print('2nd part answer: ' + str(r2))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
