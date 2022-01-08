def f(numbers, acc):
    if len(numbers) < 2:
        return acc
    else:
        a, b, *rest = numbers
        acc = acc + int(a < b)
        return f([b] + rest, acc)


l = [199,
     200,
     208,
     210,
     200,
     207,
     240,
     269,
     260,
     263,
     ]

#print(f(l, 0))

numbers = map(int, open("sample.txt").read().strip().split("\n"))


def g(last, numbers):
    if numbers == []:
        return 0
    else:
        current, *rest = numbers
        return int(last < current) + g(current, rest)


print(g(999999, numbers))
