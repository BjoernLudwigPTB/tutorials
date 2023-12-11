import numpy as np
from scipy.stats import mode

format_prec_one = "{:.1f}"
format_prec_zero = "{:.0f}"

N = input()
numbers_str = input()

numbers = np.fromstring(numbers_str, sep=" ")

print(format_prec_one.format(np.mean(numbers)))
print(format_prec_one.format(np.median(numbers)))
print(format_prec_zero.format(mode(numbers)[0][0]))
