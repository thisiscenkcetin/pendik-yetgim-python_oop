"""
Multiplication Quiz
- Rastgele çarpma soruları sorar, kullanıcı kaç soru istediğini belirler.
- Doğru sayısını ve başarı yüzdesini gösterir.
"""

import random


def read_int(prompt, minv=1, maxv=1000):
    while True:
        s = input(prompt).strip()
        try:
            v = int(s)
            if v < minv or v > maxv:
                print(f'Lütfen {minv}-{maxv} arasında bir sayı girin.')
                continue
            return v
        except ValueError:
            print('Geçersiz giriş. Tam sayı girin.')


def main():
    print('Çarpma Quiz')
    n = read_int('Kaç soru istiyorsunuz? ', 1, 100)
    correct = 0
    for i in range(1, n+1):
        a = random.randint(1, 12)
        b = random.randint(1, 12)
        ans = a * b
        try:
            r = int(input(f'Soru {i}: {a} x {b} = '))
        except ValueError:
            print('Geçersiz giriş, yanlış sayıldı.')
            continue
        if r == ans:
            print('Doğru!')
            correct += 1
        else:
            print(f'Yanlış. Doğru cevap {ans}')
    print(f'Quiz tamamlandı. Doğru: {correct}/{n} (%{correct*100/n:.1f})')


if __name__ == '__main__':
    main()
