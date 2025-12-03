"""
Palindrome Kontrolü
- Girilen kelime veya cümlenin palindrome (tersi kendisi) olup olmadığını kontrol eder.
- Alfasayısal karakterler dışında kalanlar atılır, büyük/küçük harf farkı yok sayılır.
"""

import re


def is_palindrome(s: str) -> bool:
    cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    return cleaned == cleaned[::-1]


def main():
    s = input('Bir kelime veya cümle girin: ').strip()
    if not s:
        print('Boş giriş. Lütfen bir ifade girin.')
        return
    if is_palindrome(s):
        print('Girilen ifade palindrome (tersiyle aynı).')
    else:
        print('Girilen ifade palindrome değildir.')


if __name__ == '__main__':
    main()
