from test_framework import generic_test
import math

def is_palindrome_number(x: int) -> bool:
    if x <= 0:
        return x == 0
    num_digs = math.floor(math.log10(x))+1
    mask = 10**(num_digs-1)
    for i in range(num_digs // 2):
        if x // mask != x % 10:
            return False
        x %= mask # remove most sig fig
        x //= 10 # remove least sig fig
        mask //= 100
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
