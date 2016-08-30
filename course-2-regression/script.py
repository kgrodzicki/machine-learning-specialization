from math import exp

__author__ = 'grokrz'


def log(x, i):
    if i == 1:
        return 1.0 / (1.0 + exp(-x))
    else:
        return 1.0 / (1.0 + exp(x))


def delta(x, i):
    if i == 1:
        return 1.0 - log(x, i)
    else:
        return -log(x, i)


data = [(2.5, 1), (0.3, -1), (2.8, 1), (0.5, 1)]
prob = 1.0
der = 0.0

for (x, y) in data:
    prob *= log(x, y)
    der += x * delta(x, y)

print prob, der
