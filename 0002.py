# Solving tasks to competitive programming from the site https://acmp.ru
# https://acmp.ru/index.asp?main=task&id_task=2
# Author of solutions: Eugene Storm
# 
# Task №2
# ID 0002

n = int(input())
s = 0
if n>0 and n!=0:
    for i in range(1,n+1):
        s += i
else:
    m = n*-1
    s = int(((1+n-3)*(m-1))/2)
print(s)
