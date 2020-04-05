
import random
import math


def mean(vals):
    return sum(vals) / len(vals)


def variance(vals):
    mu = mean(vals)

    acc = 0
    for val in vals:
        acc += (val - mu)**2

    return acc / len(vals)


def standard_deviation(vals):
    return math.sqrt(variance(vals))


if __name__ == '__main__':
    vals = [random.randint(9, 12) for i in range(20)]
    mu = mean(vals)
    var = variance(vals)
    sigma = standard_deviation(vals)

    print(f'values: {vals}')
    print(f'mean: {mu}')
    print(f'variance: {var}')
    print(f'standard deviation: {sigma}')