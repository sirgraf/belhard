# Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза

from collections import OrderedDict

numbers_lst = [3, 1, 4, 6, 77, 9, 8, 7, 0]

def reverted_list(target_list):
    print(f"Original list: {numbers_lst}")
    list_halflen = len(target_list) // 2
    left_n = None
    right_n = None
    left_i = 0
    right_i = -1
    while list_halflen > 0:
        left_n = target_list[left_i]
        right_n = target_list[right_i]
        target_list[left_i] = right_n
        target_list[right_i] = left_n
        left_i += 1
        right_i += -1
        list_halflen -= 1
    print(f"Reversed list: {numbers_lst}")
    # print(f"Reversed list: {list(OrderedDict(sorted(dict(enumerate(target_list)).items(), reverse=True)).values())}")

reverted_list(numbers_lst)
