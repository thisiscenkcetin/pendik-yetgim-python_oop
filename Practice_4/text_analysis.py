"""
Metin Analizi
"""
from collections import Counter
import re


def word_count(text: str) -> int:
    words = re.findall(r"\w+", text)
    return len(words)


def char_count(text: str) -> int:
    return len(text)


def most_common_words(text: str, n=5):
    words = re.findall(r"\w+", text.lower())
    c = Counter(words)
    return c.most_common(n)


def average_word_length(text: str) -> float:
    words = re.findall(r"\w+", text)
    if not words:
        return 0.0
    return sum(len(w) for w in words) / len(words)


if __name__ == '__main__':
    sample = input('Analiz edilecek metni girin: ')[:10000]
    print('Kelime sayısı:', word_count(sample))
    print('Karakter sayısı:', char_count(sample))
    print('Ortalama kelime uzunluğu:', average_word_length(sample))
    print('En sık kelimeler:', most_common_words(sample, 10))
