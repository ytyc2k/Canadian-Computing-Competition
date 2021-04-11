'''
4
5
7
R 3
C 1
C 2
R 2
R 2
C 1
R 4
'''
from time import time
T=time()
print(T)
R = 4
C = 5
N = 7
Canvas = [[0] * C for i in range(R)]
Rc = [1 for _ in range(R)]
Cc = [1 for _ in range(C)]
for i in range(R):
    print(Canvas[i])
for i in range(N):
    x, y = input().split()
    y = int(y) - 1
    if x == 'R':
        Rc[y] = ~ Rc[y]
    elif x == 'C':
        Cc[y] = ~ Cc[y]
print(Rc)
print(Cc)

for i in range(R):
    if Rc[i]:
        for x in range(C):
            Canvas[i][x] = ~ Canvas[i][x]
for i in range(C):
    if Cc[i]:
        for x in range(R):
            Canvas[x][i]=~ Canvas[x][i]
print(time()-T)









