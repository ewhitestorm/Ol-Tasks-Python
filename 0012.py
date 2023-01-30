# Solving tasks to competitive programming from the site https://acmp.ru
# Author of solutions: Eugene Storm
# 
# Task №12
# ID 0012
# Completion time - 0,046 sec.


n = int(input())
list_n = []
t = 0

def S_triangle(ax,ay,bx,by,cx,cy):
  return abs((ax-bx)*(cy-by)-(ay-by)*(cx-bx))

for i in range(0, n):
  list_elem = [int(i) for i in list(''.join(input()).split(' '))]
  list_n.append(list_elem)
  
for v in list_n:
  S_space = S_triangle(v[2],v[3],v[4],v[5],v[6],v[7]) + S_triangle(v[2],v[3],v[8],v[9],v[6],v[7])
  
  if S_space == (S_triangle(v[2],v[3],v[4],v[5],v[0],v[1]) +
                 S_triangle(v[6],v[7],v[4],v[5],v[0],v[1]) +
                 S_triangle(v[2],v[3],v[8],v[9],v[0],v[1]) +
                 S_triangle(v[6],v[7],v[8],v[9],v[0],v[1])
                 ):
    t += 1

print(t)
