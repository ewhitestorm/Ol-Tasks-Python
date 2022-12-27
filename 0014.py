# Solving tasks to competitive programming from the site https://acmp.ru
# https://acmp.ru/index.asp?main=task&id_task=14
# Author of solutions: Eugene Storm
# 
# Task №14
# ID 0014
# Completion time - 0,031 sec.


main = [int(i) for i in list(''.join(input()).split(' ')) if i != '']
a = main[0]
b = main[1]

c = a * b

while b:
  nod = a%b
  a = b
  b = nod
  
nok = c / a

print(int(nok))
