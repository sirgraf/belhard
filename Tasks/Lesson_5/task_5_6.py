##### необходимо написать игру "угадай число" и сказать сколько попыток ушло на
#####  это у пользователя

from random import randint
max_N = int(input("Сыграем в игру \"Угадай число\". Введите максимальный диапазон чисел: "))
# max_N = 20
a = randint(1, max_N)

print(f"Угадайте число от 1 до {max_N}\n")

guess_N = int(input("Ваше число? "))
attempts = 1
while guess_N != a:
    guess_N = int(input("Попробуйте еще раз: "))
    attempts += 1

print(f"Общее количество попыток: {attempts}")
