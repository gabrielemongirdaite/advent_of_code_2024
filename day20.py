import time
import networkx as nx


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    return lines


def add_nodes_to_graph(race):
    G = nx.DiGraph()
    for y, i in enumerate(race):
        for x, j in enumerate(i):
            if j != '#':
                current_point = y * len(race) + x
                if y < len(race) - 1:  # south
                    if race[y + 1][x] != '#':
                        G.add_edge(current_point, (y + 1) * len(race) + x, weight=1)
                if y >= 1:  # north
                    if race[y - 1][x] != '#':
                        G.add_edge(current_point, (y - 1) * len(race) + x, weight=1)
                if x < len(race[0]) - 1:  # east
                    if race[y][x + 1] != '#':
                        G.add_edge(current_point, y * len(race) + x + 1, weight=1)
                if x >= 1:  # west
                    if race[y][x - 1] != '#':
                        G.add_edge(current_point, y * len(race) + x - 1, weight=1)
    return G


def cheat(current_point, graph, race, to_save):
    x = current_point % len(race)
    y = current_point // len(race)
    cheated_paths = 0
    if y < len(race) - 2:  # south
        if race[y + 1][x] == '#' and race[y + 2][x] != '#':
            cheated_paths += 1 if nx.shortest_path_length(graph, current_point, (y + 2) * len(race) + x,
                                                          weight='weight') - 2 >= to_save else 0
    if y >= 2:  # north
        if race[y - 1][x] == '#' and race[y - 2][x] != '#':
            cheated_paths += 1 if nx.shortest_path_length(graph, current_point, (y - 2) * len(race) + x,
                                                          weight='weight') - 2 >= to_save else 0
    if x < len(race[0]) - 2:  # east
        if race[y][x + 1] == '#' and race[y][x + 2] != '#':
            cheated_paths += 1 if nx.shortest_path_length(graph, current_point, y * len(race) + x + 2,
                                                          weight='weight') - 2 >= to_save else 0
    if x >= 2:  # west
        if race[y][x - 1] == '#' and race[y][x - 2] != '#':
            cheated_paths += 1 if nx.shortest_path_length(graph, current_point, y * len(race) + (x - 2),
                                                          weight='weight') - 2 >= to_save else 0
    return cheated_paths / 2


start_time = time.time()
race = read_file('input_day20.txt')

for y, i in enumerate(race):
    for x, j in enumerate(i):
        if j == 'S':
            start_x, start_y = x, y
        elif j == 'E':
            end_x, end_y = x, y

graph_part1 = add_nodes_to_graph(race)

starting_point = start_y * len(race) + start_x
ending_point = end_y * len(race) + end_x

shortest_path = nx.shortest_path(graph_part1, starting_point, ending_point, weight='weight')
result = 0
for i in shortest_path:
    result += cheat(i, graph_part1, race, 100)

print('1st part answer: ' + str(result))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()

result2 = 0
to_save = 100
for ind, i in enumerate(shortest_path):
    for ind2, j in enumerate(shortest_path[ind + to_save:]):
        ind_j = ind2 + to_save
        p = abs((i % len(race)) - (j % len(race))) + abs((i // len(race)) - (j // len(race)))
        if ind_j - p >= to_save and p <= 20:
            result2 += 1

print('2nd part answer: ' + str(result2))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
