def recursive1(last, numbers):
    if numbers == []:
        return 0
    else:
        current, *rest = numbers
        return int(last < current) + recursive1(current, rest)


def recursive(text):
    return recursive1(9999999, map(int, text.split()))
