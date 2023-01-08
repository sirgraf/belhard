# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом нечётные

numbers_lst = [23, 1, 2, 5, 6, 1, 4353, 4, 5, 6, 0]

numbers_lst.sort(key=lambda x: (x % 2 == 0, x % 2 != 0), reverse=True)
print(numbers_lst)
