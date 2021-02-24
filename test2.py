# input:
'''
3
4
3 10 8 14
1 11 12 12
6 2 3 9

'''

# output:
'''
yes
'''

R = int(input())
C = int(input())
lst = [list(map(int, input().split())) for i in range(R)]

#
# R = 3
# C = 4
# lst = [[3, 10, 8, 14],
#        [1, 11, 12, 12],
#        [6, 2, 3, 9]]
Stack = [(0, 0)]
while Stack:
    x, y = Stack.pop(0)
    N = lst[x][y]
    if N == 0:
        continue
    if (x, y) == (R - 1, C - 1):
        print('yes')
        break

    lst[x][y] = 0

    for i in range(1,R+1):
        for j in range(1,C+1):
            if i * j == N:
                Stack.append((i - 1, j - 1))
else:
    print('no')
