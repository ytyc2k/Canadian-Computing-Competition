# 2020-2-2 14:15pm
# 2020-2-2 14:36pm
'''
Sample Input
4
5 6
6 6
4 3
5 2

Output for Sample Input
94
91
'''
n=int(input())
lst_in=[list(map(int,input().split())) for i in range(n)]
print(lst_in)
A=D=100
for x,y in lst_in:
    if x<y:
        A=A-y
    elif x>y:
        D=D-x

print(A)
print(D)

