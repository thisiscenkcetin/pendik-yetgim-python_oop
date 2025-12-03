"""
Güvenli Şifre Oluşturucu
"""
import secrets
import string


def generate_password(length=12, use_upper=True, use_digits=True, use_punct=True):
    if length < 4:
        raise ValueError('Şifre uzunluğu en az 4 olmalıdır')
    alphabet = list(string.ascii_lowercase)
    if use_upper:
        alphabet += list(string.ascii_uppercase)
    if use_digits:
        alphabet += list(string.digits)
    if use_punct:
        alphabet += list('!@#$%^&*()-_=+[]{};:,.<>?')
    # Ensure at least one of each selected type
    while True:
        pwd = ''.join(secrets.choice(alphabet) for _ in range(length))
        # basic checks
        if use_upper and not any(c.isupper() for c in pwd):
            continue
        if use_digits and not any(c.isdigit() for c in pwd):
            continue
        if use_punct and not any(c in '!@#$%^&*()-_=+[]{};:,.<>?' for c in pwd):
            continue
        return pwd


if __name__ == '__main__':
    print('Şifre Oluşturucu')
    try:
        l = int(input('Uzunluk (ör. 12): ').strip())
    except Exception:
        l = 12
    pwd = generate_password(length=l)
    print('Oluşan şifre:', pwd)
