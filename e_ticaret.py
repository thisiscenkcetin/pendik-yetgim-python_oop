#!/usr/bin/env python3
"""
Soru:
Kapsamlı bir e-ticaret sipariş sistemi oluşturun. Farklı ürün tipleri, sepet yönetimi ve indirim hesaplamaları yapın.
İstenenler:

Urun base sınıfı ve alt sınıfları (Elektronik, Giyim)
Her ürün tipinin kendine özel özellikleri olsun
Sepet sınıfı ile ürünleri yönetin
Musteri sınıfı ile müşteri bilgileri ve indirim oranını saklayın
Property kullanarak indirim oranını kontrol edin (0-50 arası)
Polymorphism ile farklı ürün tiplerinin farklı %0(301 kdv ihracat istisnası), %1, %8, %18 KDV oranları olsun
Sipariş özeti çıkarın (toplam tutar, KDV, indirim sonrası)
"""

from typing import List, Dict, Optional


class Urun:
    def __init__(self, sku: str, isim: str, fiyat: float, stok: int = 0, ihracat: bool = False, kdv_orani: Optional[float] = None):
        self.sku = sku
        self.isim = isim
        try:
            self.fiyat = float(fiyat)
        except Exception:
            raise ValueError('Fiyat sayısal olmalıdır')
        self.stok = int(stok)
        # ihracat ise KDV %0 olur
        self.ihracat = bool(ihracat)
        # opsiyonel ürün bazlı KDV oranı (ondalık, ör: 0.01 -> %1)
        self._kdv_orani: Optional[float] = None if kdv_orani is None else float(kdv_orani)

    def get_kdv(self) -> float:
        """Varsayılan KDV oranı (örn. %8) - alt sınıflar override edilecek.
        Döndürülen değer ondalık oran (ör: 0.08)
        - Öncelik sırası: ihracat (%0) > ürün bazlı `_kdv_orani` > sınıf varsayılanı
        """
        if self.ihracat:
            return 0.0
        if self._kdv_orani is not None:
            return float(self._kdv_orani)
        return 0.08

    def get_kdv_aciklama(self) -> str:
        """KDV açıklaması döndürür. %0 ise 301 e-ihracat istisnası olarak etiketlenir."""
        if self.get_kdv() == 0.0:
            return '301 e-ihracat istisnası'
        return ''

    def __repr__(self) -> str:
        return f'<Urun {self.sku} {self.isim} {self.fiyat:.2f}>'


class Elektronik(Urun):
    def __init__(self, sku: str, isim: str, fiyat: float, stok: int = 0, garanti_yil: int = 1, ihracat: bool = False, kdv_orani: Optional[float] = None):
        super().__init__(sku, isim, fiyat, stok, ihracat=ihracat, kdv_orani=kdv_orani)
        self.garanti_yil = int(garanti_yil)

    def get_kdv(self) -> float:
        if self.ihracat:
            return 0.0
        if self._kdv_orani is not None:
            return float(self._kdv_orani)
        # Elektronik için varsayılan KDV %20
        return 0.20


class Giyim(Urun):
    def __init__(self, sku: str, isim: str, fiyat: float, stok: int = 0, beden: Optional[str] = None, renk: Optional[str] = None, ihracat: bool = False, kdv_orani: Optional[float] = None):
        super().__init__(sku, isim, fiyat, stok, ihracat=ihracat, kdv_orani=kdv_orani)
        self.beden = beden
        self.renk = renk

    def get_kdv(self) -> float:
        if self.ihracat:
            return 0.0
        if self._kdv_orani is not None:
            return float(self._kdv_orani)
        # Giyim için varsayılan KDV %8
        return 0.08


class Musteri:
    def __init__(self, ad: str, email: str, indirim: float = 0.0):
        self.ad = ad
        self.email = email
        self._indirim = 0.0
        self.indirim = indirim

    @property
    def indirim(self) -> float:
        """İndirim yüzdesi (0-50) olarak döner."""
        return self._indirim

    @indirim.setter
    def indirim(self, value: float) -> None:
        try:
            v = float(value)
        except Exception:
            raise ValueError('İndirim sayısal olmalıdır')
        if v < 0 or v > 50:
            raise ValueError('İndirim %0 ile %50 arasında olmalıdır')
        self._indirim = v

    def indirim_orani(self) -> float:
        """Ondalık indirim oranı döndürür (ör: %10 -> 0.10)"""
        return self._indirim / 100.0

    def __repr__(self) -> str:
        return f'<Musteri {self.ad} ({self.email}) Indirim: {self._indirim}%>'


