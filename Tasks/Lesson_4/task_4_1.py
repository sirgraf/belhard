##### Заполнить список степенями числа 2 (от 2^1 до 2^n)

input_n_power = int(input('Введите степень n: '))

list_numbers = []

list_numbers = [2**i for i in range(1, input_n_power + 1)]

print(list_numbers)