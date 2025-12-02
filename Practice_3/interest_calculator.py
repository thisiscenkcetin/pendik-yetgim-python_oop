"""
Interest Calculator (Compound Interest)
- Ana para, yıllık faiz oranı (%), ve yıl sayısı alınır.
- Her yılın sonunda bakiye gösterilir.
"""

def read_positive_float(prompt):
    while True:
        s = input(prompt).strip()
        try:
            v = float(s)
            if v < 0:
                print('Negatif değer girilemez.')
                continue
            return v
        except ValueError:
            print('Geçersiz giriş. Sayı girin.')


def read_positive_int(prompt):
    while True:
        s = input(prompt).strip()
        try:
            v = int(s)
            if v <= 0:
                print('Pozitif bir tam sayı girin.')
                continue
            return v
        except ValueError:
            print('Geçersiz giriş. Tam sayı girin.')


def main():
    print('Bileşik Faiz Hesaplayıcı')
    principal = read_positive_float('Ana para (TL): ')
    rate = read_positive_float('Yıllık faiz oranı (%) : ')
    years = read_positive_int('Yıl sayısı: ')

    balance = principal
    print('\nYıl başı bakiye gösterimi:')
    for y in range(1, years+1):
        balance *= (1 + rate/100)
        print(f'Yıl {y}: {balance:.2f} TL')

    print(f'Toplam: {balance:.2f} TL (Başlangıç: {principal:.2f} TL, Faiz: {rate}%)')


if __name__ == '__main__':
    main()
