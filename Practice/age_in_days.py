"""
Yaş Gün Hesaplayıcı
- Doğum tarihini alır ve bugüne kadar kaç gün geçtiğini hesaplar.
- Kabul edilen formatlar: YYYY-MM-DD, DD/MM/YYYY, DD.MM.YYYY
"""

from datetime import datetime, date


def read_date(prompt):
    formats = ["%Y-%m-%d", "%d/%m/%Y", "%d.%m.%Y"]
    while True:
        s = input(prompt).strip()
        for fmt in formats:
            try:
                return datetime.strptime(s, fmt).date()
            except ValueError:
                continue
        print('Geçersiz tarih. Örnek: 1990-05-21 veya 21/05/1990')


def main():
    print('Yaş Gün Hesaplayıcı')
    bdate = read_date('Doğum tarihinizi girin (YYYY-MM-DD veya DD/MM/YYYY): ')
    today = date.today()
    if bdate > today:
        print('Doğum tarihi gelecekte olamaz.')
        return
    delta = today - bdate
    years = delta.days // 365
    print(f'Bugüne kadar {delta.days} gün geçti (yaklaşık {years} yıl).')


if __name__ == '__main__':
    main()
