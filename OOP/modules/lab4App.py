from modules.lab4Modules import Lab4Core


# Основной класс
class Lab4App():
    def __init__(self):
        while 1:
            # Инициализация вспомогательного модуля как поля основного класса
            self.Core = Lab4Core()
            print('Введите X:')
            # Получаем скользящую кривую
            self.Result = self.Core.Calculate(input())
            print('Скользящая кривая: ')
            print(self.Result)
            # Строим график
            self.Core.BuildGraphic()
            print('\nДля продолжения введите 1 \nДля выхода введите 2')
            p = input()
            if p == '2':
                break;
