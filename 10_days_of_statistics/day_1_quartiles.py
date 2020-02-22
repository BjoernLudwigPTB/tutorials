from statistics import median
from math import floor, ceil

format_prec_one = "{:.0f}"

N = float(input())
numbers_str = input()

numbers = [float(number_str) for number_str in numbers_str.split(sep=" ")]
numbers.sort()

q_1 = median(numbers[: floor(N / 2)])
q_2 = median(numbers)
q_3 = median(numbers[ceil(N / 2) :])

print(format_prec_one.format(q_1))
print(format_prec_one.format(q_2))
print(format_prec_one.format(q_3))
