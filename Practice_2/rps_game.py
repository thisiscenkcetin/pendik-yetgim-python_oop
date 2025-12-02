"""
Taş-Kağıt-Makas
- Kullanıcı ile bilgisayar arasında oynanır
- 'rock', 'paper', 'scissors' veya kısa 'r','p','s' kabul edilir
- En iyi-of-N (tek sayılı tur sayısı) oynanır
"""

import random

CHOICES = {'r':'rock','p':'paper','s':'scissors','rock':'rock','paper':'paper','scissors':'scissors'}


def read_choice(prompt):
    while True:
        s = input(prompt).strip().lower()
        if s in CHOICES:
            return CHOICES[s]
        print('Geçersiz seçim. r/p/s veya rock/paper/scissors girin.')


def outcome(p, c):
    if p == c:
        return 0
    wins = {('rock','scissors'), ('scissors','paper'), ('paper','rock')}
    return 1 if (p,c) in wins else -1


def main():
    print('Taş-Kağıt-Makas')
    try:
        rounds = int(input('Tur sayısı (tek sayı, örn. 3): ').strip())
    except Exception:
        print('Geçersiz sayı, varsayılan 3 tur seçildi.')
        rounds = 3
    if rounds <= 0:
        rounds = 3
    player_score = 0
    comp_score = 0
    needed = rounds//2 + 1

    for i in range(1, rounds+1):
        print(f'--- Tur {i} ---')
        p = read_choice('Seçiminiz (r/p/s): ')
        c = random.choice(['rock','paper','scissors'])
        print(f'Bilgisayar: {c}')
        res = outcome(p,c)
        if res == 0:
            print('Berabere')
        elif res == 1:
            print('Kazandınız')
            player_score += 1
        else:
            print('Kaybettiniz')
            comp_score += 1
        if player_score == needed or comp_score == needed:
            break

    print(f'Final: Siz {player_score} - Bilgisayar {comp_score}')
    if player_score > comp_score:
        print('Maçı kazandınız!')
    elif player_score < comp_score:
        print('Maçı kaybettiniz.')
    else:
        print('Berabere maç.')


if __name__ == '__main__':
    main()