class Sepet:
    def __init__(self):
        # items: list of dict {urun, miktar}
        self.items: List[Dict] = []

    def add_urun(self, urun: Urun, miktar: int = 1) -> None:
        if miktar <= 0:
            raise ValueError('Miktar pozitif olmalıdır')
        # stok kontrol opsiyonel; sadece ekleme
        for it in self.items:
            if it['urun'].sku == urun.sku:
                it['miktar'] += int(miktar)
                return
        self.items.append({'urun': urun, 'miktar': int(miktar)})

    def remove_urun(self, sku: str) -> None:
        self.items = [it for it in self.items if it['urun'].sku != sku]

    def update_miktar(self, sku: str, miktar: int) -> None:
        if miktar < 0:
            raise ValueError('Miktar negatif olamaz')
        for it in self.items:
            if it['urun'].sku == sku:
                if miktar == 0:
                    self.remove_urun(sku)
                else:
                    it['miktar'] = int(miktar)
                return
        raise KeyError('Ürün sepette bulunamadı')

    def temizle(self) -> None:
        self.items.clear()

    def siparis_ozeti(self, musteri: Musteri) -> Dict:
        """Sipariş özeti hesaplar ve sözlük halinde döndürür.

        Döndürülen ana anahtarlar:
        - subtotal: ürünlerin toplamı (indirim öncesi)
        - toplam_indirim: uygulanan indirim tutarı
        - toplam_kdv: uygulanan KDV toplamı
        - toplam: ödenecek toplam (indirim sonrası + KDV)
        - detaylar: ürün bazlı döküm
        """
        subtotal = 0.0
        toplam_indirim = 0.0
        toplam_kdv = 0.0
        detay = []
        indirim_orani = musteri.indirim_orani()

        for it in self.items:
            urun = it['urun']
            miktar = int(it['miktar'])
            tutar = urun.fiyat * miktar
            subtotal += tutar
            # ürün bazlı indirim
            urun_indirim = tutar * indirim_orani
            toplam_indirim += urun_indirim
            vergi_taban = tutar - urun_indirim
            kdv = vergi_taban * urun.get_kdv()
            toplam_kdv += kdv
            detay.append({
                'sku': urun.sku,
                'isim': urun.isim,
                'adet': miktar,
                'birim_fiyat': urun.fiyat,
                'tutar': tutar,
                'urun_indirim': urun_indirim,
                'kdv_orani': urun.get_kdv(),
                'kdv_tutar': kdv,
                'kdv_aciklama': urun.get_kdv_aciklama(),
            })

        toplam_odenecek = (subtotal - toplam_indirim) + toplam_kdv

        return {
            'subtotal': round(subtotal, 2),
            'toplam_indirim': round(toplam_indirim, 2),
            'toplam_kdv': round(toplam_kdv, 2),
            'toplam': round(toplam_odenecek, 2),
            'detaylar': detay,
        }

    def __repr__(self) -> str:
        return f'<Sepet {len(self.items)} item(s)>'


def demo():
    # Ürün örnekleri
    tel = Elektronik('E001', 'Akıllı Telefon', 8000.0, stok=10, garanti_yil=2)
    kulaklik = Elektronik('E002', 'Kablosuz Kulaklık', 600.0, stok=25, garanti_yil=1, ihracat=True)
    tshirt = Giyim('G001', 'T-Shirt', 150.0, stok=50, beden='M', renk='Siyah')
    # Ürün bazlı özel KDV örnekleri: %1 ve %0
    kitap = Urun('K001', 'Kitap', 120.0, stok=30, kdv_orani=0.01)  # %1 KDV
    gida = Urun('F001', 'Temel Gıda', 50.0, stok=100, kdv_orani=0.0)  # %0 KDV (istisna)

    # Müşteri (indirim %10)
    m = Musteri('Elif Kaya', 'elif@example.com', indirim=10)

    s = Sepet()
    s.add_urun(tel, 1)
    s.add_urun(kulaklik, 2)
    s.add_urun(tshirt, 3)
    s.add_urun(kitap, 2)
    s.add_urun(gida, 5)

    ozet = s.siparis_ozeti(m)

    print('--- Sipariş Özeti ---')
    print(f"Ara Toplam: {ozet['subtotal']:.2f} TL")
    print(f"Toplam İndirim: {ozet['toplam_indirim']:.2f} TL")
    print(f"Toplam KDV: {ozet['toplam_kdv']:.2f} TL")
    print(f"Ödenecek Toplam: {ozet['toplam']:.2f} TL")
    print('\nÜrün Detayları:')
    for d in ozet['detaylar']:
        print(f"- {d['isim']} (x{d['adet']}): {d['tutar']:.2f} TL | Indirim: {d['urun_indirim']:.2f} TL | KDV ({int(d['kdv_orani']*100)}%): {d['kdv_tutar']:.2f} TL")


if __name__ == '__main__':
    demo()
