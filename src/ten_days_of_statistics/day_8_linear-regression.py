from functools import reduce
from math import prod, sqrt
from statistics import mean
from typing import Iterable


def standard_deviation(n_samples: int, var: Iterable) -> float:
    """Compute the standard deviation of the random sample"""
    numerator = reduce(lambda x, y: x + y, [(x - mean(var)) ** 2 for x in var])

    return sqrt(numerator / float(n_samples))


def covariance(n_samples: int, var_x: Iterable, var_y: Iterable) -> float:
    """Compute the covariance of the two samples"""
    assert len(var_x) == len(var_y) == n_samples

    def compute_differences(_n_samples: int, var: Iterable) -> Iterable:
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


def pearson_coefficient(n_samples: int, var_x: Iterable, var_y: Iterable) -> float:
    """Compute the pearson correlation coefficient of the two random samples"""
    assert len(var_x) == len(var_y) == n_samples
    std_x = standard_deviation(n_samples, var_x)
    std_y = standard_deviation(n_samples, var_y)
    return covariance(n_samples, var_x, var_y) / (std_x * std_y)


def read_students_results() -> tuple[list[int], list[int]]:
    """Read students results from standard input"""
    var_x, var_y = tuple([int(var_i)] for var_i in input().split(" "))
    for _ in range(4):
        var_x_i, var_y_i = input().split(" ")
        var_x.append(int(var_x_i))
        var_y.append(int(var_y_i))
    return var_x, var_y


def compute_b(var_x: list[int], var_y: list[int]) -> float:
    """Compute the factor of the regression line"""
    assert len(var_x) == len(var_y)
    n_samples = len(var_x)
    return pearson_coefficient(n_samples, var_x, var_y) * (
        standard_deviation(n_samples, var_y) / standard_deviation(n_samples, var_x)
    )


def compute_a(var_x: list[int], var_y: list[int], factor: float) -> float:
    """Compute the translation of the regression line"""
    assert len(var_x) == len(var_y)
    return mean(var_y) - factor * mean(var_x)


def challenge_linear_regression() -> None:
    aptitude_scores, statistics_grades = read_students_results()
    factor = compute_b(aptitude_scores, statistics_grades)
    translation = compute_a(aptitude_scores, statistics_grades, factor)
    print(f"{translation + factor * 80:.3f}")


if __name__ == "__main__":
    challenge_linear_regression()
