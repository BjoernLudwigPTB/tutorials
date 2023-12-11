from math import erf, sqrt

format_prec_four = "{:.4f}"


def cdf_normal(x: float, mean: float = 0, std: float = 1):
    """Return the probability that normally distributed is smaller or equal to x"""
    return (1 / 2) * (1 + erf((x - mean) / (std * sqrt(2))))


def challenge_central_limit_theorem_1():
    max_weight = float(input())
    n_boxes = float(input())
    mean = float(input())
    std = float(input())
    sample_mean = n_boxes * mean
    sample_std = sqrt(n_boxes) * std
    print(format_prec_four.format(cdf_normal(max_weight, sample_mean, sample_std)))


if __name__ == "__main__":
    challenge_central_limit_theorem_1()
