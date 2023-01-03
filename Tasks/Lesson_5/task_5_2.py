##### Сделать калькулятор: у пользователя спрашивается число, потом действие и второе число

print("Введите по порядку первое число, операнд и второе число:")
calc_list = []
output_str = "Результат: "

for i in range(3):
    calc_list.append(input(": ").strip())

if calc_list[0].replace('.', '').replace(',', '').isdigit() \
            and calc_list[2].replace('.', '').replace(',', '').isdigit():
    if calc_list[1] == '+':
        output_str += str(float(calc_list[0]) + float(calc_list[2]))
    elif calc_list[1] == '-':
        output_str += str(float(calc_list[0]) - float(calc_list[2]))
    elif calc_list[1] == '*':
        output_str += str(float(calc_list[0]) * float(calc_list[2]))
    elif calc_list[1] == '/' or calc_list[1] == ':':
        output_str += str(float(calc_list[0]) - float(calc_list[2]))
    elif calc_list[1] == '**':
        output_str += str(float(calc_list[0]) ** float(calc_list[2]))
    elif calc_list[1] == '//':
        output_str += str(float(calc_list[0]) // float(calc_list[2]))
    elif calc_list[1] == '%':
        output_str += str(float(calc_list[0]) % float(calc_list[2]))
    else:
        output_str += 'Ошибка! Неверный арифметический оператор'
else:
    output_str += 'Ошибка! Неверно введено число'

print(output_str)
