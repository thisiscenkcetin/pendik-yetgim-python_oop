"""
Soru:
Bir şirketin çalışan sistemi için kalıtım kullanın. Temel Calisan sınıfından farklı çalışan tipleri türetin.
İstenenler:

Calisan base sınıfı (ad, soyad, maas, departman)
Yazilimci ve Muhasebeci alt sınıfları oluşturun
Her alt sınıf kendi özel özelliklerini eklesin (Yazılımcı: programlama_dilleri, Muhasebeci: sertifikalar)
maas_hesapla() metodunu her sınıfta override edin (Yazılımcılar %20, Muhasebeçiler %10 zam alsın)
bilgi_goster() metodunu override edin
"""

from typing import List


class Calisan:
    def __init__(self, ad: str, soyad: str, maas: float, departman: str):
        self.ad = ad
        self.soyad = soyad
        try:
            self.maas = float(maas)
        except Exception:
            raise ValueError('Maaş sayısal olmalıdır')
        self.departman = departman

    def maas_hesapla(self) -> float:
        """Temel hesaplama: ek zam yok, sadece mevcut maaşı döndürür."""
        return self.maas

    def bilgi_goster(self) -> str:
        """Çalışanın temel bilgilerini döndürür."""
        return f'{self.ad} {self.soyad} | Departman: {self.departman} | Maaş: {self.maas:.2f} TL'

    def __str__(self) -> str:
        return self.bilgi_goster()


class Yazilimci(Calisan):
    def __init__(self, ad: str, soyad: str, maas: float, departman: str, programlama_dilleri: List[str] = None):
        super().__init__(ad, soyad, maas, departman)
        self.programlama_dilleri = programlama_dilleri or []

    def maas_hesapla(self) -> float:
        """Yazılımcılar için %20 zam uygulanmış maaşı döndürür."""
        return round(self.maas * 1.20, 2)

    def bilgi_goster(self) -> str:
        diller = ', '.join(self.programlama_dilleri) if self.programlama_dilleri else 'Yok'
        return (f'{self.ad} {self.soyad} | Yazılımcı | Departman: {self.departman} | '
                f'Maaş: {self.maas:.2f} TL | Zamlı Maaş: {self.maas_hesapla():.2f} TL | '
                f'Diller: {diller}')

    def dil_ekle(self, dil: str) -> None:
        if dil and dil not in self.programlama_dilleri:
            self.programlama_dilleri.append(dil)


class Muhasebeci(Calisan):
    def __init__(self, ad: str, soyad: str, maas: float, departman: str, sertifikalar: List[str] = None):
        super().__init__(ad, soyad, maas, departman)
        self.sertifikalar = sertifikalar or []

    def maas_hesapla(self) -> float:
        """Muhasebeciler için %10 zam uygulanmış maaşı döndürür."""
        return round(self.maas * 1.10, 2)

    def bilgi_goster(self) -> str:
        serts = ', '.join(self.sertifikalar) if self.sertifikalar else 'Yok'
        return (f'{self.ad} {self.soyad} | Muhasebeci | Departman: {self.departman} | '
                f'Maaş: {self.maas:.2f} TL | Zamlı Maaş: {self.maas_hesapla():.2f} TL | '
                f'Sertifikalar: {serts}')

    def sertifika_ekle(self, sertifika: str) -> None:
        if sertifika and sertifika not in self.sertifikalar:
            self.sertifikalar.append(sertifika)


def demo():
    print('Çalışan sınıfları demo')
    yaz = Yazilimci('Deniz', 'Kaya', 10000, 'Yazılım', ['Python', 'Java'])
    muh = Muhasebeci('Ahmet', 'Demir', 8000, 'Muhasebe', ['SMMM'])

    print('\n-- Bilgiler (orijinal) --')
    print(yaz.bilgi_goster())
    print(muh.bilgi_goster())

    print('\n-- Maas hesaplamaları (zam uygulanmış) --')
    print(f'Yazılımcı zamlı maaş: {yaz.maas_hesapla():.2f} TL')
    print(f'Muhasebeci zamlı maaş: {muh.maas_hesapla():.2f} TL')

    print('\n-- Özellik güncellemeleri --')
    yaz.dil_ekle('Go')
    muh.sertifika_ekle('Vergi Uzmanı')
    print(yaz.bilgi_goster())
    print(muh.bilgi_goster())


if __name__ == '__main__':
    demo()
