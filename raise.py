"Метод хорд"
import math
import numpy


def func_m(x): return x2 + 3 - 1/x


e = 0.001


def hord_method(a, b, e):
    fa = func_m(a)
    fb = func_m(b)
    x = a

    while True:
        xp = x
        x = a-fa(b-a)/(fb-fa)
        fx = func_m(x)

    if np.sign(fa) == np.sign(fx):
        a = x
        fa = fx
    else:
        b = x
        fb = fx
    if abs(xp - x) < e:



