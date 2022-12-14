# Solving tasks to competitive programming from the site https://acmp.ru
# https://acmp.ru/index.asp?main=task&id_task=9
# Author of solutions: Eugene Storm
# 
# Task №9
# ID 0009
# Completion time - 0,046 sec.


n = int(input())
N = 1

main = [int(i) for i in list(''.join(input()).split(' ')) if i != '']

num_min = main.index(min(main))
num_max = main.index(max(main))

if num_min < num_max:
    for num in range(num_min+1, num_max):
        N = N * main[num]
else:
    for num in range(num_max+1, num_min):
        N = N * main[num]

print(sum([int(elem) for elem in main if elem > 0]), N)
