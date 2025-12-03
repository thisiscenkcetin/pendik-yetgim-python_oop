"""
Set ile Veri Temizleme
"""
from typing import List


def remove_duplicates(records: List) -> List:
    seen = set()
    out = []
    for r in records:
        if r not in seen:
            seen.add(r)
            out.append(r)
    return out


def normalize_and_dedupe(strings: List[str]) -> List[str]:
    seen = set()
    out = []
    for s in strings:
        norm = s.strip().lower()
        if norm not in seen:
            seen.add(norm)
            out.append(norm)
    return out


if __name__ == '__main__':
    data = ['A','b','a','B','c','a']
    print('Original:', data)
    print('Remove duplicates preserving order:', remove_duplicates(data))
    print('Normalize and dedupe:', normalize_and_dedupe([' Hello ','hello','WORLD','world']))
