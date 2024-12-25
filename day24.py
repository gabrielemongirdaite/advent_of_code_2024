import time
from collections import deque


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

# by manually looking into input and considering how binary addition is done
gates_c = gates.copy()
wires_c = wires.copy()

i = [('XOR', 'ccp', 'hhw', 'fph'), ('OR', 'snp', 'mnh', 'z15')]
ind1 = gates_c.index(i[0])
ind2 = gates_c.index(i[1])
gates_c[ind1] = (i[0][0], i[0][1], i[0][2], i[1][3])
gates_c[ind2] = (i[1][0], i[1][1], i[1][2], i[0][3])

i = [('XOR', 'nsp', 'tqh', 'gds'), ('AND', 'x21', 'y21', 'z21')]
ind1 = gates_c.index(i[0])
ind2 = gates_c.index(i[1])
gates_c[ind1] = (i[0][0], i[0][1], i[0][2], i[1][3])
gates_c[ind2] = (i[1][0], i[1][1], i[1][2], i[0][3])

i = [('XOR', 'y30', 'x30', 'jrs'), ('AND', 'y30', 'x30', 'wrk')]
ind1 = gates_c.index(i[0])
ind2 = gates_c.index(i[1])
gates_c[ind1] = (i[0][0], i[0][1], i[0][2], i[1][3])
gates_c[ind2] = (i[1][0], i[1][1], i[1][2], i[0][3])

i = [('XOR', 'ksm', 'fcv', 'cqk'), ('AND', 'ksm', 'fcv', 'z34')]
ind1 = gates_c.index(i[0])
ind2 = gates_c.index(i[1])
gates_c[ind1] = (i[0][0], i[0][1], i[0][2], i[1][3])
gates_c[ind2] = (i[1][0], i[1][1], i[1][2], i[0][3])

while gates_c:
    g = gates_c.popleft()
    if g[1] in wires and g[2] in wires:
        if g[0] == 'AND':
            wires[g[3]] = 1 if wires[g[1]] == 1 and wires[g[2]] == 1 else 0
        elif g[0] == 'OR':
            wires[g[3]] = 1 if wires[g[1]] == 1 or wires[g[2]] == 1 else 0
        else:
            wires[g[3]] = wires[g[1]] ^ wires[g[2]]
    else:
        gates_c.append(g)

for i in z_wires:
    print(i, z_wires[i], wires[i])

c = sorted(['fph', 'z15', 'z21', 'gds', 'wrk', 'jrs', 'cqk', 'z34'])

print('2nd part answer: ' + str(','.join(c)))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
