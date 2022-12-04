# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi():
    score_map = {"X": 1, "A": 1, "Y": 2, "B": 2, "Z": 3, "C": 3}
    battle_map = {
        ("A", "X"): 3,
        ("A", "Y"): 6,
        ("A", "Z"): 0,
        ("B", "X"): 0,
        ("B", "Y"): 3,
        ("B", "Z"): 6,
        ("C", "X"): 6,
        ("C", "Y"): 0,
        ("C", "Z"): 3,
    }

    point_managment = {(k[0], v): k[1] for k, v in battle_map.items()}

    ## manage for Part 2, if you have X you want to lose so 0 points, with Y you want to tie so 3 points
    ## with Z you want to win so 6 points.
    manage = {"X": 0, "Y": 3, "Z": 6}
    print(point_managment)

    with open("../../data/day2Input.txt") as f:
        part1 = 0
        part2 = 0
        for line in f:
            enemy_hand, my_hand = line.strip().split(" ")
            part1 += score_map[my_hand] + battle_map[(enemy_hand, my_hand)]
            part2 += score_map[point_managmcmdent[(enemy_hand, manage[my_hand])]] + manage[my_hand]
        print(part1)
        print(part2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
