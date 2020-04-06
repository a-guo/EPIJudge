import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    write_ind, a_count = 0, 0
    for i in range(size):
        if s[i] != 'b':
            s[write_ind] = s[i]
            write_ind += 1
        if s[i] == 'a':
            a_count += 1
    cur_ind = write_ind - 1
    write_ind += a_count - 1
    final_size = write_ind + 1
    while cur_ind >= 0:
        if s[cur_ind] == 'a':
            s[write_ind-1:write_ind+1] = 'dd'
            write_ind -= 2
        else:
            s[write_ind] = s[cur_ind]
            write_ind -= 1
        cur_ind -= 1
    return final_size


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
