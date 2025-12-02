"""
Vergi Hesaplayıcı
- Basit bir kademeli vergi hesabı uygular.
- Braketler (örnek):
  0 - 10.000 : %0
  10.001 - 30.000 : %10
  30.001 - 100.000 : %20
  100.001+ : %30
"""

def read_positive_float(prompt):
    while True:
        s = input(prompt).strip()
        try:
            v = float(s)
            if v < 0:
                raise ValueError
            return v
        except ValueError:
            print('Geçersiz giriş. Pozitif bir sayı girin.')


def calculate_tax(income):
    tax = 0.0
    # dilimlere göre hesap (kademeli)
    brackets = [ (10000, 0.00), (30000, 0.10), (100000, 0.20) ]
    remaining = income
    lower = 0
    for upper, rate in brackets:
        if income > lower:
            taxable = min(upper - lower, income - lower)
            tax += taxable * rate
        lower = upper
    if income > 100000:
        tax += (income - 100000) * 0.30
    return tax


def main():
    print('Vergi Hesaplayıcı (örnek kademeler ile)')
    income = read_positive_float('Yıllık gelirinizi girin: ')
    tax = calculate_tax(income)
    net = income - tax
    print(f'Brüt gelir: {income:.2f} TL')
    print(f'Ödenecek vergi: {tax:.2f} TL')
    print(f'Net gelir: {net:.2f} TL')


if __name__ == '__main__':
    main()
