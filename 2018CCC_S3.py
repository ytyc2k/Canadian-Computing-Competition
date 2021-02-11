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
M = 7
Matrix = [
    ['W', 'W', 'W', 'W', 'W', 'W', 'W'],
    ['W', 'D', '.', 'L', '.', 'R', 'W'],
    ['W', '.', 'W', 'C', 'U', '.', 'W'],
    ['W', 'W', 'W', '.', 'S', '.', 'W'],
    ['W', 'W', 'W', 'W', 'W', 'W', 'W']]

for i in range(N):
    for j in range(M):
        if Matrix[i][j] == 'S':
            break
    if Matrix[i][j] == 'S':
        break
Stack = [[i, j]]
record = [f'{[i, j]}-']
while Stack:
    i = Stack[0][0]
    j = Stack[0][1]
    rs = record[0]
    k = 0
    if 0 < i < N - 1 and 0 < j < M - 1:
        if Matrix[i - 1][j] not in 'WC0':
            Stack.append([i - 1, j])
            record.append(f'{rs}{[i - 1, j]}-')
            k = k + 1
        elif Matrix[i + 1][j] not in 'WC0':
            Stack.append([i + 1, j])
            record.append(f'{rs}{[i + 1, j]}-')
            k = k + 1
        elif Matrix[i][j - 1] not in 'WC0':
            Stack.append([i, j - 1])
            record.append(f'{rs}{[i, j - 1]}-')
            k = k + 1
        elif Matrix[i][j + 1] not in 'WC0':
            Stack.append([i, j + 1])
            record.append(f'{rs}{[i, j + 1]}-')
            k = k + 1
    Matrix[i][j] = '0'
    # if k > 0:
    #     record.pop(0)
    record.pop(0)
    Stack.pop(0)

    # print(i, j)
    # print(Stack)
    print(record)
print(Matrix)
print(sorted(record))
