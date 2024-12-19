import time
from collections import deque


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    patterns = lines[0].split(', ')
    designs = lines[2:]
    return patterns, designs


def match_design(patterns, design):
    q = deque()
    q.append(('', 0))
    while q:
        curr = q.popleft()
        if curr[1] == len(design):
            return 1
        for i in patterns:
            pattern_length = len(i)
            if i == design[curr[1]:curr[1] + pattern_length]:
                if (curr[0] + i, curr[1] + pattern_length) not in q:
                    q.append((curr[0] + i, curr[1] + pattern_length))

    return 0


def match_design_part2(patterns, design):
    q = deque()
    q.append(['', 0, 1])
    matching = 0
    relevant_patterns = []
    for i in patterns:
        if i in design:
            relevant_patterns.append(i)
    while q:
        curr = q.popleft()
        if curr[0] == design:
            matching += curr[2]
        for i in relevant_patterns:
            pattern_length = len(i)
            if i == design[curr[1]:curr[1] + pattern_length]:
                q.append([curr[0] + i, curr[1] + pattern_length, curr[2]])
        distinct_patterns = []
        for i in q:
            distinct_patterns.append(i[0])
        distinct_patterns = list(set(distinct_patterns))
        q_new = deque()
        for ind, i in enumerate(distinct_patterns):
            q_new.append([i, len(i), 0])
            for j in q:
                if i == j[0]:
                    q_new[ind][2] += j[2]
        q = q_new
    return matching


start_time = time.time()

patterns, designs = read_file('input_day19.txt')

result = 0
for i in designs:
    result += match_design(patterns, i)

print('1st part answer: ' + str(result))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()

result2 = 0

for ind, i in enumerate(designs):
    result2 += match_design_part2(patterns, i)


print('2nd part answer: ' + str(result2))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
