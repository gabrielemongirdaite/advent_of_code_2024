import time


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    tmp1 = []
    tmp2 = []
    div_sections = lines.index("")
    for ind, i in enumerate(lines):
        if ind < div_sections:
            tmp1.append(i.split('|'))
        elif ind > div_sections:
            tmp2.append(i.split(','))
    order_rules = []
    updates = []
    for i in tmp1:
        order_rules.append([int(m) for m in i])
    for i in tmp2:
        updates.append([int(m) for m in i])
    return order_rules, updates


def get_elements_before_after(element, order_rules):
    elements_after = []
    elements_before = []
    for j in order_rules:
        if j[0] == element:
            elements_after.append(j[1])
        if j[1] == element:
            elements_before.append(j[0])
    return elements_after, elements_before


def get_indices(lst1, lst2):
    return [ind for ind, i in enumerate(lst1) if i in lst2]


def check_order(single_update, order_rules):
    r = 0
    broken_rules = []
    for ind, i in enumerate(single_update):
        elements_after, elements_before = get_elements_before_after(i, order_rules)
        indices_after = get_indices(single_update, elements_after)
        indices_before = get_indices(single_update, elements_before)
        indices_after_invalid = [m for m in indices_after if m < ind]
        indices_before_invalid = [m for m in indices_before if m > ind]
        if indices_after_invalid:
            for k in indices_after_invalid:
                if [i, single_update[k]] not in broken_rules:
                    broken_rules.append([i, single_update[k]])
        if indices_before_invalid:
            for k in indices_before_invalid:
                if [single_update[k], i] not in broken_rules:
                    broken_rules.append([single_update[k], i])
        if broken_rules:
            r += 1
    return r, broken_rules


start_time = time.time()
order_rules, updates = read_file('input_day5.txt')
result = 0
incorrect_updates = []
for i in updates:
    if check_order(i, order_rules)[0] == 0:
        result += i[(len(i) - 1)//2]
    else:
        incorrect_updates.append([i, check_order(i, order_rules)[1]])
print('1st part answer: ' + str(result))
print("--- %s seconds for 1st part---" % (time.time() - start_time))


start_time = time.time()
result2 = 0
for tmp in incorrect_updates:
    lst = tmp[0]
    order_to_fix = tmp[1]
    while order_to_fix:
        for i in order_to_fix:
            ind_after = lst.index(i[0])
            ind_current = lst.index(i[1])
            lst.insert(ind_after, lst.pop(ind_current))
        order_to_fix = check_order(lst, order_rules)[1]
    result2 += lst[(len(lst) - 1) // 2]
print('2nd part answer: ' + str(result2))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))