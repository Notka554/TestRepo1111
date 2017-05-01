from modules.lab1Modules import Lab1Core


# Основной класс
class Lab1App():
    def __init__(self):
        while 1:
            # Инициализация вспомогательного модуля как поля основного класса
            self.Core = Lab1Core()
            print('\nВведите два числа и знак:')
            self.a = int(input())
            self.b = int(input())
            self.z = input()
            self.a = self.Core.Calculate(self.a, self.b, self.z)
            print(' = ', self.a)
            print('\nДля продолжения введите 1 \nДля выхода введите 2')
            p = input()
            if p == '2':
                break;
