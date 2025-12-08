"""
Kullanıcıdan alınan cümlenin kaç kelimeden oluştuğunu ekrana bastırın
"""

from typing import Any


def kelime_say(cumle: str) -> int:
    """Verilen cümledeki kelime sayısını döndürür

    - Giriş None veya boşsa 0 döner
    - Kelimeler aralarındaki boşluk karakterlerine göre ayrılır
    """
    if cumle is None:
        return 0
    s = str(cumle).strip()
    if not s:
        return 0
    return len(s.split())


def main() -> None:
    try:
        cumle = input('Cümleyi girin: ')
    except EOFError:
        
        print('Giriş alınamadı.')
        return
    adet = kelime_say(cumle)
    print(f'Kelime sayısı: {adet}')


if __name__ == '__main__':
    main()
