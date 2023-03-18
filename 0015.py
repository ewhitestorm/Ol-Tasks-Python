# Solving tasks to competitive programming from the site https://acmp.ru
# https://acmp.ru/index.asp?main=task&id_task=15
# Author of solutions: Eugene Storm
# 
# Task №15
# ID 0015
# Completion time - 0,031 sec.


N = int(input())
p = 0

for n in range(N):
    list_el = [i for i in list(''.join(input()).split()) if i != '']
    p += list_el.count('1')
print(p//2)
