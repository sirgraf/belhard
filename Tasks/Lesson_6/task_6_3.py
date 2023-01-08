# Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]
import collections
from collections import deque

list_N = collections.deque([0,1,2,3,4,5,6,7,8,9])
input_shift = int(input("N: "))

def list_shifter(list_N, shift):
    if shift == 0:
        return list_N
    else:
        list_N.rotate(1)
        return list_shifter(list_N, shift - 1)

print(list(list_shifter(list_N, input_shift)))
