from modules.lab2Modules import Lab2Core


# Основной класс
class Lab2App():
    def __init__(self):
        while 1:
            # Инициализация вспомогательного модуля как поля основного класса
            self.Core = Lab2Core()
            print('\nВведите число:')
            self.Input = input()
            self.Output = self.Core.Sqrt(float(self.Input))
            print(round(self.Output, 5))
            print('\nДля продолжения введите 1 \nДля выхода введите 2')
            p = input()
            if p == '2':
                break;
