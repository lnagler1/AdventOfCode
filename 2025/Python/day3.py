def part1(input_file):
    with open(input_file, 'r') as f:
        content = f.read().splitlines()
        total_sum = 0
        for line in content:
            first_val = 0
            second_val = 0
            counter = 0
            for i in line:
                i = int(i)
                counter += 1
                if i > first_val and counter != len(line):
                    first_val = i
                    second_val = 0
                elif i > second_val:
                    second_val = i
            total_sum += int(str(first_val) + str(second_val))
        print(total_sum)


if __name__=='__main__':
    part1("../data/day3.input")
