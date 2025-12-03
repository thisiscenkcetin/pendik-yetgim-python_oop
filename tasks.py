"""
Practice_4 - Dört küçük araç

1) Girilen sayının asal olup olmadığını kontrol et
2) Girilen kelimenin palindrome (tersi kendisi) olup olmadığını kontrol et
3) Girilen kelimedeki tekrar eden karakterleri bul
4) Girilen sayıya kadar (<= N) Fibonacci serisini bastır

Menüyle etkileşimli olarak çalışır.
"""

from collections import Counter
import math


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def is_palindrome(s: str) -> bool:
    # Küçük/büyük harf farkını yok say ve alfabenümerik karakterleri kullan
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


def repeating_characters(s: str):
    c = Counter(s)
    return {ch: cnt for ch, cnt in c.items() if cnt > 1}


def fibonacci_upto(n: int):
    # n'e kadar olan (<= n) Fibonacci sayılarını döndür
    if n < 0:
        return []
    seq = []
    a, b = 0, 1
    while a <= n:
        seq.append(a)
        a, b = b, a + b
    return seq


def read_int(prompt: str, allow_negative=False) -> int:
    while True:
        s = input(prompt).strip()
        try:
            v = int(s)
            if not allow_negative and v < 0:
                print('Negatif değer girilemez.')
                continue
            return v
        except ValueError:
            print('Geçersiz giriş. Lütfen bir tam sayı girin.')


def read_nonempty(prompt: str) -> str:
    while True:
        s = input(prompt).strip()
        if s == '':
            print('Boş giriş kabul edilmez.')
            continue
        return s


def main():
    while True:
        print('\n-- Practice_4 Araçları --')
        print('1) Sayının asal olup olmadığını kontrol et')
        print('2) Kelimenin palindrome (tersi aynı) olup olmadığını kontrol et')
        print('3) Kelimedeki tekrar eden karakterleri bul')
        print('4) Girilen sayıya kadar Fibonacci serisini bastır')
        print('5) Çıkış')

        choice = read_int('Seçiminiz (1-5): ', allow_negative=False)
        if choice == 1:
            n = read_int('Pozitif bir tam sayı girin: ')
            if is_prime(n):
                print(f'{n} bir asal sayıdır.')
            else:
                print(f'{n} asal sayı değildir.')

        elif choice == 2:
            s = read_nonempty('Bir kelime veya cümle girin: ')
            if is_palindrome(s):
                print('Girilen ifade palindrome (tersi aynı).')
            else:
                print('Girilen ifade palindrome değildir.')

        elif choice == 3:
            s = read_nonempty('Bir kelime girin: ')
            repeats = repeating_characters(s)
            if repeats:
                print('Tekrar eden karakterler ve sayıları:')
                for ch, cnt in repeats.items():
                    print(f"'{ch}': {cnt}")
            else:
                print('Tekrar eden karakter yok.')

        elif choice == 4:
            n = read_int('Pozitif bir tam sayı girin (limit N): ')
            seq = fibonacci_upto(n)
            print(f'Fibonacci (<= {n}):')
            print(', '.join(str(x) for x in seq))

        elif choice == 5:
            print('Çıkılıyor.')
            break

        else:
            print('Geçersiz seçim. 1-5 arasında bir değer girin.')


if __name__ == '__main__':
    main()
