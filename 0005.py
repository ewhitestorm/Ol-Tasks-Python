# Solving tasks to competitive programming from the site https://acmp.ru
# https://acmp.ru/index.asp?main=task&id_task=5
# Author of solutions: Eugene Storm
# 
# Task №5
# ID 0005

n = int(input())
d = int(0)
list_first = []
list_second = []
main = []

for i in list(''.join(input()).split(' ')):
    if i != '':
       main.append(i)

for e in main:
    if int(e)%2 == 0:
        d += 1
    else:
        list_first.append(e)
        
for e in main:
    if int(e)%2 == 0:
        list_second.append(e)

print(' '.join(list_first))
print(' '.join(list_second))

if d >= (n-d):
    print("YES")
else:
    print("NO")

