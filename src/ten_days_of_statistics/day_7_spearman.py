def spearman_coefficient_without_duplicates(
    n_samples: int, var_x: tuple[float, ...], var_y: tuple[float, ...]
) -> float:
    """Compute the spearman rank correlation coefficient of the two random samples"""
    assert len(var_x) == len(var_y) == n_samples
    differences = tuple(
        (x_i - y_i) ** 2 for (x_i, y_i) in zip(rank_order(var_x), rank_order(var_y))
    )
    return 1 - 6 * sum(differences) / (n_samples * (n_samples**2 - 1))


def rank_order(var_x: tuple[float, ...]) -> tuple[int, ...]:
    """Compute the rank order of the random sample"""
    return tuple(len(var_x) - (sorted(var_x).index(x)) for x in var_x)


def read_random_var_from_stdin() -> tuple[float, ...]:
    """Read random variable from standard input"""
    return tuple(
        float(real_number) for real_number in input().split(" ") if real_number != "\r"
    )


def challenge_pearson_1():
    n_values: int = int(input())
    var_x: tuple[float, ...] = read_random_var_from_stdin()
    var_y: tuple[float, ...] = read_random_var_from_stdin()
    print(f"{spearman_coefficient_without_duplicates(n_values, var_x, var_y):.3f}")


if __name__ == "__main__":
    challenge_pearson_1()
