import statistics
from functools import reduce
from math import sqrt

format_prec_one = "{:.1f}"

N = input()
numbers_str = input()

numbers = [float(number_str) for number_str in numbers_str.split(sep=" ")]

numerator = reduce(
    lambda x, y: x + y, [(x - statistics.mean(numbers)) ** 2 for x in numbers]
)

print(format_prec_one.format(sqrt(numerator / float(N))))
