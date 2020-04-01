from test_framework import generic_test


def divide(x: int, y: int) -> int:
    result, power = 0, 32
    ypow = y << power
    while x >= y:
        while ypow > x:
            ypow >>= 1
            power -= 1
        result += 1 << power
        x -= ypow
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_divide.py',
                                       'primitive_divide.tsv', divide))
