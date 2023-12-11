from functools import reduce
from math import prod, sqrt
from statistics import mean


def standard_deviation(n_samples: int, var: tuple[float, ...]) -> float:
    """Compute the standard deviation of the random sample"""
    numerator = reduce(lambda x, y: x + y, [(x - mean(var)) ** 2 for x in var])

    return sqrt(numerator / float(n_samples))


def covariance(
    n_samples: int, var_x: tuple[float, ...], var_y: tuple[float, ...]
) -> float:
    """Compute the covariance of the two samples"""
    assert len(var_x) == len(var_y) == n_samples

    def compute_differences(
        _n_samples: int, var: tuple[float, ...]
    ) -> tuple[float, ...]:
        """Compute the differences between the samples and their mean"""
        return tuple(var_i - mean(var) for var_i in var)

    cov_temp = 0
    for vars in zip(
        compute_differences(n_samples, var_x),
        compute_differences(n_samples, var_y),
    ):
        cov_temp += prod(vars)
    cov_temp /= n_samples
    return cov_temp


def pearson_coefficient(
    n_samples: int, var_x: tuple[float, ...], var_y: tuple[float, ...]
) -> float:
    """Compute the pearson correlation coefficient of the two random samples"""
    assert len(var_x) == len(var_y) == n_samples
    std_x = standard_deviation(n_samples, var_x)
    std_y = standard_deviation(n_samples, var_y)
    return covariance(n_samples, var_x, var_y) / (std_x * std_y)


def read_random_var() -> tuple[float, ...]:
    """Read random variable from standard input"""
    return tuple(
        float(real_number) for real_number in input().split(" ") if real_number != "\r"
    )


def challenge_pearson_1():
    n_values: int = int(input())
    var_x: tuple[float, ...] = read_random_var()
    var_y: tuple[float, ...] = read_random_var()
    print(f"{pearson_coefficient(n_values, var_x, var_y):.3f}")


if __name__ == "__main__":
    challenge_pearson_1()
