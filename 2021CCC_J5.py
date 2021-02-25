###########################################
# Canadian Computing Conpetition ( CCC )  #
# 2021 Junior J5                          #
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

# # m,n,k=int(input()),int(input()),int(input())
# m, n, k = 4, 5, 7
# # lst=[input().split() for i in range(k)]
# lst = [['R', '3'], ['C', '1'], ['C', '2'], ['R', '2'], ['R', '2'], ['C', '1'], ['R', '4']]
# lst = [(x, int(y)) for x, y in lst]
# # print(lst)
# matrix = [['B' for i in range(n)] for j in range(m)]
# for x in matrix:
#     print(x)
# for x, y in lst:
#     if x == 'R':
#         for i in range(n):
#             if matrix[y - 1][i]=='B':
#                 matrix[y - 1][i] = 'G'
#             else:
#                 matrix[y - 1][i] = 'B'
#     if x == 'C':
#         for i in range(m):
#             if matrix[i][y - 1]=='B':
#                 matrix[i][y - 1] = 'G'
#             else:
#                 matrix[i][y - 1] = 'B'
# print('-----------------------------')
# s=0
# for x in matrix:
#     print(x)
#     s+=(x.count('G'))
# print('-----------------------------')
# print(s)

# import time
# T = time.time()
# m, n, k = 100, 50000, 700
# # lst=[input().split() for i in range(k)]
# lst = [['R', '3'], ['C', '1'],['C', '2'], ['R', '2'], ['R', '2'], ['C', '1'], ['R', '4']]*100
# lst=[(i,int(j)) for i,j in lst]
# matrix = [['B' for i in range(n)] for j in range(m)]
# for x, y in lst:
#     if x == 'R':
#         for i in range(n):
#             if matrix[y - 1][i] == 'B':
#                 matrix[y - 1][i] = 'G'
#             else:
#                 matrix[y - 1][i] = 'B'
#     if x == 'C':
#         for i in range(m):
#             if matrix[i][y - 1] == 'B':
#                 matrix[i][y - 1] = 'G'
#             else:
#                 matrix[i][y - 1] = 'B'
# s = 0
# for x in matrix:
#     s += (x.count('G'))
# print(s)
# print(time.time() - T)


# R, C, k = int(input()),int(input()),int(input())
# matrix = ['B' * C for i in range(R)]
# for cnt in range(k):
#     x, y = input().split()
#     y=int(y)
#     if x == 'R':
#         matrix[y - 1] = ''.join(['G' if i == 'B' else 'B' for i in matrix[y - 1]])
#     else:
#         matrix = [i[:y - 1] + 'G' + i[y:] if i[y - 1] == 'B' else i[:y - 1] + 'B' + i[y:] for i in matrix]
# s = 0
# for i in matrix:
#     s = s + i.count('G')
# print(s)

# from time import time
# T=time()
# m, n, k = int(input()), int(input()), int(input())
# lst = [input().split() for i in range(k)]
# lst = [i for i in lst if lst.count(i) % 2]
# lst = [(x, int(y)) for x, y in lst]
# matrix = [False for i in range(n) for j in range(m)]
# for x, y in lst:
#     if x == 'R':
#         for i in range(n):
#             matrix[(y-1)*n+i] = not matrix[(y-1)*n+i]
#     if x == 'C':
#         for i in range(m):
#             matrix[i*n+y-1] = not matrix[i*n+y-1]
# print(matrix.count(True))
# print(time()-T)

# m, n, k = int(input()), int(input()), int(input())
# lst = sorted([input().split() for i in range(k)])

# from time import time
# T = time()
# m, n, k = 100,50000,7
# lst = ['R 3', 'C 1', 'C 2', 'R 2', 'R 2', 'C 1', 'R 4']
# lst = [i for i in lst if lst.count(i) % 2]
# lst = [i.split() for i in lst]
# lst = [(i, int(j)) for i, j in lst]
#
# matrix = [[False for i in range(n)] for j in range(m)]
# for x, y in lst:
#     if x == 'R':
#         for i in range(n):
#             matrix[y - 1][i] = not matrix[y - 1][i]
#     else:
#         for i in range(m):
#             matrix[i][y - 1] = not matrix[i][y - 1]
# s = 0
# for x in matrix:
#     s += (x.count(True))
# print(s)
# print(time() - T)

R, C, k = int(input()), int(input()), int(input())
Rcommand = [False for _ in range(R)]
Ccommand = [False for _ in range(C)]
Grid = [[False for _ in range(C)] for _ in range(R)]
for i in Grid:
    print(i)
# for _ in range(k):
#     x, y = input().split()
#     y = int(y) - 1
#     if x == 'R':
#         Rcommand[y] = not Rcommand[y]
#     else:
#         Ccommand[y] = not Ccommand[y]
# for x in range(R):
#     if Rcommand[x]:
#         for y in range(C):
#             Grid[x][y] = not Grid[x][y]
# for y in range(C):
#     if Ccommand[y]:
#         for x in range(R):
#             Grid[x][y] = not Grid[x][y]
# s = 0
# for x in Grid:
#     s = s + x.count(True)
# print(s)

