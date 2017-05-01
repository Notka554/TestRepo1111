from modules.lab3Modules import Lab3Core


# Основной класс
class Lab3App():
    def __init__(self):
        while 1:
            # Инициализация вспомогательного модуля как поля основного класса
            self.Core = Lab3Core()
            self.Result = self.Core.Calculate()
            print('Для прогрессии ')
            print(self.Core.Poly)
            print('полином будет равен ')
            print(self.Result)
            print('\nДля продолжения введите 1 \nДля выхода введите 2')
            p = input()
            if p == '2':
                break;
