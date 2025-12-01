def read_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Geçersiz sayı. Lütfen tekrar deneyin.")


def main():
    a = read_number("1. sayıyı girin: ")
    b = read_number("2. sayıyı girin: ")

    if a > b:
        print(f"Büyük olan sayı: {a}")
    elif b > a:
        print(f"Büyük olan sayı: {b}")
    else:
        print(f"İki sayı eşit: {a}")


if __name__ == "__main__":
    main()
