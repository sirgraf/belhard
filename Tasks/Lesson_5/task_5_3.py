##### Вывести четные числа от 2 до N по 5 в строку

input_N = int(input('Введите N: '))
output_str = str()

for i, j in zip(range(2, input_N + 1, 2), range(1, input_N // 2 + 1)):
    if j % 5 != 0:
        output_str += f"{i} "
    elif j % 5 == 0:
        output_str += f"{i}\n"

print(output_str)

