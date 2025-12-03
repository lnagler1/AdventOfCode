def part1(input_file):
    curr_point = 50
    max = 100
    counter = 0
    with open(input_file, 'r') as f:
        data = f.read().splitlines()
        for i in range(len(data)):
            rotation = "".join([c for c in data[i] if not c.isdigit()])
            rotation_number = "".join([c for c in data[i] if c.isdigit()])

            if rotation == "L":
                curr_point -= int(rotation_number)
                if curr_point < 0:
                    if int(rotation_number) > 99:
                        curr_point += (max * (int(rotation_number) // 100))
                        if curr_point < 0:
                            curr_point += 100
                    else:
                        curr_point += max
            elif rotation == "R":
                curr_point += int(rotation_number)
                if curr_point >= max:
                    if int(rotation_number) > 99:
                        curr_point -= (max * (int(rotation_number) // 100))
                        if curr_point >= max:
                            curr_point -= 100
                    else:
                        curr_point -= max

            if curr_point == 0:
                counter += 1
            print(counter)


def part2(input_file):
    MAX_POS = 100
    curr_point = 50
    counter = 0

    with open(input_file, 'r') as f:
        data = f.read().splitlines()

        for line in data:
            direction = line[0]
            distance = int(line[1:])

            if direction == "L":
                while distance != 0:
                    if curr_point == 0:
                        curr_point = 100
                    distance -= 1
                    curr_point -= 1
                    if curr_point == 0:
                        counter += 1
            elif direction == "R":
                while distance != 0:
                    if curr_point == MAX_POS:
                        curr_point = 0
                    distance -= 1
                    curr_point += 1
                    if curr_point == MAX_POS:
                        counter += 1
            print(counter)

if __name__=='__main__':
    part1("../../data/day1.input")
