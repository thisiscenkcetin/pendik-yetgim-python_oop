"""
[1,2,2,3,4,4,5] bu listedeki tekrar eden elemanları çıkarın
"""

from typing import List, Iterable, TypeVar

T = TypeVar('T')


def remove_duplicates_preserve_order(seq: Iterable[T]) -> List[T]:

    seen = set()
    result: List[T] = []
    for item in seq:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def main() -> None:
    lst = [1, 2, 2, 3, 4, 4, 5]
    unique = remove_duplicates_preserve_order(lst)
    print('Orijinal liste:', lst)
    print('Tekrarsız liste:', unique)


if __name__ == '__main__':
    main()
