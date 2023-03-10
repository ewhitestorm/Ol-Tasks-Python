# Solving tasks to competitive programming from the site https://acmp.ru/index.asp?main=task&id_task=13
# Author of solutions: Eugene Storm
# 
# Task №13
# ID 0013
# Completion time - 0,031 sec.


list_in = [i for i in list(''.join(input()).split(' ')) if i != '']
t = b = k = 0
for elem in list_in:
    for t in range(len(elem)):
        if list_in[0][t] == list_in[1][t]:
            b += 1
        elif list_in[0][t] in list_in[1]:
            k += 1
    break
print("{} {}".format(b, k))
