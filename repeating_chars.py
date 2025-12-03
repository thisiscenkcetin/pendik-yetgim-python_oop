"""
Tekrar Eden Karakterleri Bulma

Kullanıcıdan bir kelime veya cümle alınır ve içinde birden fazla geçen
karakterler ile sayıları ekrana yazdırılır.

Davranış:
- Büyük/küçük harf ayrımı yapılır (A ve a farklı kabul edilir). Eğer isterseniz
  küçültülmüş olarak sayma davranışı da ekleyebilirim.
"""

from collections import Counter


def main():
    s = input('Bir kelime veya cümle girin: ')
    if not s:
        print('Boş giriş. Lütfen bir ifade girin.')
        return

    counts = Counter(s)
    repeats = {ch: cnt for ch, cnt in counts.items() if cnt > 1}

    if not repeats:
        print('Tekrar eden karakter bulunamadı.')
        return

    # Sıklığa göre azalan sırada göster
    sorted_repeats = sorted(repeats.items(), key=lambda x: (-x[1], x[0]))
    print('Tekrar eden karakterler ve sayıları:')
    for ch, cnt in sorted_repeats:
        # Görsel için boşlukları görünür hale getir
        display = ch if ch != ' ' else '<space>'
        print(f"'{display}': {cnt}")


if __name__ == '__main__':
    main()
