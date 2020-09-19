import subprocess as sbp
import pip
from sys import exit
from colorama import Fore, init
init()
print(Fore.CYAN + '--------------------------------------' + Fore.WHITE)
print(Fore.GREEN + '[!]' +Fore.WHITE +' Получение пакетов, которые можно обновить...')
string = str(sbp.run("pip3 list -o --format=json", shell=True, stdout=sbp.PIPE).stdout, encoding='utf-8')
if "[]" in str(string):
    print(Fore.GREEN + '[!]' +Fore.WHITE +' Все пакеты обновлённые =)')
    print(Fore.CYAN + '--------------------------------------' + Fore.WHITE)
    exit()

pkgs = eval(string)

print(Fore.GREEN + '[!]' +Fore.WHITE +' Пакеты получены =)')
print(Fore.GREEN + '[!]' +Fore.WHITE +' Установка пакетов')
for pkg in pkgs:
    sbp.run("pip3 install --upgrade " + pkg['name'], shell=True)
print(Fore.GREEN + '[!]' +Fore.WHITE +' Пакеты обновлены!')
print(Fore.RED + '--[==  With love, Temnij  ==]--' + Fore.WHITE)
print(Fore.CYAN + '--------------------------------------' + Fore.WHITE)