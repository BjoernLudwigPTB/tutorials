from math import pi, sqrt, erf

format_prec_three = "{:.3f}"


def cdf_normal(x: float, mean: float = 0, std: float = 1):
    return (1 / 2) * (1 + erf((x - mean) / (std * sqrt(2))))


def challenge_normal_distribution_1():
    mean, std = map(float, input().split())
    first_input = float(input())
    lower_bound, upper_bound = map(float, input().split())

    print(format_prec_three.format(cdf_normal(x=first_input, mean=mean, std=std)))
    print(
        format_prec_three.format(
            cdf_normal(x=upper_bound, mean=mean, std=std)
            - cdf_normal(x=lower_bound, mean=mean, std=std)
        )
    )


if __name__ == "__main__":
    challenge_normal_distribution_1()
