from binascii import unhexlify
from collections import namedtuple
from functools import reduce


Literal = namedtuple('Literal', ['version', 'type_id', 'value'])
Operator = namedtuple('Operator', ['version', 'type_id', 'packets'])


def parse_input():
    with open('input.txt') as f:
        line = f.read().strip()

    return unhexlify(line)


def bit_index(b, ix):
    byte_ix = ix // 8
    bit_ix = ix % 8
    try:
        return (b[byte_ix] >> (7 - bit_ix)) & 1
    except IndexError:
        raise IndexError((b, byte_ix, bit_ix))


def bit_slice(b, start, length):
    assert length > 0
    n = 0
    for offset, bit_ix in enumerate(range(start, start + length)):
        bit = bit_index(b, bit_ix)
        n |= (bit << (length - offset - 1))
    return n


def decode_literal(packet, offset):
    n = 0
    while True:
        bit = bit_index(packet, offset)
        offset += 1
        nib = bit_slice(packet, offset, 4)
        offset += 4
        n = (n << 4) + nib
        if bit == 0:
            break
    return n, offset


def decode_operator(packet, offset):
    length_type_id = bit_index(packet, offset)
    offset += 1

    length_bits = 11 if length_type_id == 1 else 15

    length = bit_slice(packet, offset, length_bits)
    offset += length_bits

    offset_end = offset + length
    packet_count = 0

    decoding = (
        (lambda: packet_count != length)
        if length_type_id == 1 else
        (lambda: offset != offset_end)
    )
    while decoding():
        if length_type_id == 0:
            assert offset < offset_end
        sub_packet, offset = decode_packet(packet, offset)
        yield sub_packet
        packet_count += 1
    yield offset


def decode_packet(packet, offset):
    version = bit_slice(packet, offset, 3)
    offset += 3
    type_id = bit_slice(packet, offset, 3)
    offset += 3

    if type_id == 4:
        value, offset = decode_literal(packet, offset)
        return Literal(version, type_id, value), offset
    else:
        *packets, offset = decode_operator(packet, offset)
        return Operator(version, type_id, packets), offset

samples = [
    #('D2FE28', ),
    #('38006F45291200', ),
    #('EE00D40C823060', ),
    ('8A004A801A8002F478', 16),
    ('620080001611562C8802118E34', 12),
    ('C0015000016115A2E0802F182340', 23),
    ('A0016C880162017C3686B18A3D4780', 31),
]

def tests():
    for sample, expected in samples:
        packet = unhexlify(sample)
        ast, _ = decode_packet(packet, 0)
        assert sum_versions(ast) == expected


def sum_versions(ast):
    if type(ast) is Literal:
        return ast.version
    elif type(ast) is Operator:
        return ast.version + sum(map(sum_versions, ast.packets))
    else:
        raise TypeError(type(ast))


SUM = 0
PRODUCT = 1
MINIMUM = 2
MAXIMUM = 3
GREATER = 5
LESS = 6
EQUAL = 7

def op(type_id):
    if type_id == SUM:
        return lambda a, b: a + b
    if type_id == PRODUCT:
        return lambda a, b: a * b
    if type_id == MINIMUM:
        return min
    if type_id == MAXIMUM:
        return max
    if type_id == GREATER:
        return lambda a, b: 1 if a > b else 0
    if type_id == LESS:
        return lambda a, b: 1 if a < b else 0
    if type_id == EQUAL:
        return lambda a, b: 1 if a == b else 0
    else:
        return TypeError(type_id)


def evaluate(ast):
    if type(ast) is Literal:
        return ast.value
    elif type(ast) is Operator:
        return reduce(op(ast.type_id), map(evaluate, ast.packets))
    else:
        raise TypeError(type(ast))


def solution():
    packet = parse_input()
    ast, _ = decode_packet(packet, 0)
    part1 = sum_versions(ast)
    print("part1", part1)

    part2 = evaluate(ast)
    print("part2", part2)


tests()
solution()
