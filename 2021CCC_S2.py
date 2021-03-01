###########################################
# Canadian Computing Conpetition ( CCC )  #
# 2021 Senior S2                          #
# Modern Art                              #
# Author : Tony Yang                      #
# 2021-02-17                              #
###########################################
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
R, C, k = int(input()), int(input()), int(input())
Rcommand = [False for _ in range(R)]
Ccommand = [False for _ in range(C)]
Canvas = [[False for _ in range(C)] for _ in range(R)]
for _ in range(k):
    x, y = input().split()
    y = int(y) - 1
    if x == 'R':
        Rcommand[y] = not Rcommand[y]
    else:
        Ccommand[y] = not Ccommand[y]
for x in range(R):
    if Rcommand[x]:
        for y in range(C):
            Canvas[x][y] = not Canvas[x][y]
for y in range(C):
    if Ccommand[y]:
        for x in range(R):
            Canvas[x][y] = not Canvas[x][y]
s = 0
for x in Canvas:
    s = s + x.count(True)
print(s)

