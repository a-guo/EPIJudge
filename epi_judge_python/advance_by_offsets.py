from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    furthest, last = 0, len(A) - 1
    i = 0
    while i <= furthest and furthest < last:
        furthest = max(furthest, A[i] + i)
        i += 1
    return furthest >= last


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
