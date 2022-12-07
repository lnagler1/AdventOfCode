from copy import deepcopy


def supplyStacks(my_input_file):
    data = open(my_input_file).read()
    lines = [x for x in data.split('\n')]

    S = []
    commands = []
    for line in lines:
        print(line)
        if line == '':
            break
        sz = (len(line) + 1) // 4
        while len(S) < sz:
            S.append([])
        for i in range(len(S)):
            ch = line[1 + 4 * i]
            if ch != ' ' and 'A' <= ch <= 'Z':
                S[i].append(ch)
    print(S)

    stack1 = deepcopy(S)
    stack2 = deepcopy(S)

    found = False
    for commands in lines:
        if commands == '':
            found = True
            continue
        if not found:
            continue
        words = commands.split()
        amount_ = int(words[1])
        from_ = int(words[3]) - 1
        to_ = int(words[5]) - 1
        for (ST, do_reverve) in [(stack1, True), (stack2, False)]:  # part 1 use reverse, because the get moved from top to bottom, for part 2 no reverse because they just get taken as they are.
            MOVE = ST[from_][:amount_]
            ST[from_] = ST[from_][amount_:]
            ST[to_] = (list(reversed(MOVE)) if do_reverve else MOVE) + ST[to_]
    print(''.join([s[0] for s in stack1 if len(s) > 0]))  # part 1
    print(''.join([s[0] for s in stack2 if len(s) > 0]))  # part 2


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    supplyStacks("../../data/day5.input")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
