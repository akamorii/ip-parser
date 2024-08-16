import os
from path import path

os.chdir(path)

try:
    with open('log.txt', 'r', encoding='utf-8') as file:
        f = file.read()
        print()
except Exception as ex:
    print(ex)