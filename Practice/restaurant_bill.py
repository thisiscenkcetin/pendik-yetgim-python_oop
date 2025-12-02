"""
Restoran Hesabı
- Yemek fiyatı, bahşiş oranı ve kişi sayısı alır
- Kişi başı toplam tutarı hesaplar
"""

def read_positive_float(prompt, allow_zero=False):
    while True:
        s = input(prompt).strip()
        try:
            v = float(s)
            if v < 0 or (not allow_zero and v == 0):
                raise ValueError
            return v
        except ValueError:
            print('Geçersiz giriş. Pozitif bir sayı girin.')


def read_positive_int(prompt):
    while True:
        s = input(prompt).strip()
        try:
            v = int(s)
            if v <= 0:
                raise ValueError
            return v
        except ValueError:
            print('Geçersiz giriş. Pozitif bir tam sayı girin.')


def main():
    print('Restoran Hesabı')
    total = read_positive_float('Toplam yemek fiyatını girin: ')
    tip = read_positive_float('Bahşiş oranı (%) girin (örn. 10): ', allow_zero=True)
    people = read_positive_int('Kaç kişi paylaşacak? ')

    total_with_tip = total * (1 + tip/100)
    per_person = total_with_tip / people

    print(f'Kişi başı ödenecek: {per_person:.2f} TL (Toplam: {total_with_tip:.2f} TL)')


if __name__ == '__main__':
    main()
