# Problem summary: Given a list of passwords, check if they are valid
# Part 1: Check if the password contains the given letter at least min and at most max times
# Part 2: Check if the password contains the given letter at position pos1 or pos2, but not both (XOR)

def problem1(beidl):
    i = 0
    for line in beidl:
        count, letter_a, password = line.split()
        letter = letter_a.split(':')[0]
        min, max = count.split('-')
        # Check if the password contains the given letter at least min and at most max times
        if int(min) <= password.count(letter) <= int(max):
            i += 1
    return i

def problem2(beidl):
    i = 0
    for line in beidl:
        positions, letters, password = line.split()
        letter = letters.split(':')[0]
        pos1, pos2 = positions.split('-')
        if validate_password(password, letter, pos1, pos2):
            i += 1
    return i

def validate_password(password, letter, pos1, pos2):
    # Check if the password contains the given letter at position pos1 or pos2, but not both (XOR)
    return (password[int(pos1) - 1] == letter) ^ (password[int(pos2) - 1] == letter)


if __name__ == '__main__':
    with open('../data/day2.input') as f:
        data = f.readlines()
    print(problem1(data))
    print(problem2(data))
