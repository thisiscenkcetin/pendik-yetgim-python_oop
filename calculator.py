#!/usr/bin/env python3

import argparse
import sys


def to_number(s):
    try:
        return int(s)
    except Exception:
        try:
            return float(s)
        except Exception:
            raise argparse.ArgumentTypeError(f"Invalid number: {s}")


def main():
    parser = argparse.ArgumentParser(description='Hesap makinesi: + - * / işlemleri (iki sayı).')
    parser.add_argument('a', nargs='?', type=to_number, help='Birinci sayı')
    parser.add_argument('b', nargs='?', type=to_number, help='İkinci sayı')
    args = parser.parse_args()

    if args.a is None or args.b is None:
        try:
            a = to_number(input("Birinci sayıyı girin: ").strip())
            b = to_number(input("İkinci sayıyı girin: ").strip())
        except (EOFError, KeyboardInterrupt):
            print('\nGiriş iptal edildi.')
            sys.exit(1)
        except Exception as e:
            print('Hatalı giriş:', e)
            sys.exit(1)
    else:
        a = args.a
        b = args.b

    print('Toplama:', a + b)
    print('Çıkarma:', a - b)
    print('Çarpma:', a * b)
    if b == 0:
        print('Bölme: Hata (sıfıra bölünemez)')
    else:
        print('Bölme:', a / b)


if __name__ == '__main__':
    main()
