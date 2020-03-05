from itertools import chain
from math import floor, ceil
from statistics import median

format_prec_one = "{:.1f}"

N = int(input())
numbers_str = input()
freqs_str = input()

numbers = [int(number_str) for number_str in numbers_str.split(sep=" ")]
freqs = [int(freq_str) for freq_str in freqs_str.split(sep=" ")]

s = list(chain.from_iterable([[num] * freq for num, freq in zip(numbers, freqs)]))
s.sort()

q_1 = median(s[: floor(len(s) / 2)])
q_3 = median(s[ceil(len(s) / 2) :])

print(format_prec_one.format(q_3 - q_1))
