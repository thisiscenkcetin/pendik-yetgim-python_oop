"""
Dönüştürücü Paket
- Sıcaklık: C <-> F
- Uzunluk: metre <-> feet, km <-> mil
- Ağırlık: kg <-> pound
"""

def c_to_f(c):
    return c * 9/5 + 32


def f_to_c(f):
    return (f - 32) * 5/9


def metre_to_feet(m):
    return m * 3.28084


def feet_to_metre(ft):
    return ft / 3.28084


def km_to_miles(km):
    return km * 0.621371


def miles_to_km(mi):
    return mi / 0.621371


def kg_to_lb(kg):
    return kg * 2.20462


def lb_to_kg(lb):
    return lb / 2.20462


if __name__ == '__main__':
    print('Dönüştürücü örnek: C->F 0C =', c_to_f(0))
