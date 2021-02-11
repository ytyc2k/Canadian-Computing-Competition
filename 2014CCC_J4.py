# 2020-2-2 14:36pm
# 2020-2-2 15:10pm
K=int(input())
m=int(input())
P=list(range(1,K+1))
lst_in=[int(input()) for i in range(m)]

for i in lst_in:
    P=[P[j] for j in range(len(P)) if (j+1)%i]
    print(P)

for i in P:
    print(i)