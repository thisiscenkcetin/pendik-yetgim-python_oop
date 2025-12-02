"""
Mükemmel Sayı Kontrolü
- Pozitif tam bölenlerinin (kendisi hariç) toplamı sayıya eşit ise "mükemmel" sayıdır.
Örnek: 6 => bölenler 1,2,3 => 1+2+3 = 6
"""

import math


def proper_divisors(n: int) -> list:
    """n'in kendisi hariç pozitif tam bölenlerinin listesini döndürür."""
    if n <= 1:
        return []
    divs = {1}
    limit = int(math.isqrt(n))
    for i in range(2, limit + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
    return sorted(divs)


def is_perfect(n: int) -> bool:
    return sum(proper_divisors(n)) == n


def read_positive_int(prompt: str) -> int:
    while True:
        s = input(prompt).strip()
        if not s:
            print('Giriş boş. Lütfen pozitif bir tam sayı girin.')
            continue
        if not (s.isdigit() or (s.startswith('-') and s[1:].isdigit())):
            print('Geçersiz giriş. Pozitif bir tam sayı girin.')
            continue
        v = int(s)
        if v <= 0:
            print('Pozitif bir sayı girin (1 veya daha büyük).')
            continue
        return v


def main():
    print('Mükemmel Sayı Kontrolü')
    n = read_positive_int('Pozitif bir tam sayı girin: ')
    divs = proper_divisors(n)
    s = sum(divs)
    print(f'{n} sayısının kendisi hariç bölenleri: {divs}')
    print(f'Bölenlerin toplamı: {s}')
    if s == n:
        print(f'{n} bir mükemmel sayıdır.')
    else:
        print(f'{n} bir mükemmel sayı değildir.')


if __name__ == '__main__':
    main()
