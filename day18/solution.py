from pprint import pprint


int_glyphs = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}


def snailfish_parse(s, index, depth):
    pair = []
    acc = None
    while index < len(s):
        c = s[index]
        index += 1
        if c == ']':
            assert depth > 0, depth
            pair.append(acc)
            return list(pair), index
        elif c in int_glyphs:
            assert type(acc) is int or acc is None, acc
            if acc is None:
                acc = 0
            acc *= 10
            acc += int(c)
        elif c == '[':
            acc, index = snailfish_parse(s, index, depth + 1)
        elif c == ',':
            pair.append(acc)
            acc = None
        else:
            raise ValueError(c)
    assert depth == 0, depth
    return list(acc)


def find_parent(lr, parents, stack):
    if parents == []:
        return lambda _1, _2: None
    else:
        parent, *rest = parents
        if type(parent[lr]) is int:
            orig_n = parent[lr]
            def addn(addn_parents, n):
                for i in stack:
                    addn_parents = addn_parents[i]
                #print((stack, orig_n, addn_parents[lr]))
                addn_parents[lr] += n
            return addn
        else:
            assert type(parent[lr]) is list
            return find_parent(lr, rest, stack[1:])


def _snailfish_reduce(snailfish, parents, stack, gen):
    for vi, v in enumerate(snailfish):
        if type(v) is int:
            yield v
        elif type(v) is list:
            if len(parents) == 3:
                assert all(type(i) is int for i in v)
                for i, n in enumerate(v):
                    addn = find_parent(i, [snailfish] + parents, stack)
                    gen.append((addn, n))
                yield 0
            else:
                yield list(_snailfish_reduce(v, [snailfish] + parents, stack + [vi], gen))


def snailfish_reduce(snailfish):
    explode = []
    new_snailfish = list(_snailfish_reduce(snailfish, [], [], explode))
    for f, n in explode:
        f(new_snailfish, n)
    return new_snailfish


explode_reductions = [
    (
        [[[[[9,8],1],2],3],4],
        [[[[0,9],2],3],4]
    ),
    (
        [7,[6,[5,[4,[3,2]]]]],
        [7,[6,[5,[7,0]]]]
    ),
    (
        [[6,[5,[4,[3,2]]]],1],
        [[6,[5,[7,0]]],3]
    ),
    (
        [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]],
        [[3,[2,[8,0]]],[9,[5,[7,0]]]]
    ),
]

for value, expected in explode_reductions:
    actual = snailfish_reduce(value)
    try:
        assert actual == expected
    except:
        pprint(expected)
        pprint(actual)
        raise



t = [[[[[9,8],1],2],3],4]
t = [[6,[5,[4,[3,2]]]],1]

l = []

print(ns)

print(ns)
