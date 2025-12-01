"""
Otobüs Bileti Fiyatı Uygulaması

- Temel ücret = km * 2.5
- 0-12 yaş: %50 indirim
- 12-24 yaş: %25 indirim (12 dahil değil, 12'den büyük ve 24'e kadar)
- 65 yaş üzeri (>65): %30 indirim
- Mesafe > 100 km ise ek %20 indirim (yaş indiriminden sonra uygulanır)

"""


def read_positive_float(prompt):
    while True:
        s = input(prompt).strip()
        try:
            value = float(s)
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Geçersiz giriş. Lütfen pozitif bir sayı girin.")


def read_nonnegative_int(prompt):
    while True:
        s = input(prompt).strip()
        try:
            # Tam sayı bekliyoruz
            if "." in s or "," in s:
                raise ValueError
            value = int(s)
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print("Geçersiz giriş. Lütfen sıfır veya daha büyük bir tam sayı girin.")


def calculate_ticket_price(age, km):
    base_price = km * 2.5

    # Yaş indirim oranı
    age_discount = 0.0
    # Bu uygulamada 12 yaş ve altı %50, 13-24 arası %25, >65 ise %30
    if age <= 12:
        age_discount = 0.50
    elif 12 < age <= 24:
        age_discount = 0.25
    elif age > 65:
        age_discount = 0.30

    price_after_age = base_price * (1 - age_discount)

    # Uzun yol indirimi (100 km üstü)
    long_distance_discount = 0.0
    if km > 100:
        long_distance_discount = 0.20

    final_price = price_after_age * (1 - long_distance_discount)

    return {
        'base_price': base_price,
        'age_discount': age_discount,
        'price_after_age': price_after_age,
        'long_distance_discount': long_distance_discount,
        'final_price': final_price,
    }


def main():
    print("Otobüs Bileti Fiyatı Hesaplayıcı")
    age = read_nonnegative_int("Yaşınızı girin (tam sayı): ")
    km = read_positive_float("Gidilecek mesafeyi km cinsinden girin: ")

    result = calculate_ticket_price(age, km)

    print("\nHesaplama Özeti:")
    print(f"- Temel ücret (km * 2.5): {result['base_price']:.2f} TL")
    if result['age_discount'] > 0:
        print(f"- Yaş indirimi: {int(result['age_discount']*100)}% => {result['price_after_age']:.2f} TL")
    else:
        print(f"- Yaş indirimi: Yok => {result['price_after_age']:.2f} TL")

    if result['long_distance_discount'] > 0:
        print(f"- Uzun mesafe indirimi: {int(result['long_distance_discount']*100)}% => {result['final_price']:.2f} TL")
    else:
        print(f"- Uzun mesafe indirimi: Yok => {result['final_price']:.2f} TL")

    print(f"\nToplam ödenecek tutar: {result['final_price']:.2f} TL")


if __name__ == '__main__':
    main()
