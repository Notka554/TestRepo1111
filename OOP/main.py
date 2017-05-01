from os import system
from sys import exit
import sys

# Подгружаем модули с задачами
from modules.lab1App import Lab1App
from modules.lab2App import Lab2App
from modules.lab3App import Lab3App
from modules.lab4App import Lab4App
from modules.lab5App import Lab5App

while 1:
    print('\nВыберите лабораторную работу (1,2,3,4,5):')
    index = int(input())
    if(index==1):
        Lab1App()
    if(index==2):
        Lab2App()
    if (index == 3):
        # Эмуляция --poly
        sys.argv = ["--poly=1,2,3,4,53"]
        Lab3App()
    if(index==4):
        Lab4App()
    if(index==5):
        Lab5App()
