import time
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    empty = lines.index('')
    wires_tmp = lines[0:empty]
    gates_tmp = lines[empty + 1:]
    wires = {}
    gates = deque()
    for i in wires_tmp:
        w, v = i.split(':')
        wires[w] = int(v)
    for i in gates_tmp:
        t, o = i.split(' -> ')
        w1, op, w2 = t.split(' ')
        gates.append((op, w1, w2, o))
    return wires, gates


def add_nodes_to_graph(gates, wires):
    G = nx.DiGraph()
    for i in gates:
        G.add_edge(i[1] + ' ' + i[0] + ' ' + i[2], i[3], weight=1)
    for i in wires:
        for j in gates:
            if i in j[1] + ' ' + j[0] + ' ' + j[2]:
                G.add_edge(i, j[1] + ' ' + j[0] + ' ' + j[2], weight=1)
    return G


def update_wires(gates_c, wires, z_wires):
    mismatch = 0
    step = 0
    while gates_c and step <= 4000:
        g = gates_c.popleft()
        if g[1] in wires and g[2] in wires:
            if g[0] == 'AND':
                wires[g[3]] = 1 if wires[g[1]] == 1 and wires[g[2]] == 1 else 0
            elif g[0] == 'OR':
                wires[g[3]] = 1 if wires[g[1]] == 1 or wires[g[2]] == 1 else 0
            else:
                wires[g[3]] = wires[g[1]] ^ wires[g[2]]
            if g[3][0] == 'z':
                mismatch += abs(wires[g[3]] - z_wires[g[3]])
        else:
            gates_c.append(g)
        step += 1
    return wires, mismatch, step


start_time = time.time()
wires, gates = read_file('input_day24.txt')
result = ''

while gates:
    g = gates.popleft()
    if g[1] in wires and g[2] in wires:
        if g[0] == 'AND':
            wires[g[3]] = 1 if wires[g[1]] == 1 and wires[g[2]] == 1 else 0
        elif g[0] == 'OR':
            wires[g[3]] = 1 if wires[g[1]] == 1 or wires[g[2]] == 1 else 0
        else:
            wires[g[3]] = wires[g[1]] ^ wires[g[2]]
    else:
        gates.append(g)

all_zs = []
all_xs = []
all_ys = []
for i in wires:
    if i[0] == 'z':
        all_zs.append(i)
    elif i[0] == 'x':
        all_xs.append(i)
    elif i[0] == 'y':
        all_ys.append(i)

for i in reversed(sorted(all_zs)):
    result += str(wires[i])

print('1st part answer: ' + str(int(result, 2)))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()

result2 = 0
wires, gates = read_file('input_day24.txt')
result_x = ''
for i in reversed(sorted(all_xs)):
    result_x += str(wires[i])

result_y = ''
for i in reversed(sorted(all_ys)):
    result_y += str(wires[i])

correct_z = "{0:b}".format(int(result_x, 2) + int(result_y, 2))
z_wires = {}
for ind, i in enumerate(correct_z[::-1]):
    if ind < 10:
        z_wires['z0' + str(ind)] = int(i)
    else:
        z_wires['z' + str(ind)] = int(i)



print('2nd part answer: ' + str(result2))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
