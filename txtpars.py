import os

os.chdir("C:/Users/ineve/OneDrive/Рабочий стол/just folder/proga res/python/OS")

try:
    with open('log.txt', 'r', encoding='utf-8') as file:
        f = file.read()
        print()
except Exception as ex:
    print(ex)