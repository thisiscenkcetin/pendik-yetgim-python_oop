"""
Fibonacci Serisi (<= N)

Kullanıcıdan pozitif bir tam sayı N alınır ve N'e kadar (<= N) olan
Fibonacci sayıları ekrana yazdırılır.
"""

def read_nonnegative_int(prompt: str) -> int:
    while True:
        s = input(prompt).strip()
        try:
            v = int(s)
            if v < 0:
                print('Lütfen negatif olmayan bir tam sayı girin.')
                continue
            return v
        except ValueError:
            print('Geçersiz giriş. Lütfen bir tam sayı girin.')


def fibonacci_upto(n: int):
    """Return list of Fibonacci numbers <= n."""
    if n < 0:
        return []
    seq = []
    a, b = 0, 1
    while a <= n:
        seq.append(a)
        a, b = b, a + b
    return seq


def main():
    print('Fibonacci Serisi (<= N)')
    n = read_nonnegative_int('Pozitif bir tam sayı girin (N): ')
    seq = fibonacci_upto(n)
    if not seq:
        print('N için Fibonacci bulunamadı.')
    else:
        print(f'N = {n} için Fibonacci sayıları:')
        print(', '.join(str(x) for x in seq))


if __name__ == '__main__':
    main()
