import time
import itertools


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    reports = []
    for i in lines:
        reports.append(list(map(int, i.split(' '))))
    return reports


def check_if_ascending(l):
    l1 = l.copy()
    l1.sort()
    return l == l1


def check_if_descending(l):
    l1 = l.copy()
    l1.sort(reverse=True)
    return l == l1


def check_levels(l):
    l1 = l[:-1]
    l2 = l[1:]
    sub_l = [a - b for a, b in zip(l2, l1)]
    return 1 if max(sub_l) <= 3 and min(sub_l) >= 1 else 0


def problem_dampener(l):
    safe = 0
    for comb in itertools.combinations(l, len(l) - 1):
        if check_if_ascending(list(comb)):
            safe += check_levels(list(comb))
        elif check_if_descending(list(comb)):
            safe += check_levels(list(comb)[::-1])
        else:
            pass
    return safe


start_time = time.time()
reports = read_file('input_day2.txt')
r = 0
for i in reports:
    if check_if_ascending(i):
        r += check_levels(i)
    elif check_if_descending(i):
        r += check_levels(i[::-1])
    else:
        pass

print('1st part answer: ' + str(r))
print("--- %s seconds for 1st part---" % (time.time() - start_time))


start_time = time.time()
r2 = 0
for i in reports:
    r2 += 1 if problem_dampener(i) > 0 else 0

print('2nd part answer: ' + str(r2))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
