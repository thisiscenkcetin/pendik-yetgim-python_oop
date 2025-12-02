"""
Sınıf Geçme Sistemi
- Kullanıcıdan birden fazla not alır (boş bırakınca bitir)
- Ortalama hesaplanır, harf notu ve geçme/kalma durumu gösterilir
- Harf notu: A >=90, B >=80, C >=70, D >=60, F <60
- Geçme için ortalama >= 60
"""

def read_score(prompt):
    while True:
        s = input(prompt).strip()
        if s == "":
            return None
        try:
            v = float(s)
            if v < 0 or v > 100:
                print("Not 0-100 arası olmalı.")
                continue
            return v
        except ValueError:
            print("Geçersiz not. Lütfen sayı girin (örn. 85.5).")


def grade_letter(avg):
    if avg >= 90:
        return 'A'
    if avg >= 80:
        return 'B'
    if avg >= 70:
        return 'C'
    if avg >= 60:
        return 'D'
    return 'F'


def main():
    print('Sınıf Geçme Sistemi')
    print("Notları girin (0-100). Bitirmek için boş bırakın ve Enter'a basın.")
    scores = []
    while True:
        s = read_score('Not (boş = bitir): ')
        if s is None:
            break
        scores.append(s)

    if not scores:
        print('Hiç not girilmedi.')
        return

    avg = sum(scores) / len(scores)
    letter = grade_letter(avg)
    status = 'Geçti' if avg >= 60 else 'Kaldı'

    print(f'Not sayısı: {len(scores)}')
    print(f'Ortalama: {avg:.2f}')
    print(f'Harf notu: {letter}')
    print(f'Sonuç: {status}')


if __name__ == '__main__':
    main()
