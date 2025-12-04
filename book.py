"""
Bir kütüphane için kitap yönetim sistemi oluşturun. Kitap sınıfı oluşturup, kitap bilgilerini saklayın ve görüntüleyin.İstenenler:

Kitap sınıfı oluşturun
_init_ metodunda: ad, yazar, sayfa_sayisi, yayın_yılı alınsın
bilgi_goster() metodu ile kitap bilgilerini ekrana yazdırın
eski_mi() metodu ile kitabın 10 yıldan eski olup olmadığını kontrol edin (2025 baz alınarak)
"""

from dataclasses import dataclass


@dataclass
class Book:
    ad: str
    yazar: str
    sayfa_sayisi: int
    yayin_yili: int

    def bilgi_goster(self) -> None:
        print('--- Kitap Bilgileri ---')
        print(f'Ad: {self.ad}')
        print(f'Yazar: {self.yazar}')
        print(f'Sayfa sayısı: {self.sayfa_sayisi}')
        print(f'Yayın yılı: {self.yayin_yili}')

    def eski_mi(self, baz_yil: int = 2025) -> bool:
        """Baz yılı 2025 alır; kitap yayın yılının baz yıldan en az 10 yıl önce olup olmadığını kontrol eder."""
        return (baz_yil - self.yayin_yili) >= 10


def demo():
    k = Book('Suç ve Ceza', 'Fyodor Dostoyevski', 430, 1866)
    k.bilgi_goster()
    print('Eski mi?:', 'Evet' if k.eski_mi() else 'Hayır')


if __name__ == '__main__':
    demo()
