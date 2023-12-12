from math import factorial
from re import split

format_prec_three = "{:.3f}"


def challenge_4():
    inputs = split(" ", input())
    prob_boys, prob_girls = float(inputs[0]), float(inputs[1])
    p = prob_boys / (prob_boys + prob_girls)

    sum = 0

    for k in range(3, 7):
        binom = factorial(6) / (factorial(k) * factorial(6 - k))
        sum += binom * p**k * (1 - p) ** (6 - k)

    return format_prec_three.format(sum)


def challenge_5():
    inputs = split(" ", input())
    error_prob, n_pistons = int(inputs[0]) / 100, int(inputs[1])

    sum = 0

    for k in range(1, 3):
        binom = factorial(n_pistons) / (factorial(k) * factorial(n_pistons - k))
        sum += binom * error_prob**k * (1 - error_prob) ** (n_pistons - k)

    return format_prec_three.format(sum)


def challenge_6():
    inputs = input().split()
    error_prob, n_pistons = int(inputs[0]) / 100, int(inputs[1])

    sum = 0

    for k in range(1, 3):
        binom = factorial(n_pistons) / (factorial(k) * factorial(n_pistons - k))
        sum += binom * error_prob**k * (1 - error_prob) ** (n_pistons - k)

    return format_prec_three.format(sum)
