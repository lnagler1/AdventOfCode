# This is a sample Python script.
import string
from itertools import zip_longest


# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def part1(my_input):
    value_lower_case = {chr(i + 96): i for i in range(1, 27)}
    value_upper_case = {chr(i + 38): i for i in range(27, 53)}
    allValues = {}
    allValues.update(value_lower_case)
    allValues.update(value_upper_case)

    with open(my_input) as f:
        count = 0
        for line in f:
            length = len(line)
            first_comp = slice(0, length // 2)
            second_comp = slice(length // 2, length)
            for letter in line[first_comp]:
                if letter in line[second_comp]:
                    count += allValues[letter]
                    break
        return count


def part2(my_input):
    value_lower_case = {chr(i + 96): i for i in range(1, 27)}
    value_upper_case = {chr(i + 38): i for i in range(27, 53)}
    allValues = {}
    allValues.update(value_lower_case)
    allValues.update(value_upper_case)

    with open(my_input) as f:
        count = 0
        for next_n_lines in zip_longest(*[f] * 3):

            backpack1 = next_n_lines[0].strip()
            backpack2 = next_n_lines[1].strip()
            backpack3 = next_n_lines[2].strip()
            for letter in backpack1:
                if letter in backpack2:
                    if letter in backpack3:
                        count += allValues[letter]
                        break
        return count


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(part1("../../data/day3.test"))
    print(part1("../../data/day3.input"))
    print(part2("../../data/day3.test"))
    print(part2("../../data/day3.input"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
