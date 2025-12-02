"""
Basamak Toplamı, Armstrong Kontrolü ve 1-100 Asal Sayılar

- Kullanıcıdan bir tam sayı alınır.
- Girilen sayının basamaklarının toplamı hesaplanır ve gösterilir.
- Girilen sayının Armstrong sayısı (örn. 153) olup olmadığı kontrol edilir.
- Ardından 1-100 arasındaki asal sayılar ekrana yazdırılır.
"""

import math


def sum_of_digits(n: int) -> int:
    return sum(int(d) for d in str(abs(n)))


def is_armstrong(n: int) -> bool:
    if n < 0:
        return False
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n


def primes_between(a: int, b: int) -> list:
    if b < 2:
        return []
    sieve = [True] * (b + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(math.isqrt(b)) + 1):
        if sieve[i]:
            for j in range(i * i, b + 1, i):
                sieve[j] = False
    return [i for i in range(max(2, a), b + 1) if sieve[i]]


def read_int(prompt: str) -> int:
    while True:
        s = input(prompt).strip()
        try:
            return int(s)
        except ValueError:
            print('Geçersiz giriş. Lütfen bir tam sayı girin.')


def main():
    print('Basamak Toplamı ve Armstrong Kontrolü')
    n = read_int('Bir tam sayı girin: ')

    s = sum_of_digits(n)
    print(f'Girilen sayının basamakları toplamı: {s}')

    if is_armstrong(n):
        print(f'{n} bir Armstrong sayıdır.')
    else:
        print(f'{n} bir Armstrong sayı değildir.')

    print('\n1-100 arasındaki asal sayılar:')
    primes = primes_between(1, 100)
    print(', '.join(str(p) for p in primes))


if __name__ == '__main__':
    main()
