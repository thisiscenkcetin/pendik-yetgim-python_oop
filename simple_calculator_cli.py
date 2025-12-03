"""
Basit Komut Satırı Hesap Makinesi
- Kullanıcıdan iki sayı alır (tam veya ondalık kabul eder)
- İşlem seçilir: +, -, *, /
- Bölme sıfıra karşı korunur
- İstendiğinde tekrar işlem yapılabilir veya çıkılabilir
"""

def read_number(prompt):
    while True:
        s = input(prompt).strip()
        # Kullanıcı çıkmak isterse
        if s.lower() in ('q', 'exit'):
            raise KeyboardInterrupt()
        try:
            if '.' in s:
                return float(s)
            return int(s)
        except ValueError:
            print("Geçersiz sayı. Lütfen tam sayı veya ondalık sayı girin (çıkmak için 'q').")


def user_input():
    num1 = read_number("Sayı1: ")
    num2 = read_number("Sayı2: ")
    return num1, num2


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def division(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("0'a bölme hatası")
    return num1 / num2


def calculator():
    print("Basit Hesap Makinesi (çıkmak için işlem sırasında 'q' ya da 'exit' yazabilirsiniz)")
    try:
        while True:
            try:
                a, b = user_input()
            except KeyboardInterrupt:
                print("\nKullanıcı çıkış yaptı.")
                break

            option = input("Lütfen yapmak istediğiniz işlemi (+, -, *, /): ").strip()
            if option == "+":
                result = add(a, b)
            elif option == "-":
                result = sub(a, b)
            elif option == "*":
                result = multiply(a, b)
            elif option == "/":
                try:
                    result = division(a, b)
                except ZeroDivisionError as e:
                    print(e)
                    continue
            else:
                print("Lütfen geçerli bir işlem seçiniz (+, -, *, /).")
                continue

            print(f"Sonuç: {result}")

            again = input("Yeni işlem yapmak ister misiniz? (e/h): ").strip().lower()
            if again not in ('e', 'evet', 'y', 'yes'):
                print('Çıkılıyor.')
                break
    except KeyboardInterrupt:
        print('\nProgram kullanıcı tarafından kesildi.')


if __name__ == '__main__':
    calculator()
