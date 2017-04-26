# -*- coding: utf-8 -*-


import urllib.request
import matplotlib.pyplot

otpravitely = []

ikk = []


def name(z, spom):
    n = otpravitely[z]
    flag = False
    n.Kmail += + 1
    n.spa.append(spom)


class Otpravitel:
    def __init__(self, n):
        self.name = n
        self.Kmail = 0
        self.spa = []
        self.srspam = None


s = urllib.request.urlopen('http://www.pythonlearn.com/code3/mbox.txt')
f = str(s.read())
pos = 0
R = 'Author: '
LR = len(R)
Spam = 'X-DSPAM-Confidence: '
Lspam = len(Spam)
sPm = 0
Name = ''
SR_Spam = 0

'''сбор данных'''
while f.find(Spam, pos) != -1:
    count = 0
    pos = f.find(Spam, pos) + Lspam
    sPm = float(f[pos:(pos + 6)])
    pos = f.find(R, pos) + LR
    for i in range(1000):
        if (f[(pos + i + 3):pos + i + 3 + 4]) == 'Date':
            Name = f[pos:(pos + i + 1)]
            break
    otp = otpravitely
    flag = False
    for x in otpravitely:
        if x.name == Name:
            flag = True
            break
        count += 1
    if not flag:
        otp.append(Otpravitel(Name))
    otpravitely = otp
    name(count - 1, sPm)
'''среднее SPAM'''
count = 0
for i in otpravitely:
    for j in i.spa:
        count += 1
        SR_Spam += j
SR_Spam /= count

otpravitely.pop()
'''кого заблокировать за спам'''

for i in otpravitely:
    sm = 0
    sk = len(i.spa)
    for j in i.spa:
        sm = sm + j
    i.srspam = sm / sk
maxx = 0
count = 0
for i in otpravitely:
    if i.srspam > otpravitely[maxx].srspam:
        maxx = count
    count += 1

print('Среднее значение X-DSPAM-Confidence = ' + str(SR_Spam))
print('Стоит заблокировать - ' + otpravitely[maxx].name)

'''гистограмма'''

X = []
for i in otpravitely:
    X.append(i.Kmail)
Y = range(len(X))
matplotlib.pyplot.bar(Y, X, align='center')
matplotlib.pyplot.xticks(Y)
matplotlib.pyplot.show()
