# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def getDuplicates(my_input_file):
    data = open(my_input_file).read().strip()
    lines = [x.strip() for x in data.split('\n')]
    # with open(my_input_file) as f:
    part1 = 0
    part2 = 0
    for line in lines:

        first_elf, second_elf = line.strip().split(",")

        if contains(first_elf, second_elf) or contains(second_elf, first_elf):
            part1 += 1
        if doesOverlap(first_elf, second_elf):
            part2 += 1

    print(part1)
    print(part2)


def contains(first, second):
    first_start, first_end = first.split("-")
    second_start, second_end = second.split("-")
    first_start, first_end, second_start, second_end = [int(x) for x in [first_start, first_end, second_start, second_end]]

    return first_start <= second_start and second_end <= first_end

def doesOverlap(first, second):
    first_start, first_end = first.split("-")
    second_start, second_end = second.split("-")
    first_start, first_end, second_start, second_end = [int(x) for x in [first_start, first_end, second_start, second_end]]

    return not(first_end < second_start or first_start > second_end)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    (getDuplicates("../../data/day4.test"))
    (getDuplicates("../../data/day4.input"))  # richtige Lösung wäre 471
