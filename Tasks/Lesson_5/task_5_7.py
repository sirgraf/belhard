##### Ведьмаку заплатите чеканной монетой
# Всем известно, что ведьмак способен одолеть любых чудовищ, однако его
# услуги обойдутся недешево,
# к тому же ведьмак не принимает купюры, он принимает только чеканные
# монеты.
# В мире ведьмака существуют монеты с номиналами 1, 5, 10, 25.
# Напишите программу, которая определяет какое минимальное количество
# чеканных монет нужно заплатить ведьмаку.
# Пример:
# На вход подается число 49.Ответом будет 7 (25 + 10 + 10 + 1 + 1 + 1 + 1) те
# минимальное количество монет)
#####

coins_t = (1, 5, 10, 25)
coins_t = sorted(coins_t, reverse=True)

input_N = int(input("Введите плату Ведьмака: "))

cumm_amount = 0
distinct_coins = 0
distinct_coins_list = list()

while cumm_amount < input_N:
    for i in range(len(coins_t)):
        if input_N - cumm_amount >= coins_t[i]:
            cumm_amount += coins_t[i]
            distinct_coins += 1
            distinct_coins_list.append(coins_t[i])
            break

print(f"Количество монет: {distinct_coins}")
print(f"Перечень номиналов монет: {distinct_coins_list}")
