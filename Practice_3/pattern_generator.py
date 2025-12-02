"""
Pattern Generator
- Kullanıcıdan desen tipi ve boyut alır ve deseni çizer.
- Desenler: 1) Right triangle 2) Pyramid 3) Square
"""

def read_int(prompt, minv=1, maxv=50):
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


def right_triangle(n):
    for i in range(1, n+1):
        print('*' * i)


def pyramid(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '* ' * (i + 1))


def square(n):
    for i in range(n):
        print('* ' * n)


def main():
    print('Desen Oluşturucu')
    print('1) Sağ üçgen')
    print('2) Piramit')
    print('3) Kare')
    choice = read_int('Desen seçin (1-3): ', 1, 3)
    size = read_int('Boyut girin (1-50): ', 1, 50)
    print()
    if choice == 1:
        right_triangle(size)
    elif choice == 2:
        pyramid(size)
    else:
        square(size)


if __name__ == '__main__':
    main()
