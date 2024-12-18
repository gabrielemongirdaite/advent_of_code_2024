import time
import networkx as nx


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    b = []
    for i in lines:
        x, y = i.split(',')
        b.append((int(x), int(y)))
    return b


def add_nodes_to_graph(bytes, len_x, len_y):
    G = nx.DiGraph()
    for y in range(0, len_y):
        for x in range(0, len_x):
            current_point = y * len_y + x
            if y < len_y - 1:  # south
                if (y + 1, x) not in bytes:
                    G.add_edge(current_point, (y + 1) * len_y + x, weight=1)
            if y >= 1:  # north
                if (y - 1, x) not in bytes:
                    G.add_edge(current_point, (y - 1) * len_y + x, weight=1)
            if x < len_x - 1:  # east
                if (y, x + 1) not in bytes:
                    G.add_edge(current_point, y * len_y + x + 1, weight=1)
            if x >= 1:  # west
                if (y, x - 1) not in bytes:
                    G.add_edge(current_point, y * len_y + x - 1, weight=1)
    return G


start_time = time.time()
bytes = read_file('input_day18.txt')

graph_part1 = add_nodes_to_graph(bytes[0:1024], 71, 71)

result = nx.shortest_path_length(graph_part1, 0 * 71 + 0, 70 * 71 + 70, weight='weight')

print('1st part answer: ' + str(result))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()

for i in range(3032, len(bytes) + 1):
    try:
        graph = add_nodes_to_graph(bytes[0:i], 71, 71)
        path = nx.shortest_path_length(graph, 0 * 71 + 0, 70 * 71 + 70, weight='weight')
    except:
        print(i, bytes[i-1])
        break

graph = add_nodes_to_graph(bytes[0:3032], 71, 71)
nx.shortest_path_length(graph, 0 * 71 + 0, 70 * 71 + 70, weight='weight')

try:
    graph = add_nodes_to_graph(bytes[0:3033], 71, 71)
    nx.shortest_path_length(graph, 0 * 71 + 0, 70 * 71 + 70, weight='weight')
except:
    result2 = bytes[0:3033][-1]

print('2nd part answer: ' + str(result2))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
