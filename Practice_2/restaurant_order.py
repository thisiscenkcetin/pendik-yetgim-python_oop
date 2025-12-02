"""
Restoran Sipariş Sistemi
- Menüden seçim yapıp toplam tutarı hesaplar
"""

MENU = {
    1: ('Adana Kebap', 120.0),
    2: ('Lahmacun', 25.0),
    3: ('İskender', 95.0),
    4: ('Salata', 30.0),
    5: ('Ayran', 8.0),
}


def print_menu():
    print('Menü:')
    for k, (name, price) in MENU.items():
        print(f'{k}) {name} - {price:.2f} TL')
    print('0) Siparişi bitir')


def read_int(prompt):
    while True:
        s = input(prompt).strip()
        try:
            return int(s)
        except ValueError:
            print('Geçersiz giriş. Bir tam sayı girin.')


def main():
    print('Restoran Sipariş Sistemi')
    order = {}
    while True:
        print_menu()
        choice = read_int('Seçiminiz (ürün numarası): ')
        if choice == 0:
            break
        if choice not in MENU:
            print('Geçersiz ürün numarası.')
            continue
        qty = read_int('Adet: ')
        if qty <= 0:
            print('Adet pozitif olmalı.')
            continue
        order[choice] = order.get(choice, 0) + qty

    if not order:
        print('Hiç ürün seçilmedi.')
        return

    total = 0.0
    print('\nSipariş Özeti:')
    for k, qty in order.items():
        name, price = MENU[k]
        line = price * qty
        total += line
        print(f'- {name} x{qty} = {line:.2f} TL')

    print(f'Toplam: {total:.2f} TL')


if __name__ == '__main__':
    main()
