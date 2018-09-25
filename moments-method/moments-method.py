from math import factorial as fac

import matplotlib.pyplot as plt
import numpy as np


def average_experiment(k, l):
    k_sum = sum([X ** k for X in l])
    return k_sum / len(l)


def uniform_moment(k, l):
    return (average_experiment(k, l) * (k + 1) / k) ** (1 / k)


def gen_uniform():
    return [np.random.uniform(0.0, theta) for _ in range(1, num_of_experiments)]


def moments_method_uniform(k):
    return [uniform_moment(k, gen_uniform()) for _ in range(1, repeat)]


def exp_moment(k, l):
    return (fac(k) / average_experiment(k, l)) ** (1 / k)


def gen_exp():
    return [np.random.exponential(theta) for _ in range(1, num_of_experiments)]


def moments_method_exp(k):
    return [exp_moment(k, gen_exp()) for _ in range(1, repeat)]


def standard_deviation(l):
    return (sum([(t - theta) ** 2 for t in l]) / len(l)) ** 0.5


if __name__ == '__main__':
    max_k = 100
    x = range(1, max_k)
    num_of_experiments = 1000
    repeat = 10
    theta = 1.5

    y_uni = [standard_deviation(moments_method_uniform(k)) for k in x]
    y_exp = [standard_deviation(moments_method_exp(k)) for k in x]

    # graph for uniform distribution
    plt.figure()
    plt.plot(x, y_uni, 'r')
    plt.yticks([0.1 * t for t in range(0, 100)])
    plt.ylim(0, 1.5)
    plt.xlim(1, max_k)
    plt.xticks([5 * t for t in range(0, max_k // 5)])
    plt.xlabel('k')
    plt.ylabel('standard deviation')
    plt.title('Uniform')

    # graph for exponential distribution
    plt.figure()
    plt.plot(x, y_exp, 'b')
    plt.ylim(0, 6)
    plt.xlim(1, max_k)
    plt.xticks([5 * t for t in range(1, max_k // 5)])
    plt.title('Exponential')
    plt.xlabel('k')
    plt.ylabel('standard deviation')
    plt.show()
