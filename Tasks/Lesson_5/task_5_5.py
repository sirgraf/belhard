##### Подсчитать среднее арифметическое N чисел, вводимых с клавиатуры

input_N = input("Какое количество чисел необходимо ввести: ")
average_number = 0

if input_N.isdigit():
    for _ in range(int(input_N)):
        average_number += int(input("Введите число: "))
    average_number = average_number / int(input_N)

    print(f"Среднее арифметическое: {average_number}")
