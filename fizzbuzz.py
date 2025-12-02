"""
FizzBuzz 1..100
- 15'e tam bölünenler -> FizzBuzz
- 3'e tam bölünenler -> Fizz
- 5'e tam bölünenler -> Buzz
- Diğerleri -> sayı
"""

def fizzbuzz(n: int) -> str:
    if n % 15 == 0:
        return 'FizzBuzz'
    if n % 3 == 0:
        return 'Fizz'
    if n % 5 == 0:
        return 'Buzz'
    return str(n)


def main():
    for i in range(1, 101):
        print(fizzbuzz(i))


if __name__ == '__main__':
    main()
