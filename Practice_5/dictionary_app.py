"""
Türkçe-İngilizce Sözlük Uygulaması
- basit: {turkish: english}
"""
from typing import Dict

dict_en: Dict[str, str] = {}


def add_word(tr: str, en: str):
    dict_en[tr.lower()] = en


def translate(tr: str) -> str:
    return dict_en.get(tr.lower(), None)


def remove_word(tr: str):
    return dict_en.pop(tr.lower(), None)


def list_words():
    return dict_en.items()


if __name__ == '__main__':
    print('Sözlük demo: örnek kelimeler ekleniyor')
    add_word('kitap','book')
    add_word('kalem','pen')
    print('Çeviri "kitap" =>', translate('kitap'))
    print('Tüm kelimeler:', list(list_words()))
