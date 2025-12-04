"""
Öğrenci Sınıfı 
isim
soyisim
numara
vize_notu
final_notu

notlari_gir()
ortalam_hesapla()
bilgileri_goster()

"""

from typing import Optional


class Student:
    def __init__(self, isim: str, soyisim: str, numara: str):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.vize_notu: Optional[float] = None
        self.final_notu: Optional[float] = None

    def _read_grade(self, prompt: str) -> float:
        while True:
            s = input(prompt).strip()
            try:
                val = float(s)
                if not (0 <= val <= 100):
                    print('Not 0-100 arası olmalıdır. Tekrar deneyin.')
                    continue
                return val
            except ValueError:
                print('Geçersiz değer. Lütfen sayı girin (örn. 85 veya 72.5).')

    def notlari_gir(self):
        """Kullanıcıdan vize ve final notlarını alır ve kaydeder."""
        print(f"{self.isim} {self.soyisim} ({self.numara}) için notları giriniz:")
        self.vize_notu = self._read_grade('Vize notu (0-100): ')
        self.final_notu = self._read_grade('Final notu (0-100): ')

    def ortalam_hesapla(self) -> Optional[float]:
        """Vize %40, Final %60 ağırlığıyla ortalamayı döndürür. Notlar yok ise None döner."""
        if self.vize_notu is None or self.final_notu is None:
            return None
        return round(self.vize_notu * 0.4 + self.final_notu * 0.6, 2)

    def bilgileri_goster(self):
        print('--- Öğrenci Bilgileri ---')
        print(f'İsim: {self.isim}')
        print(f'Soyisim: {self.soyisim}')
        print(f'Numara: {self.numara}')
        print(f'Vize notu: {self.vize_notu if self.vize_notu is not None else "(girilmedi)"}')
        print(f'Final notu: {self.final_notu if self.final_notu is not None else "(girilmedi)"}')
        ort = self.ortalam_hesapla()
        print(f'Ortalama: {ort if ort is not None else "(hesaplanamadı)"}')


def demo():
    print('Örnek kullanım - Öğrenci oluşturuluyor ve notlar giriliyor')
    s = Student('Ahmet', 'Yılmaz', 'S001')
    s.notlari_gir()
    s.bilgileri_goster()


if __name__ == '__main__':
    demo()
