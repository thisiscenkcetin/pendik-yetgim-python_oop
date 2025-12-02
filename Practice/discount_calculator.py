"""
İndirim Hesaplayıcı
- Ürün fiyatı ve indirim oranı (%) alır, yeni fiyatı hesaplar.
"""

def read_positive_float(prompt):
    while True:
        s = input(prompt).strip()
        try:
            v = float(s)
            if v < 0:
                raise ValueError
            return v
        except ValueError:
            print('Geçersiz giriş. Pozitif bir sayı girin.')


def read_discount(prompt):
    while True:
        v = read_positive_float(prompt)
        if v > 100:
            print('İndirim oranı %0-100 arasında olmalıdır.')
        else:
            return v


def main():
    print('İndirim Hesaplayıcı')
    price = read_positive_float('Ürün fiyatını girin: ')
    discount = read_discount('İndirim oranını yüzde olarak girin (örn. 25): ')

    new_price = price * (1 - discount/100)
    saved = price - new_price

    print(f'Yeni fiyat: {new_price:.2f} TL')
    print(f'Kazanç/İndirim tutarı: {saved:.2f} TL')


if __name__ == '__main__':
    main()
