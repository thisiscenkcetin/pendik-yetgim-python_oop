"""
Basit ATM Simülasyonu

Seçenekler:
1 - Bakiye Sorgulama
2 - Para Çekme
3 - Para Yatırma
4 - Çıkış

Kullanıcı 4'e basmadığı sürece işlem yapmaya devam eder.
"""

def print_menu():
    print('\n----- ATM Menüsü -----')
    print('1) Bakiye Sorgulama')
    print('2) Para Çekme')
    print('3) Para Yatırma')
    print('4) Çıkış')


def read_choice():
    while True:
        s = input('Seçiminiz (1-4): ').strip()
        if s in ('1','2','3','4'):
            return int(s)
        print('Geçersiz seçim. 1-4 arasında bir sayı girin.')


def read_amount(prompt):
    while True:
        s = input(prompt).strip()
        try:
            v = float(s)
            if v <= 0:
                print('Miktar pozitif olmalıdır.')
                continue
            return v
        except ValueError:
            print('Geçersiz miktar. Lütfen sayı girin (ör. 100 veya 50.5).')


def main():
    balance = 1000.0  # Başlangıç bakiyesi (istendiğinde değiştirilebilir)
    print('ATM Simülasyonuna hoş geldiniz.')
    while True:
        print_menu()
        choice = read_choice()

        if choice == 1:
            print(f'Güncel bakiye: {balance:.2f} TL')

        elif choice == 2:
            amount = read_amount('Çekmek istediğiniz tutarı girin: ')
            if amount > balance:
                print('Yetersiz bakiye. İşlem iptal edildi.')
            else:
                balance -= amount
                print(f'{amount:.2f} TL çekildi. Yeni bakiye: {balance:.2f} TL')

        elif choice == 3:
            amount = read_amount('Yatırmak istediğiniz tutarı girin: ')
            balance += amount
            print(f'{amount:.2f} TL yatırıldı. Yeni bakiye: {balance:.2f} TL')

        elif choice == 4:
            print('Çıkılıyor. İyi günler!')
            break


if __name__ == '__main__':
    main()
