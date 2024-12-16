import time
import dijkstar
import networkx as nx


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    return lines


def add_nodes_to_graph(maze):
    graph = dijkstar.Graph()
    for y, i in enumerate(maze):
        for x, j in enumerate(i):
            current_point = y * len(maze) + x
            if y < len(maze) - 1:  # south
                if maze[y + 1][x] != '#':
                    graph.add_edge((current_point, 'S'), ((y + 1) * len(maze) + x, 'S'), 1)
                    graph.add_edge((current_point, 'W'), ((y + 1) * len(maze) + x, 'S'), 1001)
                    graph.add_edge((current_point, 'E'), ((y + 1) * len(maze) + x, 'S'), 1001)
            if y >= 1:  # north
                if maze[y - 1][x] != '#':
                    graph.add_edge((current_point, 'N'), ((y - 1) * len(maze) + x, 'N'), 1)
                    graph.add_edge((current_point, 'W'), ((y - 1) * len(maze) + x, 'N'), 1001)
                    graph.add_edge((current_point, 'E'), ((y - 1) * len(maze) + x, 'N'), 1001)
            if x < len(maze[0]) - 1:  # east
                if maze[y][x + 1] != '#':
                    graph.add_edge((current_point, 'E'), (y * len(maze) + x + 1, 'E'), 1)
                    graph.add_edge((current_point, 'N'), (y * len(maze) + x + 1, 'E'), 1001)
                    graph.add_edge((current_point, 'S'), (y * len(maze) + x + 1, 'E'), 1001)
            if x >= 1:  # west
                if maze[y][x - 1] != '#':
                    graph.add_edge((current_point, 'W'), (y * len(maze) + x - 1, 'W'), 1)
                    graph.add_edge((current_point, 'N'), (y * len(maze) + x - 1, 'W'), 1001)
                    graph.add_edge((current_point, 'S'), (y * len(maze) + x - 1, 'W'), 1001)
    return graph


def add_nodes_to_graph_part2(maze):
    G = nx.DiGraph()
    for y, i in enumerate(maze):
        for x, j in enumerate(i):
            current_point = y * len(maze) + x
            if y < len(maze) - 1:  # south
                if maze[y + 1][x] != '#':
                    G.add_edge((current_point, 'S'), ((y + 1) * len(maze) + x, 'S'), weight=1)
                    G.add_edge((current_point, 'W'), ((y + 1) * len(maze) + x, 'S'), weight=1001)
                    G.add_edge((current_point, 'E'), ((y + 1) * len(maze) + x, 'S'), weight=1001)
            if y >= 1:  # north
                if maze[y - 1][x] != '#':
                    G.add_edge((current_point, 'N'), ((y - 1) * len(maze) + x, 'N'), weight=1)
                    G.add_edge((current_point, 'W'), ((y - 1) * len(maze) + x, 'N'), weight=1001)
                    G.add_edge((current_point, 'E'), ((y - 1) * len(maze) + x, 'N'), weight=1001)
            if x < len(maze[0]) - 1:  # east
                if maze[y][x + 1] != '#':
                    G.add_edge((current_point, 'E'), (y * len(maze) + x + 1, 'E'), weight=1)
                    G.add_edge((current_point, 'N'), (y * len(maze) + x + 1, 'E'), weight=1001)
                    G.add_edge((current_point, 'S'), (y * len(maze) + x + 1, 'E'), weight=1001)
            if x >= 1:  # west
                if maze[y][x - 1] != '#':
                    G.add_edge((current_point, 'W'), (y * len(maze) + x - 1, 'W'), weight=1)
                    G.add_edge((current_point, 'N'), (y * len(maze) + x - 1, 'W'), weight=1001)
                    G.add_edge((current_point, 'S'), (y * len(maze) + x - 1, 'W'), weight=1001)
    return G


start_time = time.time()
maze = read_file('input_day16.txt')

for y, i in enumerate(maze):
    for x, j in enumerate(i):
        if j == 'S':
            start_x, start_y = x, y
        elif j == 'E':
            end_x, end_y = x, y

graph_part1 = add_nodes_to_graph(maze)

starting_point = start_y * len(maze) + start_x
ending_point = end_y * len(maze) + end_x
result = []

try:
    result.append(dijkstar.find_path(graph_part1, (starting_point, 'E'), (ending_point, 'E'))[3])
except:
    pass

try:
    result.append(dijkstar.find_path(graph_part1, (starting_point, 'E'), (ending_point, 'S'))[3])
except:
    pass

try:
    result.append(dijkstar.find_path(graph_part1, (starting_point, 'E'), (ending_point, 'W'))[3])
except:
    pass

try:
    result.append(dijkstar.find_path(graph_part1, (starting_point, 'E'), (ending_point, 'N'))[3])
except:
    pass

best_path = min(result)
print('1st part answer: ' + str(best_path))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()

graph_part2 = add_nodes_to_graph_part2(maze)
result2 = []

try:
    for p in nx.all_shortest_paths(graph_part2, (starting_point, 'E'), (ending_point, 'E'), weight='weight'):
        if nx.path_weight(graph_part2, p, weight='weight') == best_path:
            for i in p:
                result2.append(i[0])
except:
    pass

try:
    for p in nx.all_shortest_paths(graph_part2, (starting_point, 'E'), (ending_point, 'S'), weight='weight'):
        if nx.path_weight(graph_part2, p, weight='weight') == best_path:
            for i in p:
                result2.append(i[0])
except:
    pass

try:
    for p in nx.all_shortest_paths(graph_part2, (starting_point, 'E'), (ending_point, 'W'), weight='weight'):
        if nx.path_weight(graph_part2, p, weight='weight') == best_path:
            for i in p:
                result2.append(i[0])
except:
    pass

try:
    for p in nx.all_shortest_paths(graph_part2, (starting_point, 'E'), (ending_point, 'N'), weight='weight'):
        if nx.path_weight(graph_part2, p, weight='weight') == best_path:
            for i in p:
                result2.append(i[0])
except:
    pass

result2 = list(set(result2))

print('2nd part answer: ' + str(len(result2)))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
