from test_framework import generic_test


def reverse(x: int) -> int:
    result, x_rem = 0, abs(x)
    while x_rem:
        result = result * 10 + x_rem % 10
        x_rem //= 10
    return -result if x < 0 else result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
