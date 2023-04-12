import numpy as np


def part1(input_file):
    with open(input_file, 'r') as f:
        data = f.read().splitlines()

        counter = 0
        previous_entry = 0
        for i in data:
            if previous_entry != 0:
                max_entry = max(previous_entry, int(i))
                if max_entry == int(i):
                    counter += 1
            previous_entry = int(i)
        print(counter)


def part2(input_file):
    with open(input_file, 'r') as f:
        measurements = [int(line.strip()) for line in f]
        sliding_windows = np.convolve(measurements, np.ones(3), 'valid')

        prev_entry = sliding_windows[0]
        increases = 0
        for entry in sliding_windows[1:]:
            if entry > prev_entry:
                increases += 1
            prev_entry = entry
        print(increases)


if __name__ == '__main__':
    part1('../../data/day1.input')
    part2('../../data/day1.input')
