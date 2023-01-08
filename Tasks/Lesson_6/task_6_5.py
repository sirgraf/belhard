# Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза

from collections import OrderedDict

numbers_lst = [3, 1, 4, 6, 77, 7, 6, 3, 0]

def reverted_list(target_list):
    print(f"Original list: {numbers_lst}")
    print(f"Reversed list: {list(OrderedDict(sorted(dict(enumerate(target_list)).items(), reverse=True)).values())}")


reverted_list(numbers_lst)
