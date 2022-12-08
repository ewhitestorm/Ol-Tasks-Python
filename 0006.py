# Solving tasks to competitive programming from the site https://acmp.ru
# https://acmp.ru/index.asp?main=task&id_task=6
# Author of solutions: Eugene Storm
# 
# Task №6
# ID 0006

import string

n = input()
if (len(n) != 5 or n[2] != '-' or
    n[0] < 'A' or n[0] > 'H' or
    n[1] < '1' or n[1] > '8' or
    n[3] < 'A' or n[3] > 'H' or
    n[4] < '1' or n[4] > '8'):
    print('ERROR')
else:
    if(abs((string.ascii_uppercase.index(n[0]) - string.ascii_uppercase.index(n[3])) * (int(n[1]) - int(n[4]))) == 2):
        print('YES')
    else:
        print('NO')
