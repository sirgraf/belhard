##### Вводится число, найти его максимальную цифру

input_N = int(input("N: "))

max_digit = str(input_N)[0]

for i in str(input_N)[1:]:
    if i > max_digit:
        max_digit = i

print(max(list(str(input_N))))
print(max_digit)
