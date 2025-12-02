"""
Advanced Number Guess Game
- Kullanıcı min/max belirler, bilgisayar rastgele seçer.
- İpuçları: tahminin yüksek/low olduğu, ayrıca kalan aralık güncellenir.
- Puan sistemi: başlangıç puanı 100, her yanlış tahminde puan azalır.
"""

import random
import math


def read_int(prompt, minv=None, maxv=None):
    while True:
        s = input(prompt).strip()
        try:
            v = int(s)
            if minv is not None and v < minv:
                print(f'Lütfen en az {minv} girin.')
                continue
            if maxv is not None and v > maxv:
                print(f'Lütfen en fazla {maxv} girin.')
                continue
            return v
        except ValueError:
            print('Geçersiz giriş. Tam sayı girin.')


def main():
    print('Sayı Tahmin Oyunu Gelişmiş')
    low = read_int('Minimum değer (ör. 1): ', None, None)
    high = read_int('Maksimum değer (ör. 100): ', low+1, None)
    secret = random.randint(low, high)
    attempts = 0
    score = 100
    max_attempts = max(5, int(math.log2(high - low + 1)) + 3)
    current_low, current_high = low, high

    while attempts < max_attempts:
        print(f'Kalan tahmin hakkı: {max_attempts - attempts}, Aralık: [{current_low}, {current_high}], Puan: {score}')
        guess = read_int('Tahmininiz: ', current_low, current_high)
        attempts += 1
        if guess == secret:
            print(f'Tebrikler! {attempts}. denemede buldunuz. Puanınız: {score}')
            break
        if guess < secret:
            print('Daha büyük bir sayı deneyin.')
            current_low = max(current_low, guess + 1)
        else:
            print('Daha küçük bir sayı deneyin.')
            current_high = min(current_high, guess - 1)
        # puan azaltma
        score -= max(1, int(100 / max_attempts))
    else:
        print(f'Kaybettiniz. Doğru sayı: {secret}. Puanınız: {score}')


if __name__ == '__main__':
    main()
