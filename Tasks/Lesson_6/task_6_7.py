# Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной
# стороны списка

numbers_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# def neighbours_sum(n_lst):
#     gen_dict = dict(enumerate(n_lst))
#     gen_dict[-1] = gen_dict.pop(len(gen_dict) - 1)
#     sum_lst = []
#     print(numbers_lst)
#     def sum_generator():
#         for i in gen_dict:
#             yield gen_dict[i + len(gen_dict) - 1 if i == -1 else i - 1] \
#                 + gen_dict[i - len(gen_dict) + 1 if i == len(gen_dict) - 2 else i + 1]
#
#     get_item = sum_generator()
#     for _ in n_lst:
#         sum_lst.append(get_item.__next__())
#     print(sum_lst)

def neighbours_sum(n_lst):
    sum_lst = []
    print(numbers_lst)
    for i in range(len(n_lst)):
        sum_lst.append(n_lst[i - 1] + n_lst[i - len(n_lst) + 1])
    print(sum_lst)

neighbours_sum(numbers_lst)
