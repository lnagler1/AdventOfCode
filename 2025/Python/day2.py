import os

def invalid_part1(x):
    s = str(x)
    n = len(s)
    return n % 2 == 0 and s[:n//2] == s[n//2:]

def invalid_part2(x):
    s = str(x)
    return s in (s + s)[1:-1]

def part1(input_file):
    with open(input_file, 'r') as f:
        content = f.read().strip()
        ranges = content.split(',')
        total_sum = 0

        for r in ranges:
            first_id_str, last_id_str = r.split('-')
            first_id = int(first_id_str)
            last_id = int(last_id_str)

            for x in range(first_id, last_id + 1):
                if invalid_part1(x):
                    total_sum += x

        print(f"Part 1 Answer: {total_sum}")


def part2(input_file):
    with open(input_file, 'r') as f:
        content = f.read().strip()
        ranges = content.split(',')
        total_sum = 0

        for r in ranges:
            first_id_str, last_id_str = r.split('-')
            first_id = int(first_id_str)
            last_id = int(last_id_str)

            for x in range(first_id, last_id + 1):
                if invalid_part2(x):
                    total_sum += x

        print(f"Part 2 Answer: {total_sum}")


if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, "../data/day2.input")

    part1(input_path)
    part2(input_path)