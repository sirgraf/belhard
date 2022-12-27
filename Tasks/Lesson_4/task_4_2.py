##### Без использования collections, написать программу, которая будет
#####  создавать словарь для подсчитывания количества вхождений каждой
#####  буквы в текст введенный с клавиатуры

input_text = input('Введите текст: ')
text_to_list = list(input_text)

output_dict = {text_to_list[i]: text_to_list.count(text_to_list[i]) for i in range(0, len(text_to_list))}

print(f"Сгенерированный словарь: {output_dict}")
