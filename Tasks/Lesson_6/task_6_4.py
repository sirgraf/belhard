# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно
objects_lst = [1, 3, True, "string", 1.3, False, (3, 4), "string2", ["stringinlist"], 3]

def lst_filter(target_list):
    return list(filter(lambda x: isinstance(x, str), target_list))

print(f"Sorted list: {lst_filter(objects_lst)}")