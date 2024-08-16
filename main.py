import os

# os.system("cd python")
# print(os.getcwd())
# os.system("cd OS")
# print(os.environ['PATH']) 
os.chdir("C:/Users/ineve/OneDrive/Рабочий стол/just folder/proga res/python/OS")
# print(os.getcwd())
# out = os.popen(f"python hello.py").read()
res = os.popen('ipconfig').read().encode('cp1251').decode('cp866')
# res = res.encode('latin-1', errors='replace')
# res = res.decode('cp1251')

with open('log.txt', 'w', encoding='utf-8') as f:
    f.write(res)

print(type(res))