import time
import networkx as nx
from itertools import combinations


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    return lines


def add_nodes_to_graph(connections):
    G = nx.Graph()
    for i in connections:
        k1, k2 = i.split('-')
        G.add_edge(k1, k2, weight=1)
    return G


start_time = time.time()

connections = read_file('input_day23.txt')
connections_graph = add_nodes_to_graph(connections)
DI_connections_graph = nx.DiGraph(connections_graph)
ls_cycles = list(nx.simple_cycles(DI_connections_graph, 3))
seen = []
result = 0
interconnected_3 = []

for i in ls_cycles:
    if len(i) == 3:
        if set(i) not in seen:
            seen.append(set(i))
            for n in set(i):
                if n[0] == 't':
                    result += 1
                    interconnected_3.append(i)
                    break

print('1st part answer: ' + str(result))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
dct = {}
for i in seen:
    dct[tuple(i)] = []
result2 = [0]

candidates = []
cand = []
for i in dct:
    ls1 = [n[1] for n in DI_connections_graph.edges(i[0])]
    ls2 = [n[1] for n in DI_connections_graph.edges(i[1])]
    ls3 = [n[1] for n in DI_connections_graph.edges(i[2])]
    inter = set(ls1) & set(ls2) & set(ls3)
    if set(list(i) + list(inter)) not in candidates:
        candidates.append(set(list(i) + list(inter)))


for i in candidates:
    loop = 0
    comb = list(combinations(i, 2))
    for n in comb:
        try:
            nx.path_weight(DI_connections_graph, list(n), weight='weight')
            loop += 1
        except:
            pass
        if loop == len(comb):
            cand.append([len(i), ','.join(sorted(i))])

for i in cand:
    result2 = i if i[0]>result2[0] else result2

print('2nd part answer: ' + str(result2[1]))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
