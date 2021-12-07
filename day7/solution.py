def parse_input():
    with open('input.txt') as f:
        return [int(i) for i in f.read().strip().split(',')]


def solution():
    positions = sorted(parse_input())
    median = positions[len(positions) // 2]
    part1_fuel = sum(abs(median - i) for i in positions)
    print("part1", part1_fuel)

    mean = int(sum(positions) / len(positions))
    part2_fuel = sum(
        sum(j + 1 for j in range(abs(i - mean)))
        for i in positions
    )
    print("part2", part2_fuel)

solution()
