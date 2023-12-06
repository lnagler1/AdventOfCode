with open('../data/day1.input') as f:
    num = f.readlines()
num = [int(i.split('\n')[0]) for i in num]

print("Solution: 1\n")
for i in num:
    if 2020-i in num:
        print(i, 2020-i, i*(2020-i))

print("\nSolution: 2\n")
for i in num:
    for j in num:
        if (2020 - i - j) in num:
            print(2020 - i - j, i, j, i*j*(2020-i-j))
