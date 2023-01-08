# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)

users_dict = {
    '223rffX21': {
        "name": "Alex",
        "surname": "Petrov",
        "tel": "02911111199",
        "email": "alexmail@gmail.com"
    },
    'g432g2X21': {
        "name": "John",
        "surname": "Kirby",
        "tel": "02911411199",
        "email": "kirbymail@gmail.com"
    },
    'pppowe233': {
        "name": "Jenny",
        "surname": "Johns",
        "tel": "02911111879",
        "email": ""
    }
}

def dict_something(some_dict):
    for user_ in some_dict:
        if some_dict[user_]['email'] == '':
            print(f"No email for: {some_dict[user_]['name'] + ' ' + some_dict[user_]['surname']}")

dict_something(users_dict)