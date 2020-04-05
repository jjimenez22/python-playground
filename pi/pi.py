
import random
import math
import sys

sys.path.insert(1, '..')
from statistics import standard_deviation, mean


# Estimate pi number by random points in a circle
def setup_points(num):
    in_circle = 0
    for _ in range(num):
        x = random.random() * random.choice([-1, 1])
        y = random.random() * random.choice([-1, 1])
        circle_radius = math.sqrt(x**2 + y**2)

        if circle_radius <= 1:
            in_circle += 1

    return (4 * in_circle) / num


def estimation(num, attempts):
    estimates = []
    for _ in range(attempts):
        pi_estimation = setup_points(num)
        estimates.append(pi_estimation)

    estimates_mean = mean(estimates)
    sigma = standard_deviation(estimates)

    print(f'mean={round(estimates_mean, 5)}, sigma={round(sigma, 5)}, points={num}')
    return estimates_mean, sigma


def estimate_pi(precision, attempts):
    points_num = 1000
    sigma = precision

    while sigma >= precision / 1.96:
        mean, sigma = estimation(points_num, attempts)
        points_num *= 2

    return mean


if __name__ == '__main__':
    estimate_pi(0.01, 1000)