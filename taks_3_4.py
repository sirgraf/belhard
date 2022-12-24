####Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных
input_var_1 = int(input("Введите 1-е число: "))
input_var_2 = int(input("Введите 2-е число: "))
input_var_3 = int(input("Введите 3-е число: "))

output_var = str(int(input_var_1 > 0)) + str(int(input_var_2 > 0)) + str(int(input_var_3 > 0))
print(  f"Количество положительных чисел:  {output_var.count('1')}" +
         f"\nКоличество отрицательных чисел: {output_var.count('0')}")