from collections import deque
from time import time


def parse_input():
    with open('input.txt') as f:
        text = f.read()

    return [int(i) for i in text.split(',')]


def simulate_day(ocean):
    zeros = ocean.popleft()
    ocean.append(zeros)
    ocean[6] += zeros


def solution(timers):
    timers = sorted(timers)
    ocean = deque([0] * 9)
    for timer in timers:
        ocean[timer] += 1

    for _ in range(80):
        simulate_day(ocean)
    print("part1", sum(ocean))

    for _ in range(256 - 80):
        simulate_day(ocean)
    print("part2", sum(ocean))


part1(parse_input())
