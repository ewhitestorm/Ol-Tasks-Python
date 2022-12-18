# Solving tasks to competitive programming from the site https://acmp.ru
# https://acmp.ru/index.asp?main=task&id_task=10
# Author of solutions: Eugene Storm
# 
# Task №10
# ID 0010
# Completion time - 0,031 sec.


main = [int(i) for i in list(''.join(input()).split(' ')) if i != '']

list_num = [str(x) for x in range(-100, 101) if main[0]*x**3 + main[1]*x**2 + main[2]*x + main[3] == 0]

print(' '.join(list_num))
