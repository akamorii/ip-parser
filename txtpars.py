import os
from path import path
from find_ip import findip_in_string

def parse_log(file_name='log.txt'):
    os.chdir(path)
    ip_arr = []
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    # print(findip_in_string(line))
                    ip_arr.append(findip_in_string(line))
                except Exception as exep:
                    print(exep)
                    continue
    except Exception as ex:
        print(ex)
        
    print(ip_arr)
    
parse_log()