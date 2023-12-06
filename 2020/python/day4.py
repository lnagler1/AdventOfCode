def problem1(beidl):
    i = 0

    for line in beidl.split("\n\n"):
        if validate_passport(line):
            i += 1
    return i


def validate_passport(passport):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for field in required_fields:
        if field in passport:
            start = passport.find(field)
            print(passport[start:].split()[0].split(':')[1])
        if field not in passport:
            return False
    return True


def problem2(beidl):
    pass


if __name__ == "__main__":
    with open('../data/day4.input') as f:
        data = f.read()
    print(problem1(data))
    print(problem2(data))