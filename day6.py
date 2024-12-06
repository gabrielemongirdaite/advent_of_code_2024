import time
import copy


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    return lines


def starting_position(lab_map):
    for y, i in enumerate(lab_map):
        for x, j in enumerate(i):
            if j == '^':
                return (x, y)


def going_next_step(current_step, guard_direction):
    if guard_direction == '^':
        tmp_next_step = (current_step[0], current_step[1] - 1)
    elif guard_direction == '>':
        tmp_next_step = (current_step[0] + 1, current_step[1])
    elif guard_direction == 'v':
        tmp_next_step = (current_step[0], current_step[1] + 1)
    elif guard_direction == '<':
        tmp_next_step = (current_step[0] - 1, current_step[1])
    return tmp_next_step


def guard_path(lab_map, guard_start):
    next_step = (guard_start[0], guard_start[1] - 1)
    max_x = len(lab_map[0])
    max_y = len(lab_map)
    guard_direction = '^'
    steps = [(guard_start, guard_direction)]
    loop = 0
    while 0 <= next_step[0] < max_x \
            and 0 <= next_step[1] < max_y:
        steps.append((next_step, guard_direction))
        tmp_next_step = going_next_step(next_step, guard_direction)
        try:
            while lab_map[tmp_next_step[1]][tmp_next_step[0]] == '#' and tmp_next_step[0] >= 0\
                    and tmp_next_step[1] >= 0:
                if guard_direction == '^':
                    guard_direction = '>'
                elif guard_direction == '>':
                    guard_direction = 'v'
                elif guard_direction == 'v':
                    guard_direction = '<'
                elif guard_direction == '<':
                    guard_direction = '^'
                tmp_next_step = going_next_step(next_step, guard_direction)
        except:
            pass
        next_step = tmp_next_step
        if (next_step, guard_direction) in steps:
            loop += 1
            break
    return steps, loop


start_time = time.time()
lab_map = read_file('input_day6.txt')
guard_start = starting_position(lab_map)
all_steps, loop = guard_path(lab_map, guard_start)
positions = []
for i in all_steps:
    positions.append(i[0])
print(all_steps)
print('1st part answer: ' + str(len(set(positions))))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
loops = 0

for ind, i in enumerate(list(set(positions))):
    new_lab_map = copy.deepcopy(lab_map)
    new_string = lab_map[i[1]][:i[0]] + '#' + lab_map[i[1]][i[0] + 1:]
    new_lab_map[i[1]] = new_string
    cnt_loop = guard_path(new_lab_map, guard_start)[1]
    if cnt_loop > 0:
        loops += 1
    print(ind, i, loops)


print('2nd part answer: ' + str(loops))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
