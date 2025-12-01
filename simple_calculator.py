#!/usr/bin/env python3
"""
Basit İnteraktif Hesap Makinesi

Kullanım:
- Program iki sayı alır (ondalıklı veya tam sayı kabul edilir)
- Kullanıcıdan yapılacak işlem istenir: + - * / ** %
- Geçersiz girişlerde tekrar istenir
- Bölme için bölen 0 ise uyarı verir
"""

def read_number(prompt):
    while True:
        s = input(prompt).strip()
        try:
            if s == "":
                raise ValueError
            # Önce int dene, değilse float
            try:
                return int(s)
            except ValueError:
                return float(s)
        except ValueError:
            print("Geçersiz sayı. Lütfen tekrar deneyin.")


def read_operation(prompt):
    valid = ['+', '-', '*', '/', '**', '%']
    while True:
        op = input(prompt).strip()
        if op in valid:
            return op
        print(f"Geçersiz işlem. Geçerli işlemler: {', '.join(valid)}")


def calculate(a, b, op):
    try:
        if op == '+':
            return a + b
        if op == '-':
            return a - b
        if op == '*':
            return a * b
        if op == '/':
            if b == 0:
                return 'Error: Bölme by zero'
            return a / b
        if op == '**':
            return a ** b
        if op == '%':
            if b == 0:
                return 'Error: Mod by zero'
            return a % b
    except Exception as e:
        return f'Error: {e}'


def main():
    print('Basit Hesap Makinesi')
    a = read_number('s1 = kullanıcından al: ')
    b = read_number('s2 = kullanıcından al: ')
    op = read_operation('islem (+ - * / ** %): ')

    result = calculate(a, b, op)

    print('\nSonuç:')
    print(f"{a} {op} {b} = {result}")


if __name__ == '__main__':
    main()
