def read_int(prompt):
    while True:
        s = input(prompt).strip()
        try:
            # Tam sayı bekliyoruz; ondalıklı girişleri reddedelim
            if "." in s or "," in s:
                raise ValueError
            return int(s)
        except ValueError:
            print("Geçersiz giriş. Lütfen bir tam sayı girin.")


def main():
    n = read_int("Bir tam sayı girin: ")
    if n % 2 == 0:
        print(f"Girilen sayı çift: {n}")
    else:
        print(f"Girilen sayı tek: {n}")


if __name__ == "__main__":
    main()
