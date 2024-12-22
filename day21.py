import time
import networkx as nx
from functools import cache
from itertools import combinations, permutations


def convert_path_to_directions(path, directions):
    converted = []
    for ind, i in enumerate(path[1:]):
        for j in directions:
            if j[0] == path[ind] and j[1] == i:
                converted.append(j[2])
    return converted + ['A']


def get_path_length(path, keypad):
    length = 0
    for ind, i in enumerate(path[1:]):
        length += nx.shortest_path_length(keypad, path[ind], i, weight='weight')
    return length


def precalculate_shortest_paths_numerical(keypad, directions, r):
    dct = {}
    for i in r:
        for j in r:
            dct[(i, j)] = [list(nx.all_shortest_paths(keypad, i, j, weight='weight'))]
            dct[(i, j)].append([convert_path_to_directions(k, directions) for k in dct[(i, j)][0]])
            dct[(i, j)].append([get_path_length(k, directional_keypad) for k in dct[(i, j)][1]])
            min_len = min(dct[(i, j)][2])
            dct[(i, j)].append(dct[(i, j)][1][dct[(i, j)][2].index(min_len)])
            by_two = []
            for ind, l in enumerate(dct[(i, j)][3][:-1]):
                by_two.append((l, dct[(i, j)][3][ind + 1]))
            dct[(i, j)].append(by_two)
    return dct


def construct_path(numbers, precalculated_paths):
    path = []
    for ind, i in enumerate(numbers[1:]):
        path.extend(precalculated_paths[(numbers[ind], i)][3])
    return path


start_time = time.time()
numeric_keypad = nx.Graph()
numeric_keypad.add_edge('7', '8', weight=1)
numeric_keypad.add_edge('7', '4', weight=1)
numeric_keypad.add_edge('8', '9', weight=1)
numeric_keypad.add_edge('8', '5', weight=1)
numeric_keypad.add_edge('9', '6', weight=1)
numeric_keypad.add_edge('4', '5', weight=1)
numeric_keypad.add_edge('4', '1', weight=1)
numeric_keypad.add_edge('5', '2', weight=1)
numeric_keypad.add_edge('5', '6', weight=1)
numeric_keypad.add_edge('6', '3', weight=1)
numeric_keypad.add_edge('1', '2', weight=1)
numeric_keypad.add_edge('2', '3', weight=1)
numeric_keypad.add_edge('2', '0', weight=1)
numeric_keypad.add_edge('3', 'A', weight=1)
numeric_keypad.add_edge('0', 'A', weight=1)

directions = [('7', '8', '>'), ('7', '4', 'v'), ('8', '7', '<'), ('8', '9', '>'), ('8', '5', 'v'), \
              ('9', '8', '<'), ('9', '6', 'v'), ('4', '7', '^'), ('4', '5', '>'), ('4', '1', 'v'), \
              ('5', '8', '^'), ('5', '6', '>'), ('5', '4', '<'), ('5', '2', 'v'), ('6', '9', '^'), \
              ('6', '5', '<'), ('6', '3', 'v'), ('1', '4', '^'), ('1', '2', '>'), ('2', '5', '^'), \
              ('2', '1', '<'), ('2', '3', '>'), ('2', '0', 'v'), ('3', '6', '^'), ('3', '2', '<'), \
              ('3', 'A', 'v'), ('0', '2', '^'), ('0', 'A', '>'), ('A', '0', '<'), ('A', '3', '^')]

directional_keypad = nx.Graph()
directional_keypad.add_edge('^', 'A', weight=1)
directional_keypad.add_edge('^', 'v', weight=1)
directional_keypad.add_edge('A', '>', weight=1)
directional_keypad.add_edge('<', 'v', weight=1)
directional_keypad.add_edge('v', '>', weight=1)

directions_directional = [('^', 'A', '>'), ('^', 'v', 'v'), ('A', '^', '<'), ('A', '>', 'v'), \
                          ('<', 'v', '>'), ('v', '^', '^'), ('v', '<', '<'), ('v', '>', '>'), \
                          ('>', 'A', '^'), ('>', 'v', '<')]

spn = precalculate_shortest_paths_numerical(numeric_keypad, directions,
                                            ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A'])
spd = precalculate_shortest_paths_numerical(directional_keypad, directions_directional, ['^', '<', 'v', '>', 'A'])

result = 0
for i in ['964A', '140A', '413A', '670A', '593A']:
    path0 = construct_path(['A'] + list(i), spn)
    current_path = path0
    for l in range(1, 3):
        new_path = construct_path(['A'] + current_path, spd)
        current_path = new_path
    result += len(current_path) * int(i[:-1])

print('1st part answer: ' + str(result))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
result2 = 0
all_comb = list(permutations(['^', '<', 'v', '>', 'A'], 2))
empty_dct = {}
for l in all_comb + [('^', '^'), ('<', '<'), ('v', 'v'), ('>', '>'), ('A', 'A')]:
    empty_dct[l] = 0

for i in ['964A', '140A', '413A', '670A', '593A']:
    path0 = construct_path(['A'] + list(i), spn)
    current_path = path0
    first_element = current_path[0]
    current_path = ['A'] + current_path
    dct = empty_dct.copy()
    for ind, l in enumerate(current_path[:-1]):
        dct[(l, current_path[ind + 1])] += 1
    for l in range(1, 26):
        first_element = spd[('A', first_element)][3][0]
        dct_temp = empty_dct.copy()
        for k in dct:
            if dct[k] != 0:
                for n in spd[k][4]:
                    dct_temp[n] += dct[k]
                try:
                    dct_temp[('A', spd[k][4][0][0])] += dct[k]
                except:
                    dct_temp[('A', 'A')] += dct[k]
        dct = dct_temp
    result2 += sum(dct.values()) * int(i[:-1])

print('2nd part answer: ' + str(result2))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
