from modules.lab5Modules import Lab5Core


# Основной класс
class Lab5App():
    def __init__(self):
        while 1:
            # Инициализация вспомогательного модуля как поля основного класса
            self.Core = Lab5Core()
            print('Обрабатываем информацию с сервера...')
            self.Core.DataBind()
            self.Core.SpamCheck()
            print('Среднее значение X-DSPAM-Confidence = ' + str(self.Core.SR_Spam))
            print('Стоит заблокировать - ' + self.Core.BanUser.name)
            self.Core.BuildGraph()
            print('\nДля продолжения введите 1 \nДля выхода введите 2')
            p = input()
            if p == '2':
                break;
