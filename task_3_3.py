#####Пользователь вводит Имя, Возраст и Город, сформировать приветственное сообщение путем форматирования 3-мя способами
name_var = input("Имя: ")
age_var = int(input("Возраст: "))
city_var = input("Город: ")

print("1st way: Привет, меня зовут %s. Мне %d лет. Я из города %s" % (name_var, age_var, city_var))

print("2nd way: Привет, меня зовут {}. Мне {} лет. Я из города {}".format(name_var, age_var, city_var))

print(f"3rd way: Привет, меня зовут {name_var}. Мне {age_var} лет. Я из города {city_var}")