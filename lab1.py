from os import system
from sys import exit


def znak(a1, b1, z1):
    if z1 == '+':
        a1 += b1
        return a1
    elif z1 == '-':
        a1 -= b1

    elif z1 == '/':
        a1 /= b1

    elif z == '*':
        a1 *= b1

    elif z == '^':
        a1 **= b1
    assert isinstance(a1, object)
    return a1


while 1:
    a = int(input())
    b = int(input())
    z = input()
    a = znak(a, b, z)
    print (' = ', a)
    while 1:
        print('\nДля продолжения введите 1, затем введите операнд и действие\nДля выхода введите 2\nЧтобы начать заного, введите 3')
        p = input()
        if p == '2':
            exit()
        elif p == '3':
            system('cls')
            break
        system('cls')
        print(a)
        b = int(input())
        z = input()
        a = znak(a, b, z)
        print(a)