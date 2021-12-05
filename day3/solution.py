def parse_input():
    with open("input.txt") as f:
        input = f.read().split()

    bits = len(input[0])
    yield bits
    for line in input:
        yield int(line, 2)


def part1():
    bits, *report = parse_input()
    gamma = 0
    epsilon = 0

    bit_ix = 0
    while bit_ix < bits:
        count = [0, 0]
        for item in report:
            bit = (item >> bit_ix) & 1
            count[bit] += 1

        if count[1] > count[0]:
            gamma |= (1 << bit_ix)
        if count[0] > count[1]:
            epsilon |= (1 << bit_ix)

        bit_ix += 1

    print("part1", gamma * epsilon)


def keep_bit(s, bit_ix, keep):
    if len(s) == 1:
        return
    for n in list(s):
        if ((n >> bit_ix) & 1) != keep:
            s.remove(n)


def part2():
    bits, *report = parse_input()
    gamma = set(report)
    epsilon = set(report)

    bit_ix = bits
    while bit_ix > 0:
        bit_ix -= 1

        count = [0, 0]
        for item in epsilon:
            bit = (item >> bit_ix) & 1
            count[bit] += 1

        if count[1] > count[0]:
            keep_bit(epsilon, bit_ix, 0)
        elif count[0] > count[1]:
            keep_bit(epsilon, bit_ix, 1)
        elif count[0] == count[1]:
            keep_bit(epsilon, bit_ix, 0)

    bit_ix = bits
    while bit_ix > 0:
        bit_ix -= 1

        count = [0, 0]
        for item in gamma:
            bit = (item >> bit_ix) & 1
            count[bit] += 1

        if count[1] > count[0]:
            keep_bit(gamma, bit_ix, 1)
        elif count[0] > count[1]:
            keep_bit(gamma, bit_ix, 0)
        elif count[0] == count[1]:
            keep_bit(gamma, bit_ix, 1)

    oxygen, = gamma
    co2, = epsilon
    print("part2", oxygen * co2)

part1()
part2()
