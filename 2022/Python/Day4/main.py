# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def part1(my_input_file):
    with open(my_input_file) as f:
        duplicates = 0
        for line in f:

            first_elf, second_elf = line.strip().split(",")

            if contains(first_elf, second_elf) or contains(second_elf, first_elf):
                duplicates += 1

        return duplicates

def contains(first, second):
    first_start = first.split("-")[0]
    first_end = first.split("-")[1]
    second_start = second.split("-")[0]
    second_end = second.split("-")[1]

    return first_start <= second_start and first_end >= second_end

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(part1("../../data/day4.test"))
    print(part1("../../data/day4.input"))

