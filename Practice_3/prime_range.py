"""
Prime Number Range
- Kullanıcıdan iki sayı alır ve bu aralıktaki asal sayıları listeler.
"""

import math


def read_int(prompt):
    while True:
        s = input(prompt).strip()
        try:
            return int(s)
        except ValueError:
            print('Geçersiz giriş. Bir tam sayı girin.')


def primes_between(a: int, b: int):
    if b < 2:
        return []
    low = max(2, min(a,b))
    high = max(a,b)
    sieve = [True] * (high + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(math.isqrt(high)) + 1):
        if sieve[i]:
            for j in range(i*i, high+1, i):
                sieve[j] = False
    return [i for i in range(low, high+1) if sieve[i]]


def main():
    print('Asal Sayı Aralığı Bulucu')
    a = read_int('Başlangıç (tam sayı): ')
    b = read_int('Bitiş (tam sayı): ')
    primes = primes_between(a, b)
    if primes:
        print(f'{a} ve {b} arası asal sayılar:')
        print(', '.join(str(p) for p in primes))
    else:
        print('Bu aralıkta asal sayı bulunamadı.')


if __name__ == '__main__':
    main()
