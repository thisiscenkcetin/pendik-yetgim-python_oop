"""
Sayı Tahmin Oyunu

- Bilgisayar 1-100 arasında rastgele bir sayı seçer.
- Kullanıcının 1-100 arasında tahminler alır.
- Kullanıcının 5 hakkı vardır; 5 hakkın içinde sayıyı bulursa "Tebrikler" yazılır,
  aksi halde "Kaybettiniz" ve doğru sayı gösterilir.
"""

import random


def read_guess(prompt: str) -> int:
    while True:
        s = input(prompt).strip()
        try:
            v = int(s)
            if 1 <= v <= 100:
                return v
            print('Lütfen 1 ile 100 arasında bir tam sayı girin.')
        except ValueError:
            print('Geçersiz giriş. Lütfen bir tam sayı girin.')


def main():
    print('Sayı Tahmin Oyununa Hoşgeldiniz! (1-100)')
    secret = random.randint(1, 100)
    max_attempts = 5

    for attempt in range(1, max_attempts + 1):
        guess = read_guess(f'{attempt}. tahmininizi girin: ')
        if guess == secret:
            print(f'Tebrikler! {attempt}. denemede bildiniz.')
            break
        elif guess < secret:
            print('Daha büyük bir sayı deneyin.')
        else:
            print('Daha küçük bir sayı deneyin.')
    else:
        # Döngü normal şekilde sonlandı (break çağrılmadı)
        print(f'Kaybettiniz. Doğru sayı: {secret}')


if __name__ == '__main__':
    main()
