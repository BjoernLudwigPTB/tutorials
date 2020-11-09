from math import sqrt


def challenge_central_limit_theorem_3():
    n_sample = float(input())
    mean = float(input())
    std = float(input())
    _ = float(input())
    z_score = float(input())
    sample_std = std / sqrt(n_sample)
    diff = z_score * sample_std
    a_low, b_high = mean - diff, mean + diff
    print(round(a_low, 2))
    print(round(b_high, 2))


if __name__ == "__main__":
    challenge_central_limit_theorem_3()
