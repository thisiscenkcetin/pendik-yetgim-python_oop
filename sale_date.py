from typing import Optional, List, Dict, Any


veri: Dict[str, List[Any]] = {
    "Tarih": [
        "2023-10-01",
        "2023-10-01",
        "2023-10-02",
        "2023-10-02",
        "2023-10-03"
    ],
    "Urun_Adi": [
        "Laptop",
        "Mouse",
        "Kitap A",
        "Klavye",
        "Kitap B"
    ],
    "Kategori": [
        "Elektronik",
        "Elektronik",
        "Kitap",
        "Elektronik",
        "Kitap"
    ],
    "Birim_Fiyat": [
        25000.0,
        300.0,
        120.0,
        750.0,
        None   # NaN yerine None kullanıldı
    ],
    "Satilan_Adet": [
        5.0,
        20.0,
        15.0,
        10.0,
        8.0
    ]
}


def toplam_gelir(veri_dict: Dict[str, List[Any]]) -> float:
    """Birim_Fiyat veya Satilan_Adet None ise 0 kabul ederek toplam geliri hesaplar."""
    fiyatlar = veri_dict.get('Birim_Fiyat', [])
    adetler = veri_dict.get('Satilan_Adet', [])
    toplam = 0.0
    for f, a in zip(fiyatlar, adetler):
        f_val = 0.0 if f is None else float(f)
        a_val = 0.0 if a is None else float(a)
        toplam += f_val * a_val
    return toplam


if __name__ == '__main__':
    print('Kayıt sayısı:', len(veri.get('Tarih', [])))
    print('Örnek kayıtlar:')
    for i in range(len(veri.get('Tarih', []))):
        print({k: v[i] for k, v in veri.items()})
    print('\nToplam gelir (None->0):', toplam_gelir(veri))
