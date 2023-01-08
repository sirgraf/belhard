# inp_number = input("N: ")
#
# result = 0
#
# for i in range(len(inp_number)):
#     result += int(inp_number[i])
#
# print(result)

# list_numbers = [1,2,3,4,5,6,7,82,3,2,2,3,2,34,4,2,32]
#
# for i in range(list_numbers.count(2)):
#     list_numbers.remove(2)
#
# print(list_numbers)

# try:
#     a = int(input())
#     b = int(input())
#     c = a / b
# except ValueError:

# i = -1
# number = int(input("N: "))
# while 2**(i + 1) <= number:
#     i += 1
# print(i)

# amount = float(input("Amount: "))
# interest_rate = float(input("IR: "))

#
# str = '123'
# custom_iter = iter(str)
# print(type(custom_iter))

# def foo(str_):
#     return list(filter(lambda x: len(x) >= 5, str_.split()))
#
# print(foo(input("Введите строку: ")))

from random import choice

passwords = {}
print(choice('abcd'))
def generate_password(res_name, pass_len):
    for i in range(pass_len):
        choice()