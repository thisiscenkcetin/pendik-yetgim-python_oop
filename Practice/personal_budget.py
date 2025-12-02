"""
Kişisel Bütçe
- Kullanıcıdan gelirleri ve giderleri alır (teker teker, boş girildiğinde bitir)
- Toplam gelir, toplam gider ve kalan miktarı yazdırır
"""


def read_amount(prompt):
    while True:
        s = input(prompt).strip()
        if s == '':
            return None
        try:
            return float(s)
        except ValueError:
            print('Geçersiz sayı. Ondalıklı veya tam sayı girin (ör: 2500 veya 99.99).')


def collect_list(prompt):
    items = []
    while True:
        v = read_amount(prompt)
        if v is None:
            break
        items.append(v)
    return items


def main():
    print('Kişisel Bütçe Hesaplayıcı')
    print("Gelirlerinizi girin (her biri için Enter). Bitirmek için boş bırakın ve Enter'a basın.")
    incomes = collect_list('Gelir (boş = bitir): ')
    print('\nGiderlerinizi girin (her biri için Enter). Bitirmek için boş bırakın.')
    expenses = collect_list('Gider (boş = bitir): ')

    total_income = sum(incomes)
    total_expense = sum(expenses)
    remaining = total_income - total_expense

    print('\nÖzet:')
    print(f'- Toplam gelir: {total_income:.2f} TL')
    print(f'- Toplam gider: {total_expense:.2f} TL')
    print(f'- Kalan: {remaining:.2f} TL')


if __name__ == '__main__':
    main()
