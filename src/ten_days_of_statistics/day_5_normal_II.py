from math import erf, sqrt

format_prec = "{:.2f}"


def cdf_normal(x: float, mean: float = 0, std: float = 1):
    return (1 / 2) * (1 + erf((x - mean) / (std * sqrt(2))))


def challenge_normal_distribution_2():
    mean, std = map(float, input().split())
    first_input = float(input())
    threshold = float(input())

    print(
        format_prec.format(
            (1 - cdf_normal(x=first_input, mean=mean, std=std)) * 100
        )
    )
    print(
        format_prec.format(
            (1 - cdf_normal(x=threshold, mean=mean, std=std)) * 100
        )
    )
    print(format_prec.format(cdf_normal(x=threshold, mean=mean, std=std) * 100))


if __name__ == "__main__":
    challenge_normal_distribution_2()
