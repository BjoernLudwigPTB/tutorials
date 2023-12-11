from functools import reduce

format_prec_one = "{:.1f}"

N = input()
numbers_str = input()
weights_str = input()

numbers = [float(number_str) for number_str in numbers_str.split(sep=" ")]
weights = [float(weight_str) for weight_str in weights_str.split(sep=" ")]

weighted_sum = reduce(lambda x, y: x + y, [a * b for a, b in zip(numbers, weights)])
sum_of_weights = reduce(lambda x, y: x + y, weights)

print(format_prec_one.format(weighted_sum / sum_of_weights))
