"""
Matematiksel Fonksiyonlar
- Trigonometrik fonksiyonlar, logaritma, temel istatistik 
"""
import math
import statistics


def sin(x):
    return math.sin(x)


def cos(x):
    return math.cos(x)


def tan(x):
    return math.tan(x)


def log(x, base=math.e):
    return math.log(x, base)


def mean(data):
    return statistics.mean(data)


def median(data):
    return statistics.median(data)


def stdev(data):
    return statistics.stdev(data) if len(data) > 1 else 0.0


if __name__ == '__main__':
    print('math_utils örnek: sin(0)=', sin(0))
