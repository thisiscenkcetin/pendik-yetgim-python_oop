"""
Artık Yıl Kontrolü
Kural: Yıl 4'e bölünebilir ve 100'e bölünemez veya 400'e bölünebilir.
Örnek artık yıllar: 2000, 2004, 2008, 2012, 2016, 2020, 2024, ...
"""


def read_year(prompt):
    while True:
        s = input(prompt).strip()
        if s == "":
            print("Geçersiz giriş. Lütfen bir yıl girin.")
            continue
        if not (s.lstrip('-').isdigit()):
            print("Geçersiz giriş. Lütfen tam sayı biçiminde bir yıl girin.")
            continue
        try:
            year = int(s)
            return year
        except ValueError:
            print("Geçersiz giriş. Lütfen tekrar deneyin.")


def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def main():
    print('Artık Yıl Kontrolü')
    year = read_year('Yıl girin (ör. 2024): ')

    if is_leap_year(year):
        print(f"{year} bir artık yıldır.")
    else:
        print(f"{year} bir artık yıl değildir.")


if __name__ == '__main__':
    main()
