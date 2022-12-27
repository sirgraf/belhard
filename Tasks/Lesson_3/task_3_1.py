#####Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами
input_text = input('Введите строку: ')
title_len_diff = len("original string: ") - len('1nd way: ')

print(  f"original string: {input_text}" +
        f"\n1st way: " + f"{input_text.replace(' ','-')}".rjust(title_len_diff + len(input_text), ' ') +
        f"\n2nd way: {'-'.join(input_text.split(' ')).rjust(title_len_diff + len(input_text), ' ')}")