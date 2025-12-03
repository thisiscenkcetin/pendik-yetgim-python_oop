"""
Modüler Hesap Makinesi
"""
import math


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        raise ZeroDivisionError("0'a bölme hatası")
    return a / b


def power(a, b):
    return a ** b


def mod(a, b):
    if b == 0:
        raise ZeroDivisionError("0'a mod alma hatası")
    return a % b


def sqrt(a):
    if a < 0:
        raise ValueError('Negatif sayının karekökü alınamaz')
    return math.sqrt(a)


if __name__ == '__main__':
    print('Basit Hesap Makinesi (modüler)')
    try:
        a = float(input('Sayı A: '))
        b = float(input('Sayı B: '))
        op = input('İşlem (+, -, *, /, **, %, sqrtA): ').strip()
        if op == '+':
            print(add(a, b))
        elif op == '-':
            print(sub(a, b))
        elif op == '*':
            print(mul(a, b))
        elif op == '/':
            print(div(a, b))
        elif op == '**':
            print(power(a, b))
        elif op == '%':
            print(mod(a, b))
        elif op == 'sqrtA':
            print(sqrt(a))
        else:
            print('Bilinmeyen işlem')
    except Exception as e:
        print('Hata:', e)
