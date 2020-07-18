from math import exp, factorial

format_prec_three = "{:.3f}"


def poisson_dist(k: int = 1, lmbd: float = 1.):
    return (lmbd ** k * exp(- lmbd)) / factorial(k)


def challenge_poisson_distribution_1():
    lmbd = float(input())
    k = int(input())

    print(format_prec_three.format(poisson_dist(k, lmbd)))


def challenge_poisson_distribution_2():
    lmbd_a, lmbd_b = input().split()

    print(format_prec_three.format(160 + 40 * (float(lmbd_a) + float(lmbd_a)**2)))
    print(format_prec_three.format(128 + 40 * (float(lmbd_b) + float(lmbd_b)**2)))
