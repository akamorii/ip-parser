import random
import json

# from 0 to 255
def generation(count = 10):
    ip_dict = {}
    rang = (0, 255)
    ip_example = [[],['.'],[],['.'],[],['.'],[]] # 0 2 4 6
    for i in range(count):
        index = 0
        for j in range(4):
            ip_example[index] = random.randint(0,255)
            index += 2
            # x = [*ip_example]
            print(ip_example)
        ip_dict.update({f'ip {i}': ip_example})
        
    return ip_dict
# with open('ip_examples.json', 'w', encoding='utf-8') as exip:
    
print(generation())