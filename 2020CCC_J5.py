#input:
'''
3
4
3 10 8 14
1 11 12 12
6 2 3 9

'''

#output:
'''
yes
'''

# R=int(input())
# C=int(input())
# lst=[list(map(int,input().split())) for i in range(R)]
# print(lst)
R=3
C=4
lst=[[3, 10, 8, 14],
     [1, 11, 12, 12],
     [6, 2, 3, 9]]

def f():
    global R,C
    si = stack[0]
    for i in range(si):
        for j in range(si):
            if (i + 1) * (j + 1) == si:
                try:
                    if i == R - 1 and j == C - 1:
                        return 1
                    if lst[i][j] != 0:
                        stack.append(lst[i][j])
                        lst[i][j] = 0
                except:
                    continue
    stack.pop(0)
stack=[lst[0][0]]
while stack:
    if f():
        print('Yes')
        break
    # print(stack)
    # print(lst)
else:
    print('NO')
