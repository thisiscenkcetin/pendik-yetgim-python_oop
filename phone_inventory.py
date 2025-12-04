"""
Soru:
Bir teknoloji mağazasının telefon envanteri için sistem yapın. Telefonları listeye ekleyin ve batarya durumunu güncelleyebilme özelliği ekleyin.İstenenler:

Telefon sınıfı oluşturun (marka, model, fiyat, batarya_yuzdesi)
get_batarya() ve set_batarya() metotları ekleyin
sarj_gerekli_mi() metodu ile batarya %20'nin altında mı kontrol edin
Birden fazla telefon oluşturup liste içinde saklayın
Tüm telefonları ve batarya durumlarını listeleyin
"""

from typing import List


class Phone:
    def __init__(self, marka: str, model: str, fiyat: float, batarya_yuzdesi: int):
        self.marka = marka
        self.model = model
        self.fiyat = float(fiyat)
        # normalize battery to 0-100
        self.batarya_yuzdesi = max(0, min(100, int(batarya_yuzdesi)))

    def get_batarya(self) -> int:
        """Batarya yüzdesini döndürür."""
        return self.batarya_yuzdesi

    def set_batarya(self, yuzde: int) -> None:
        """Batarya yüzdesini 0-100 aralığına ayarlar; geçersizse ValueError fırlatır."""
        try:
            v = int(yuzde)
        except Exception:
            raise ValueError('Batarya yüzdesi tam sayı olmalıdır')
        if v < 0 or v > 100:
            raise ValueError('Batarya yüzdesi 0-100 arasında olmalıdır')
        self.batarya_yuzdesi = v

    def sarj_gerekli_mi(self) -> bool:
        """Batarya %20'nin altındaysa True döner."""
        return self.batarya_yuzdesi < 20

    def __str__(self) -> str:
        return f"{self.marka} {self.model} - {self.fiyat:.2f} TL - Batarya: {self.batarya_yuzdesi}%"


class Inventory:
    def __init__(self):
        self.phones: List[Phone] = []

    def add_phone(self, phone: Phone) -> None:
        self.phones.append(phone)

    def update_battery(self, index: int, yuzde: int) -> None:
        if index < 0 or index >= len(self.phones):
            raise IndexError('Geçersiz telefon indeksi')
        self.phones[index].set_batarya(yuzde)

    def list_phones(self) -> None:
        if not self.phones:
            print('Envanter boş.')
            return
        for i, p in enumerate(self.phones, start=1):
            status = 'Şarj gerekli' if p.sarj_gerekli_mi() else 'Şarj yeterli'
            print(f"{i}. {p} -> {status}")


def demo():
    inv = Inventory()
    # Örnek telefonlar ekleyelim
    inv.add_phone(Phone('Apple', 'iPhone 14', 25000, 85))
    inv.add_phone(Phone('Samsung', 'Galaxy S22', 18000, 15))
    inv.add_phone(Phone('Xiaomi', 'Redmi Note 12', 8000, 45))

    print('Başlangıç envanteri:')
    inv.list_phones()

    print('\nGüncelleme: 2. telefonu %50 bataryaya ayarlıyoruz...')
    inv.update_battery(1, 50)  # index 1 => 2. telefon
    inv.list_phones()

    print('\nHatalı değer denemesi (batarya = 150) -> ValueError bekleniyor:')
    try:
        inv.update_battery(0, 150)
    except Exception as e:
        print('Hata:', e)


if __name__ == '__main__':
    demo()
