import numpy as np

# Метод обратных функций
# Пусть a = |a|
# 2ac + 2c e^{-a} = 1
# c = 1 / (2a + 2 e^{-a})
# F(t) = c e^{t}, t < -a
# F(t) = c e^{-a} + c (t + a), t \in [-a; a]
# F(t) = 2 c e^{-a} + 2 c a - c e ^{-t}, t > a
# x_* = -\inf
# x^8 = \inf
# G(y) = \ln (y / c), y < c e^{-a}
# G(y) = (y - c e^{-a} - ca) / c, c e^{-a} <= y <=  c e^{-a} + 2ca
# G(y) = -\ln((y - 2c e^{-a} - 2ca) / c) , otherwise


def C(a):
    return 1 / (2 * a + 2 * np.exp(-a))


def G(y, a):
    a = abs(a)
    c = C(a)
    if y < c * np.exp(-a):
        return np.log(y / c)
    if y > c * np.exp(-a) + 2 * c * a:
        return -np.log(y / c - 2 * np.exp(-a) -a)
    return y / c - np.exp(-a) - a


def get_exp(a):
    x = np.random.exponential(a)
    while x < a:
        x = np.random.exponential(a)
    return x


# Метод дискретной декомпозиции
# F1(x) = a_1 c e^{t}, t < -a, p1 = 1 / a1 =  (c e^{-a})
# F2(t) = a_2 (c e^{-a} + c (t + a)), t \in [-a; a], p2 = 1 /  a2 = (2ca)
# F3(t) = a_3 (2 c e^{-a} + 2 c a - c e ^{-t}), t > a, p3 = 1 - p2 - p3


def discreate_decomposition(a):
    c = C(a)
    p1 = c * np.exp(-a)
    print(p1)
    p2 = 2 * c * a
    p3 = 1 - p1 - p2
    p = np.array([p1, p2, p3])
    p_res = np.random.choice([1, 2, 3], 1, p=p)[0]
    return  {
        1 : -get_exp(a),
        2 : np.random.uniform(-a, a),
        3 : get_exp(a)
    }[p_res]


