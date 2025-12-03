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


def part2_better_solution(input_file):
    with open(input_file, 'r') as f:
        content = f.read().splitlines()
        total_sum = 0
        for line in content:
            val = 0
            start = 0
            for n in range(12):
                c = max(line[start : len(line) - 12 + n  +1])
                start = line.index(c, start) + 1
                val = 10 * val + int(c)
            total_sum += val
        print(total_sum)


def part2_my_solution(input_file):
    total_sum = 0
    target_length = 12

    with open(input_file, 'r') as f:
        lines = f.read().splitlines()

        for line in lines:
            to_remove = len(line) - target_length

            stack = []
            for digit in line:
                while to_remove > 0 and stack and stack[-1] < digit:
                    stack.pop()
                    to_remove -= 1
                stack.append(digit)

            while to_remove > 0:
                stack.pop()
                to_remove -= 1

            total_sum += int("".join(stack))

        return total_sum



if __name__=='__main__':
    part1("../data/day3.input")
    part2_better_solution("../data/day3.input")
    print(part2_my_solution("../data/day3.input"))
