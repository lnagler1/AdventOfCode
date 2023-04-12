

def part1(input_file):
    hor_pos = 0
    depth_pos = 0

    # down adds X to depth_pos
    # up subtracts X from depth_pos
    # forward adds X to hor_pos

    # To get your final Position multiply hor_pos with depth_pos
    with open(input_file, "r") as f:
        data = f.read().splitlines()

        for i in range(len(data)):
            command, value = data[i].split(" ")

            match command:
                case "forward":
                    hor_pos += int(value)
                case "down":
                    depth_pos += int(value)
                case "up":
                    depth_pos -= int(value)
        print(f"Final Position: {hor_pos * depth_pos}")


def part2(input_file):
    hor_pos = 0
    depth_pos = 0
    aim = 0

    # down adds X to aim
    # up subtracts X aim
    # forward adds X to hor_pos, increases depth_pos by aim * X

    # To get your final Position multiply hor_pos with depth_pos
    with open(input_file, "r") as f:
        data = f.read().splitlines()

        for i in range(len(data)):
            command, value = data[i].split(" ")

            match command:
                case "forward":
                    hor_pos += int(value)
                    depth_pos += aim * int(value)
                case "down":
                    aim += int(value)
                case "up":
                    aim -= int(value)
        print(f"Final Position: {hor_pos * depth_pos}")


if __name__ == '__main__':
    part1("../../data/day2.input")
    part2("../../data/day2.input")
