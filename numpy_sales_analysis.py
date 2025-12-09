"""NUMPY UYGULAMA SORUSU – GÜNLÜK SATIŞ ANALİZİ
 Senaryo:

Bir mağazanın 1 haftalık (7 günlük) satış verileri aşağıdaki gibidir:

Gün	Satış (TL)
Pazartesi	1200
Salı	1500
Çarşamba	1100
Perşembe	1800
Cuma	2100
Cumartesi	2500
Pazar	1700

Bu satışları NumPy kullanarak analiz ediniz.

İSTENENLER

Aşağıdaki maddelerin her birini NumPy kullanarak bulunuz:
Satış verilerini bir NumPy dizisine (array) aktarınız.
Haftalık toplam ciroyu hesaplayınız.
Günlük ortalama satışı hesaplayınız.
En yüksek satışın hangi gün ve kaç TL olduğunu bulunuz.
En düşük satışın hangi gün ve kaç TL olduğunu bulunuz.
Hafta içi satışları (Pazartesi–Cuma) ayrı bir diziye alınız.
Hafta sonu satışlarını (Cumartesi–Pazar) ayrı bir diziye alınız.
Hafta içi ortalama satış ile hafta sonu ortalama satışı karşılaştırınız:
"""

import numpy as np


def analiz():
    gunler = np.array([
        'Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma', 'Cumartesi', 'Pazar'
    ])
    satis = np.array([1200, 1500, 1100, 1800, 2100, 2500, 1700], dtype=float)

    toplam = satis.sum()
    ortalama = satis.mean()

    max_idx = satis.argmax()
    min_idx = satis.argmin()

    en_yuksek = {'gun': gunler[max_idx], 'tutar': satis[max_idx]}
    en_dusuk = {'gun': gunler[min_idx], 'tutar': satis[min_idx]}

    hafta_ici_mask = np.arange(len(gunler)) < 5  # 0-4
    hafta_sonu_mask = ~hafta_ici_mask

    hafta_ici = satis[hafta_ici_mask]
    hafta_sonu = satis[hafta_sonu_mask]

    hafta_ici_ort = hafta_ici.mean()
    hafta_sonu_ort = hafta_sonu.mean()

    return {
        'gunler': gunler,
        'satis': satis,
        'toplam': toplam,
        'ortalama': ortalama,
        'en_yuksek': en_yuksek,
        'en_dusuk': en_dusuk,
        'hafta_ici': hafta_ici,
        'hafta_sonu': hafta_sonu,
        'hafta_ici_ort': hafta_ici_ort,
        'hafta_sonu_ort': hafta_sonu_ort,
    }


def yazdir(sonuc):
    print('--- Günlük Satış Analizi (NumPy) ---')
    print('Satışlar   :', sonuc['satis'])
    print(f"Toplam     : {sonuc['toplam']:.2f} TL")
    print(f"Ortalama   : {sonuc['ortalama']:.2f} TL")
    print(f"En yüksek  : {sonuc['en_yuksek']['gun']} -> {sonuc['en_yuksek']['tutar']:.2f} TL")
    print(f"En düşük   : {sonuc['en_dusuk']['gun']} -> {sonuc['en_dusuk']['tutar']:.2f} TL")
    print('Hafta içi  :', sonuc['hafta_ici'])
    print('Hafta sonu :', sonuc['hafta_sonu'])
    print(f"Hafta içi ortalama : {sonuc['hafta_ici_ort']:.2f} TL")
    print(f"Hafta sonu ortalama: {sonuc['hafta_sonu_ort']:.2f} TL")

    fark = sonuc['hafta_sonu_ort'] - sonuc['hafta_ici_ort']
    durum = 'daha yüksek' if fark > 0 else 'daha düşük' if fark < 0 else 'eşit'
    print(f"Hafta sonu ortalama, hafta içi ortalamadan {abs(fark):.2f} TL {durum}.")


def main():
    sonuc = analiz()
    yazdir(sonuc)


if __name__ == '__main__':
    main()
