"""
Luhn Algoritması ile Kredi Kartı Doğrulama
- Girilen sayının Luhn kuralına göre geçerli olup olmadığını kontrol eder.
"""

def read_digits(prompt):
    while True:
        s = input(prompt).strip().replace(' ','')
        if not s:
            print('Boş giriş. Tekrar deneyin.')
            continue
        if not s.isdigit():
            print('Yalnızca rakam girin (boşluk kabul edilir).')
            continue
        return s


def luhn_check(number: str) -> bool:
    total = 0
    reverse_digits = number[::-1]
    for i, ch in enumerate(reverse_digits):
        d = int(ch)
        if i % 2 == 1:
            d = d * 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0


def main():
    print('Luhn Doğrulama')
    num = read_digits('Kredi kartı numarasını girin (boşluklar kabul edilir): ')
    ok = luhn_check(num)
    if ok:
        print('Geçerli (Luhn)')
    else:
        print('Geçersiz (Luhn)')


if __name__ == '__main__':
    main()
