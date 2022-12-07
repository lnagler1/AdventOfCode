# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from collections import defaultdict


def getDirectories(my_input_file):
    data = open(my_input_file).read().strip()
    lines = [x for x in data.split('\n')]

    size_dictionary = defaultdict(int)
    path = []
    for line in lines:
        words = line.strip().split()
        if words[1] == "cd":
            if words[2] == '..':
                path.pop()
            else:
                path.append(words[2])
        elif words[1] == "ls":
            continue
        elif words[0] == "dir":
            continue
        else:
            size = int(words[0])
            for i in range(1, len(path) + 1):
                size_dictionary['/'.join(path[:i])] += size

    max_used = 70000000 - 30000000
    total_used = size_dictionary['/']
    need_to_have = total_used - max_used

    part1 = 0;
    part2 = 1e9;
    for k, v in size_dictionary.items():
        if v <= 100000:
            part1 += v
        if v >= need_to_have:
            part2 = min(part2, v)
    print(part1)
    print(part2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    getDirectories("../../data/day7.input")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
