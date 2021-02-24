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
    ['W', 'D', '.', 'L', '.', 'R', 'W','W'],
    ['W', '.', 'W', 'C', 'U', '.', '.','W'],
    ['W', 'W', 'W', '.', 'S', '.', '.','W'],
    ['W', 'W', 'W', 'W', 'W', 'W', 'W','W']]

for i in range(N):
    for j in range(M):
        if Matrix[i][j] == 'C':
            break
    if Matrix[i][j] == 'C':
        break

Stack = [(i, j)]
print(Stack)
CX,CY=i,j
while Stack:
    x,y=Stack.pop(0)
    if Matrix[x][y] in 'WX' or CX!=x and CY!=y:
        continue
    if Matrix[x][y] not in 'UDLR':
        Matrix[x][y] = 'X'
    Stack.append((x-1,y))
    Stack.append((x+1,y))
    Stack.append((x,y-1))
    Stack.append((x,y+1))


# for i in range(N):
#     for j in range(M):
#         if Matrix[i][j] == 'S':
#             break
#     if Matrix[i][j] == 'S':
#         break
#
# Stack = [(i, j)]
# CX,CY=i,j
# Record=[f'{i,j}']
# R=[]
# while Stack:
#     x,y=Stack.pop(0)
#     rs=Record.pop(0)
#     if Matrix[x][y] in 'WX0':
#         continue
#     if Matrix[x][y] in 'S.':
#         Matrix[x][y] = '0'
#         Stack.append((x - 1, y))
#         Record.append(f'{rs}-{x-1,y}')
#         Stack.append((x + 1, y))
#         Record.append(f'{rs}-{x+1,y}')
#         Stack.append((x, y - 1))
#         Record.append(f'{rs}-{x,y-1}')
#         Stack.append((x, y + 1))
#         Record.append(f'{rs}-{x,y+1}')
#         R.append(rs)
#     elif Matrix[x][y] == 'U':
#         Stack.append((x-1,y))
#         Record.append(f'{rs}-{x-1,y}')
#     elif Matrix[x][y] == 'D':
#         Stack.append((x+1,y))
#         Record.append(f'{rs}-{x+1,y}')
#     elif Matrix[x][y] == 'L':
#         Stack.append((x,y-1))
#         Record.append(f'{rs}-{x,y-1}')
#     elif Matrix[x][y] == 'R':
#         Stack.append((x,y+1))
#         Record.append(f'{rs}-{x,y+1}')
#
#
# print(R)
# R.sort()
# R=[R[i-1] for i in range(len(R)) if R[i].find(R[i-1])]
# print(R)
# # R3=[list(map(eval,x.split('-'))) for x in R]
# # print(R3)
# # R4=[(j,k) for x in R3 for j,k in x if Matrix[j][k] not in 'UDLR']
# # print(R4)
# # #
# # # k=0
# # # for x,y in R4:
# # #    if (x,y)==(CX,CY):
# # #        k=0
# # #    else:
# # #        k+=1
# # #        Matrix[x][y]=k
# #
for i in Matrix:
    print(i)
