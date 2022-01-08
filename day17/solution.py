

def step(x, y, dx, dy):
    x += dx
    y += dy
    dx -= (dx // abs(dx)) if dx > 0 else 0
    dy -= 1
    return x, y, dx, dy


X = 0
Y = 1
DX = 2
DY = 3


def simulate(state, x_bound, y_bound, min_y):
    max_y = -999999
    while True:
        if state[Y] > max_y:
            max_y = state[Y]
        if state[DX] == 0 and state[Y] < min_y:
            return False, max_y
        if state[X] in x_bound and state[Y] in y_bound:
            return True, max_y

        state = step(*state)


def parse_input():
    with open('input.txt') as f:
        text = f.read().strip()
    area = text.split('target area: ')[1]
    def parse(s):
        return [int(i) for i in s.split('=')[1].split('..')]
    x_area, y_area = map(parse, area.split(', '))
    return (
        set(range(x_area[0], x_area[1] + 1)),
        set(range(y_area[0], y_area[1] + 1)),
    )

def solution():
    #x_bound = set(range(20, 30 + 1))
    #y_bound = set(range(-10, -5 + 1))
    #min_y = min(y_bound)
    x_bound, y_bound = parse_input()
    min_y = min(y_bound)

    max_y = -999999
    best = None
    matches = set()

    for dx in range(0, max(x_bound)+1):
        for dy in range(min(y_bound), 999+1):
            print(dx, dy)
            state = 0, 0, dx, dy
            match, sim_max_y = simulate(state, x_bound, y_bound, min_y)
            if match:
                matches.add((dx, dy))
            if match and sim_max_y > max_y:
                best = state
                max_y = sim_max_y
    print("part1", max_y)
    print("part2", len(matches), matches)


solution()
