def Add(a, b):
    MAX_BIT = 2 ** 32
    MAX_BIT_COMPLIMENT = -2 ** 32

    while b != 0:
        if b == MAX_BIT:
            return a ^ MAX_BIT_COMPLIMENT
        carry = a & b
        a = a ^ b
        b = carry << 1

    return a

print(Add(-1,1))
