# Solving tasks to competitive programming from the site https://acmp.ru
# https://acmp.ru/index.asp?main=task&id_task=7
# Author of solutions: Eugene Storm
# 
# Task №7
# ID 0007
# Version - 1
# Completion time - 0,046 sec.




main = []

for elem in list(''.join(input()).split(' ')):
    if elem != '':
        main.append(int(elem))

print(max(main))
