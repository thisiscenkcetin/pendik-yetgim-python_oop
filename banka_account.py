"""
Bir banka hesap sistemi oluşturun. Hesap bakiyesi private olacak ve @property dekoratörü ile erişilecek.İstenenler:

BankaHesabi sınıfı oluşturun (hesap_no, sahibi, __bakiye)
@property dekoratörü ile bakiye getter ve setter tanımlayın
Setter'da bakiye negatif olamaz kontrolü yapın
para_yatir() ve para_cek() metotları ekleyin
İşlem geçmişini tutan bir liste ekleyin
"""

from datetime import datetime
from typing import List, Dict


class BankaHesabi:
    def __init__(self, hesap_no: str, sahibi: str, bakiye: float = 0.0):
        self.hesap_no = hesap_no
        self.sahibi = sahibi
        # private bakiye
        self.__bakiye = 0.0
        self.islemler: List[Dict] = []
        # kullanıcının verdiği başlangıç bakiyesini setter üzerinden ayarla (doğrulama için)
        self.bakiye = bakiye

    @property
    def bakiye(self) -> float:
        """Hesabın bakiyesini döndürür."""
        return self.__bakiye

    @bakiye.setter
    def bakiye(self, value: float) -> None:
        """Bakiye negatif olamaz; negatif atama girişiminde ValueError atılır."""
        try:
            v = float(value)
        except Exception:
            raise ValueError('Bakiye sayısal olmalıdır')
        if v < 0:
            raise ValueError('Bakiye negatif olamaz')
        # bakiye değişimini işlem geçmişine kaydet
        old = getattr(self, '_BankaHesabi__bakiye', None)
        self.__bakiye = v
        # başlangıç atamasında eski bakiye None olabilir; kayıt için yine de tarih kaydı ekleyelim
        self.islemler.append({
            'tarih': datetime.now().isoformat(),
            'tur': 'bakiye_atama',
            'miktar': v,
            'bakiye': self.__bakiye,
            'eski_bakiye': old,
        })

    def para_yatir(self, amount: float) -> None:
        """Hesaba pozitif miktar yatırır ve işlemi kaydeder."""
        try:
            amt = float(amount)
        except Exception:
            raise ValueError('Yatırılacak miktar sayısal olmalıdır')
        if amt <= 0:
            raise ValueError('Yatırılacak miktar pozitif olmalıdır')
        self.__bakiye += amt
        self.islemler.append({
            'tarih': datetime.now().isoformat(),
            'tur': 'yatirma',
            'miktar': amt,
            'bakiye': self.__bakiye,
        })

    def para_cek(self, amount: float) -> None:
        """Hesaptan miktar çeker; bakiye yetersizse ValueError atar; işlemi kaydeder."""
        try:
            amt = float(amount)
        except Exception:
            raise ValueError('Çekilecek miktar sayısal olmalıdır')
        if amt <= 0:
            raise ValueError('Çekilecek miktar pozitif olmalıdır')
        if amt > self.__bakiye:
            raise ValueError('Yetersiz bakiye')
        self.__bakiye -= amt
        self.islemler.append({
            'tarih': datetime.now().isoformat(),
            'tur': 'cekme',
            'miktar': amt,
            'bakiye': self.__bakiye,
        })

    def get_islem_gecmisi(self) -> List[Dict]:
        """İşlem geçmişini kronolojik liste olarak döndürür."""
        return list(self.islemler)

    def __str__(self) -> str:
        return f'Hesap {self.hesap_no} - Sahibi: {self.sahibi} - Bakiye: {self.bakiye:.2f} TL'


def demo():
    print('BankaHesabi demo')
    h = BankaHesabi('TR123', 'Ayşe Yılmaz', bakiye=500.0)
    print(h)
    h.para_yatir(250)
    print('250 TL yatırıldı ->', h)
    try:
        h.para_cek(900)
    except Exception as e:
        print('Çekme hatası (beklenen):', e)
    h.para_cek(200)
    print('200 TL çekildi ->', h)
    print('\nİşlem geçmişi:')
    for i, islem in enumerate(h.get_islem_gecmisi(), start=1):
        print(i, islem)


if __name__ == '__main__':
    demo()
