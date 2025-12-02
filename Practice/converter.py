"""
Basit Dönüştürücü
- Metre <-> Feet
- Kilogram <-> Pound
"""

METRE_TO_FEET = 3.28084
KG_TO_POUND = 2.20462


def read_float(prompt):
    while True:
        s = input(prompt).strip()
        try:
            return float(s)
        except ValueError:
            print("Geçersiz sayı. Lütfen tekrar deneyin.")


def menu():
    print("Basit Dönüştürücü")
    print("1) Metre -> Feet")
    print("2) Feet -> Metre")
    print("3) Kilogram -> Pound")
    print("4) Pound -> Kilogram")
    print("0) Çıkış")

    while True:
        choice = input("Seçiminiz: ").strip()
        if choice in ['0','1','2','3','4']:
            return choice
        print("Geçersiz seçim. 0-4 arasında bir değer girin.")


def metre_to_feet(m):
    return m * METRE_TO_FEET


def feet_to_metre(f):
    return f / METRE_TO_FEET


def kg_to_pound(kg):
    return kg * KG_TO_POUND


def pound_to_kg(lb):
    return lb / KG_TO_POUND


def main():
    while True:
        choice = menu()
        if choice == '0':
            print('Çıkılıyor.')
            break
        if choice == '1':
            m = read_float('Metre girin: ')
            print(f'{m} m = {metre_to_feet(m):.4f} ft')
        elif choice == '2':
            f = read_float('Feet girin: ')
            print(f'{f} ft = {feet_to_metre(f):.4f} m')
        elif choice == '3':
            kg = read_float('Kilogram girin: ')
            print(f'{kg} kg = {kg_to_pound(kg):.4f} lb')
        elif choice == '4':
            lb = read_float('Pound girin: ')
            print(f'{lb} lb = {pound_to_kg(lb):.4f} kg')
        print()


if __name__ == '__main__':
    main()
