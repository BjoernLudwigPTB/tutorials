from math import erf, sqrt

format_prec_four = "{:.4f}"


def cdf_normal(x: float, mean: float = 0, std: float = 1):
    """Return the probability that normally distributed is smaller or equal to x"""
    return (1 / 2) * (1 + erf((x - mean) / (std * sqrt(2))))


def challenge_central_limit_theorem_2():
    tickets_available = float(input())
    n_students = float(input())
    mean = float(input())
    std = float(input())
    sample_mean = n_students * mean
    sample_std = sqrt(n_students) * std
    print(
        format_prec_four.format(cdf_normal(tickets_available, sample_mean, sample_std))
    )


if __name__ == "__main__":
    challenge_central_limit_theorem_2()
