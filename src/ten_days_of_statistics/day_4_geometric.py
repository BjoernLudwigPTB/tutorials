format_prec_three = "{:.3f}"


def challenge_geometric_distribution_2():
    prob_numerator, prob_denominator = input().split()
    latest_success = int(input())
    p = float(prob_numerator) / float(prob_denominator)

    result = 0

    for k in range(latest_success):
        result += p * (1 - p) ** k

    print(format_prec_three.format(result))
