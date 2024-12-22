import time
from itertools import product


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    return [int(k) for k in lines]


def get_next_secret_number(secret_number):
    s1 = ((secret_number * 64) ^ secret_number) % 16777216
    s2 = ((s1 // 32) ^ s1) % 16777216
    s3 = ((s2 * 2048) ^ s2) % 16777216
    return s3


start_time = time.time()

secret_numbers = read_file('input_day22.txt')
result = 0
for i in secret_numbers:
    secret_number = i
    for j in range(0, 2000):
        secret_number = get_next_secret_number(secret_number)
    result += secret_number

print('1st part answer: ' + str(result))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()

all_changes = list(product(list(range(-9, 10)), repeat=4))
result2 = 0

dct = {}
for i in all_changes:
    dct[i] = 0

for i in secret_numbers:
    secret_number = i
    changes = []
    prices = [int(str(i)[-1])]
    for j in range(0, 2000):
        secret_number_new = get_next_secret_number(secret_number)
        prices.append(int(str(secret_number_new)[-1]))
        changes.append(int(str(secret_number_new)[-1]) - int(str(secret_number)[-1]))
        secret_number = secret_number_new
    comb = []
    for ind, n in enumerate(changes[:-3]):
        if (n, changes[ind + 1], changes[ind + 2], changes[ind + 3]) not in comb:
            dct[(n, changes[ind + 1], changes[ind + 2], changes[ind + 3])] += prices[ind + 4]
            comb.append((n, changes[ind + 1], changes[ind + 2], changes[ind + 3]))


result2 = max(dct.values())

print('2nd part answer: ' + str(result2))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
