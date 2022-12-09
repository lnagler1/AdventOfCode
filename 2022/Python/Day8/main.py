import numpy as np


def tree_house(my_input_file):
    with open(my_input_file, "r") as f:
        lines = f.read().strip().split()

    grid = [list(map(int, list(line))) for line in lines]
    n = len(grid)
    m = len(grid[0])

    np_grid = np.array(grid)
    answer = 0

    for row in range(n):
        for column in range(m):
            h = np_grid[row, column]

            # Search to the left, for bigger trees
            if column == 0 or np.amax(np_grid[row, :column]) < h:
                answer += 1
            # Search to the right, for bigger trees
            elif column == m - 1 or np.amax(np_grid[row, (column + 1):]) < h:
                answer += 1
            # Search upwards for bigger trees
            elif row == 0 or np.amax(np_grid[:row, column]) < h:
                answer += 1
            # Search downwards for bigger trees
            elif row == n - 1 or np.amax(np_grid[(row + 1):, column]) < h:
                answer += 1

    print(answer)

    # part 2

    grid = [list(map(int, list(line))) for line in lines]
    DIR = [(-1,0), (0,1), (1,0), (0,-1)]
    n = len(grid)
    m = len(grid[0])

    highest_score = 0
    for row in range(n):
        for column in range(m):
            score = 1
            for (drow, dcol) in DIR:
                distance = 1
                rr = row + drow
                cc = column + dcol
                while True:
                    if not (0 <= rr < n and 0 <= cc < m):
                        distance -= 1
                        break
                    if grid[rr][cc] >= grid[row][column]:
                        break
                    distance += 1
                    rr += drow
                    cc += dcol
                score *= distance
            highest_score = max(highest_score , score)
    print(highest_score)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tree_house("../../data/day8.input")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
