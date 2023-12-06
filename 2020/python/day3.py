def problem1(beidl):
    moves = {
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    }
    tree_map = [list(line) for line in beidl]
    posX = 0
    trees = 1
    for moveX, moveY in moves:
        trees *= check_slope(tree_map, posX, moveX, moveY)
    return trees

def check_slope(tree_map, posX, moveX, moveY):
    trees = 0
    for i in range(0, len(tree_map) - 1, +moveY):
        posX += moveX
        if posX >= len(tree_map[moveY + i]):
            posX = posX - len(tree_map[moveY])
        if tree_map[moveY + i][posX] == '#':
            trees += 1
    print(trees)
    return trees


def problem2(beidl):
    pass


if __name__ == '__main__':
    with open('../data/day3.input') as f:
        data = f.read().splitlines()
    print(problem1(data))
    print(problem2(data))
