import time
from itertools import *
from collections import Counter
import shapely


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    return lines


def find_regions(regions_map):
    dct = {}
    for y, i in enumerate(regions_map):
        for x, j in enumerate(i):
            try:
                dct[j].append((x, y))
            except:
                dct[j] = [(x, y)]
    return dct


def nearby_plots(plot):
    return [(plot[0] + 1, plot[1]), (plot[0] - 1, plot[1]), (plot[0], plot[1] + 1), (plot[0], plot[1] - 1)]


def split_regions(region):
    regions = []
    while region:
        for i in region:
            seen = 0
            for j in regions:
                if i in j:
                    seen += 1
            if seen == 0:
                region_tmp = [i]
                nearby_plots_tmp = nearby_plots(i)
                added = True
                region_tmp_len = len(region_tmp)
                while added:
                    for j in region:
                        if j in nearby_plots_tmp:
                            region_tmp.append(j)
                            nearby_plots_tmp.extend(nearby_plots(j))
                            nearby_plots_tmp = list(set(nearby_plots_tmp))
                    region_tmp = list(set(region_tmp))
                    region_tmp.sort()
                    if len(region_tmp) > region_tmp_len:
                        region_tmp_len = len(region_tmp)
                    else:
                        added = False
                # region_tmp = list(set(region_tmp))
                # region_tmp.sort()
                for i in region_tmp:
                    region.remove(i)
                regions.append(region_tmp)
    return regions  # list(unique_everseen(regions, key=frozenset))


def calculate_perimeter(region):
    perimeter = 0
    for i in region:
        for j in nearby_plots(i):
            if j not in region:
                perimeter += 1
    return perimeter


def count_corners(region):
    corners = 0
    for l in region:
        k = 0
        corner = 0
        nearby = []
        for i in nearby_plots(l):
            if i in region:
                k += 1
                nearby.append(i)
        if k == 2 and abs(nearby[0][0] - nearby[1][0] <= 1) and abs(nearby[0][1] - nearby[1][1] <= 1):
            corner += 1
        elif k == 1:
            corner += 2
        if ((l[0], l[1] - 1) in region) and ((l[0] - 1, l[1]) in region) and ((l[0] - 1, l[1] - 1) not in region):
            corner += 1
        if ((l[0], l[1] - 1) in region) and ((l[0] + 1, l[1]) in region) and ((l[0] + 1, l[1] - 1) not in region):
            corner += 1
        if ((l[0], l[1] + 1) in region) and ((l[0] - 1, l[1]) in region) and ((l[0] - 1, l[1] + 1) not in region):
            corner += 1
        if ((l[0], l[1] + 1) in region) and ((l[0] + 1, l[1]) in region) and ((l[0] + 1, l[1] + 1) not in region):
            corner += 1
        corners += corner
    return corners


start_time = time.time()
regions_map = read_file('input_day12.txt')
regions = find_regions(regions_map)

separate_regions = []
for i in regions:
    new_regions = split_regions(regions[i])
    separate_regions.extend(new_regions)

result = 0
for i in separate_regions:
    perimeter = calculate_perimeter(i)
    result += len(i) * perimeter

print('1st part answer: ' + str(result))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
result2 = 0

for i in separate_regions:
    result2 += len(i) * (count_corners(i) if len(i) > 1 else 4)

print('2nd part answer: ' + str(result2))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
