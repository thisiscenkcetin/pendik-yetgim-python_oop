veri = {
    "Ad": [
        "Berkay", "Sezgin", "Aykut", "Cenk", "Elif",
        "Zeynep", "Mert", "Ahmet", "Selin", "Burak"
    ],
    "Soyad": [
        "Kaplan", "Yılmaz", "Demir", "Kaya", "Arslan",
        "Çelik", "Koç", "Şahin", "Aydın", "Öztürk"
    ],
    "Yaş": [25, 28, 26, 23, 27, 29, 31, 23, 26, 30],
    "Şehir": [
        "İstanbul", "Ankara", "Bursa", "İzmir", "Eskişehir",
        "İstanbul", "Kocaeli", "Sakarya", "Antalya", "Ankara"
    ],
    "Meslek": [
        "Bilgisayar Mühendisi",
        "Mekatronik Mühendisi",
        "Makine Mühendisi",
        "Yazılım Mühendisi",
        "Endüstri Mühendisi",
        "Veri Analisti",
        "Elektrik-Elektronik Mühendisi",
        "Bilgisayar Programcısı",
        "Yazılım Test Uzmanı",
        "Sistem Analisti"
    ],
    "Deneyim_Yılı": [2, 4, 3, 3, 5, 4, 6, 1, 3, 7],
    "Maaş": [32000, 38000, 35000, 30000, 42000, 40000, 50000, 28000, 36000, 55000]
}


if __name__ == '__main__':

    kayit_sayisi = len(veri.get('Ad', []))
    print(f'Kayıt sayısı: {kayit_sayisi}')
    if kayit_sayisi:
        print('Örnek kayıt:')
        print({k: v[0] for k, v in veri.items()})
