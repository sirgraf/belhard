##### Написать функцию перевода десятичного числа в двоичное и обратно, без использования функции int
def bin2dec_converter(number):
    # print("Binary")
    bin_power = 0
    result_ = 0
    for i in str(number)[-1::-1]:
        if int(i) & 1:
            result_ += 2 ** bin_power
        bin_power += 1
    return f"Ваше десятичное число: {result_}"


def dec2bin_converter(number):
    # print("Decimal")
    bin_power = 0
    result_ = ''
    number_ = number
    while number_ > 0:
        if number_ & (2 ** bin_power):
            result_ = '1' + result_
        else:
            result_ = '0' + result_
        number_ = number_ - (number_ & (2 ** bin_power))
        bin_power += 1
    if len(result_) % 4 != 0:
        result_ = result_.zfill(len(result_) + (4 - (len(result_) % 4)))
    result_ = ''.join(l + ' ' * (n % 4 == 3) for n, l in enumerate(result_))
    return f"Ваше двоичное число: {result_}"


try:
    input_number = int(input("Введите десятичное или двоичное число: "))

except ValueError as e:
    print(f"Необходимо ввести число")
except Exception as e:
    print(e)
else:
    if all(c in "01" for c in str(input_number)):
        # да-да, ввод десятичных чисел только с 1 и 0 (десять напр) будет восприниматься как двоичное, я в курсе
        print(bin2dec_converter(input_number))
    else:
        print(dec2bin_converter(input_number))
