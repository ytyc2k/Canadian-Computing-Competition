'''
4 5
WWWWW
W.W.W
WWS.W
WWWWW

'''

# S=input().split()
# N=int(S[0])
# M=int(S[1])
# Matrix=[list(input()) for i in range(N)]
# print(Matrix)
N = 5
M = 8
Matrix = [
    ['W', 'W', 'W', 'W', 'W', 'W', 'W','W'],
    ['W', 'D', '.', '.', '.', 'R', 'W','W'],
    ['W', '.', 'W', 'C', 'U', '.', '.','W'],
    ['W', 'W', 'W', '.', 'S', '.', '.','W'],
    ['W', 'W', 'W', 'W', 'W', 'W', 'W','W']]

for i in range(N):
    for j in range(M):
        if Matrix[i][j] == 'C':
            break
    if Matrix[i][j] == 'C':
        break

Stack = [[i, j]]
CX,CY=i,j
print(CX,CY)
while Stack:
    x,y=Stack.pop(0)
    if Matrix[x][y]==-1 or Matrix[x][y] in 'W' or CX!=x and CY!=y:
        continue
    if Matrix[x][y] not in 'UDLR':
        Matrix[x][y] = -1
    Stack.append((x-1,y))
    Stack.append((x+1,y))
    Stack.append((x,y-1))
    Stack.append((x,y+1))
Matrix[CX][CY]='C'

for i in range(N):
    for j in range(M):
        if Matrix[i][j] == 'S':
            break
    if Matrix[i][j] == 'S':
        break
Stack = [[i, j]]
CX,CY=i,j
Record=[f'{i,j}']
R=[]
while Stack:
    x,y=Stack.pop(0)
    rs=Record.pop(0)
    if Matrix[x][y] == -1 or Matrix[x][y] in 'CW0123456789':
        continue
    if Matrix[x][y] not in 'UDLR':
        Matrix[x][y] = '0'
        R.append(rs)
    Stack.append((x-1,y))
    Record.append(f'{rs}-{x-1,y}')
    Stack.append((x+1,y))
    Record.append(f'{rs}-{x+1,y}')
    Stack.append((x,y-1))
    Record.append(f'{rs}-{x,y-1}')
    Stack.append((x,y+1))
    Record.append(f'{rs}-{x,y+1}')
for i in Matrix:
    print(i)
print(Record)
print(R)
