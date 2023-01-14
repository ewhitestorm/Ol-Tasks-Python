# Solving tasks to competitive programming from the site https://acmp.ru
# https://acmp.ru/index.asp?main=task&id_task=11
# Author of solutions: Eugene Storm
# 
# Task №11
# ID 0011
# Completion time - 0,046 sec.


list_elem = [int(i) for i in list(''.join(input()).split(' ')) if i != '']

array = [1] + [0] * (list_elem[1] - 1)

for i in range(0, list_elem[0] - 1):
    array[i+1] = array[i] * 2

for i in range(list_elem[0] - 1, list_elem[1] - 1):
    elem = i - list_elem[0]
    if elem < 0:
        elem = i + 1 - list_elem[0]

    array[i+1] = (array[i] * 2) - array[elem]

print(array[-1])
