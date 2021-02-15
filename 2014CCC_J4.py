# 2020-2-2 14:36pm
# 2020-2-2 15:10pm
'''
Sample Input
10
2
2
3

Output for Sample Input
1
3
7
9
'''
K=int(input())
m=int(input())
P=list(range(1,K+1))
lst_in=[int(input()) for i in range(m)]

for i in lst_in:
    P=[P[j] for j in range(len(P)) if (j+1)%i]
    print(P)

for i in P:
    print(i)