##### Вывести первые N цисел кратные M и больше K

input_N = int(input("N: "))
input_M = int(input("M: "))
input_K = int(input("K: "))

result = input_K + 1

for i in range(input_N):
    while result % input_M != 0:
        result += 1
    print(f"index[{i+1}] - {result}")
    result += 1
