import numpy as np


veri = {
    'Urun': ['A', 'B', 'C', 'D', 'E'],
    'Fiyat': [100, 150, np.nan, 200, 120],
    'Adet': [10, 5, 8, np.nan, 15],
    'Stok Kodu': ['SK001', 'SK002', 'SK003', 'SK004', 'SK005']
}


if __name__ == '__main__':
    print('veri sözlüğü oluşturuldu:')
    for k, v in veri.items():
        print(f'- {k}: {v}')


    print('\nNaN kontrolü:')
    for k, v in veri.items():
        arr = np.array(v, dtype=object)

        nan_count = int(np.sum([1 for x in arr if isinstance(x, float) and np.isnan(x)]))
        print(f"{k}: {nan_count} NaN")

    fiyat = np.array(veri['Fiyat'], dtype=float)
    adet = np.array(veri['Adet'], dtype=float)
    fiyat_filled = np.nan_to_num(fiyat, nan=0.0)
    adet_filled = np.nan_to_num(adet, nan=0.0)
    toplam_deger = np.sum(fiyat_filled * adet_filled)
    print(f"\nToplam stok değeri (NaN->0 ile): {toplam_deger:.2f} TL")
