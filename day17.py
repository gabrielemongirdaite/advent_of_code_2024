import time


def combo(val, A, B, C):
    if 0 <= val <= 3:
        return val
    elif val == 4:
        return A
    elif val == 5:
        return B
    elif val == 6:
        return C


def adv(A, B, C, operand):
    return int(A / (2 ** combo(operand, A, B, C)))


def bxl(B, operand):
    return B ^ operand


def bst(A, B, C, operand):
    return combo(operand, A, B, C) % 8


def jnz(A, operand, program, pointer):
    if A == 0:
        return pointer + 2
    else:
        return operand


def run_program(program, A, B, C):
    pointer = 0
    output = []
    while pointer + 1 < len(program):
        opcode = program[pointer]
        operand = program[pointer + 1]
        if opcode == 0:
            A = adv(A, B, C, operand)
        elif opcode == 1:
            B = bxl(B, operand)
        elif opcode == 2:
            B = bst(A, B, C, operand)
        elif opcode == 3:
            pointer = jnz(A, operand, program, pointer) - 2
        elif opcode == 4:
            B = bxl(B, C)
        elif opcode == 5:
            output.append(bst(A, B, C, operand))
        elif opcode == 6:
            B = adv(A, B, C, operand)
        elif opcode == 7:
            C = adv(A, B, C, operand)
        pointer += 2
    return A, B, C, output


start_time = time.time()
A = 51342988
B = 0
C = 0
program = [2, 4, 1, 3, 7, 5, 4, 0, 1, 3, 0, 3, 5, 5, 3, 0]

A, B, C, output = run_program(program, A, B, C)
print('1st part answer: ' + str((','.join([str(x) for x in output]))))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()

step = 0
A = [0]
program_to_compare = []
while program_to_compare != program:
    program_to_compare = program[-(step + 1):]
    possibilities = []
    for a in A:
        A_tmp = a * 8
        for i in range(0, 8):
            if A_tmp + i > 0:
                if run_program(program, A_tmp + i, 0, 0)[3] == program_to_compare:
                    possibilities.append(A_tmp+i)

    A = list(set(possibilities))
    if A:
        step += 1
    else:
        break


print('2nd part answer: ' + str(A[0]))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
