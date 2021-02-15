'''
Sample Input 1
8
4
Output for Sample Input 1
5
'''
# # m,n=int(input()),int(input())
# # m,n=8,4
# # m,n=70,70
# # m,n=70,15
#
# visited = []
#
# def pi(n,k,min):
#     if visited [n][k][min] == 0:
#         if n == k:
#             visited[n][k][min] = 1
#         elif k == 1:
#             visited[n][k][min] = 1
#         else:
#             t = 0
#             for i in range (min, (n // k)+1):
#                 t = t + pi(n-i, k-1, i)
#             visited[n][k][min] = t
#
#     return visited[n][k][min]
#
#
#
# n = 250
# k = 120
#
# for i in range(n+1):
#     x = []
#     for j in range(k+1):
#         t = []
#         for kk in range(n+1):
#             t.append (0)
#         x.append(t)
#     visited.append(x)
#
# print(pi(n,k,1))

# m,n=int(input()),int(input())
m,n=70,15
from itertools import combinations_with_replacement
print(sum([1 for x in combinations_with_replacement(range(1,m-n+2),n) if sum(x)==m]))
