import time
from itertools import product


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    equations = []
    for i in lines:
        t, n = i.split(': ')
        numbers = n.split(' ')
        numbers = [int(m) for m in numbers]
        equations.append([int(t), numbers])
    return equations


def evaluate_equation_part1(equation):
    possible_combinations = list(product(['+', '*'], repeat=len(equation[1]) - 1))
    for i in possible_combinations:
        r = equation[1][0]
        for ind, j in enumerate(equation[1][1:]):
            if i[ind] == '+':
                r += j
            else:
                r *= j
        if r == equation[0]:
            return equation[0]
    return 0


def evaluate_equation_part2(equation):
    possible_combinations = list(product(['+', '*', '||'], repeat=len(equation[1]) - 1))
    for i in possible_combinations:
        r = equation[1][0]
        for ind, j in enumerate(equation[1][1:]):
            if i[ind] == '+':
                r += j
            elif i[ind] == '*':
                r *= j
            else:
                r = r * (10 ** len(str(j))) + j
        if r == equation[0]:
            return equation[0]
    return 0


start_time = time.time()
equations = read_file('input_day7.txt')
result = 0
not_solved = []
for i in equations:
    r = evaluate_equation_part1(i)
    result += r
    if r == 0:
        not_solved.append(i)
print('1st part answer: ' + str(result))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
result2 = 0
for i in not_solved:
    r2 = evaluate_equation_part2(i)
    result2 += r2

print('2nd part answer: ' + str(result+result2))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))