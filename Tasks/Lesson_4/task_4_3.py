##### Заполнить словарь где ключами будут выступать числа от 0 до n, а
##### значениями вложенный словарь с ключами "name" и "email", а значения
##### для этих ключей будут браться с клавиатуры
input_N = int(input('Введите N: '))

output_dict = {i: {"email": input("email: "), "name": input("name: ")} for i in range(input_N)}
print(output_dict)