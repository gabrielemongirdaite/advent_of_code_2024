import time


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    return lines[0]


def convert_to_blocks(compressed_string):
    block = []
    for ind, i in enumerate(compressed_string):
        if ind % 2 == 0:  # file
            block.extend([str(ind // 2)] * int(i))
        else:  # empty space
            block.extend(['.'] * int(i))
    return block


def convert_to_blocks_part2(compressed_string):
    block = []
    for ind, i in enumerate(compressed_string):
        if int(i) != 0:
            if ind % 2 == 0:  # file
                block.append([str(ind // 2), int(i)])
            else:  # empty space
                block.append(['.', int(i)])
    return block


def rearrange(block):
    updated_block = block.copy()
    length = len(block)
    for ind, i in enumerate(block[::-1]):
        empty_index = updated_block.index('.')
        if empty_index >= length - 1 - ind:
            break
        if i != '.':
            updated_block[empty_index] = i
            updated_block[length - 1 - ind] = '.'
    return updated_block


def rearrange_part2(block):
    updated_block = block.copy()
    for ind, i in enumerate(block[::-1]):
        for ind2, j in enumerate(updated_block):
            if i[0] != '.':
                if j[0] == '.' and j[1] >= i[1]:
                    updated_block.insert(ind2, i)
                    if j[1] == i[1]:
                        updated_block.pop(ind2 + 1)
                    else:
                        updated_block[ind2 + 1] = [j[0], j[1] - i[1]]
                    index_to_update = [ind for ind, m in enumerate(updated_block) if m == [i[0], i[1]]]
                    updated_block[index_to_update[-1]] = ['.', i[1]]
                    break
    return updated_block


start_time = time.time()
disk_input = read_file('input_day9.txt')
block = convert_to_blocks(disk_input)
updated = rearrange(block)
result = 0
for ind, i in enumerate(updated):
    if i != '.':
        result += ind * int(i)
print('1st part answer: ' + str(result))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
block_part2 = convert_to_blocks_part2(disk_input)
updated_part2 = rearrange_part2(block_part2)
result2 = 0

convert_to_list = []
for i in updated_part2:
    convert_to_list.extend([i[0]] * i[1])

for ind, i in enumerate(convert_to_list):
    if i != '.':
        result2 += ind * int(i)

print('2nd part answer: ' + str(result2))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
