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


# Метод дискретной декомпозиции
# F(x) = c e^{t}, t < -a
#

