# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def turningTrouble(my_input_file):
    data = open(my_input_file).read()

    found_p1 = False
    found_p2 = False
    for i in range(len(data)):
        if (not found_p1) and i - 3 >= 0 and len(set([data[i - j] for j in range(4)])) == 4:
            print(i + 1)
            found_p1 = True
        if (not found_p2) and i - 13 >= 0 and len(set(data[i - j] for j in range(14))) == 14:
            print(i + 1)
            found_p2 = True

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    turningTrouble("../../data/day6.input")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
