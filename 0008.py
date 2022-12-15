# Solving tasks to competitive programming from the site https://acmp.ru
# https://acmp.ru/index.asp?main=task&id_task=8
# Author of solutions: Eugene Storm
# 
# Task №8
# ID 0008
# Completion time - 0,031 sec.


main = [int(elem) for elem in list(''.join(input()).split(' '))]

if main[0] * main[1] == main[2]:
    print('YES')
else:
    print('NO')
