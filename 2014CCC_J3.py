# 2020-2-2 14:15pm
# 2020-2-2 14:36pm
n=int(input())
lst_in=[list(map(int,input().split())) for i in range(n)]

A=D=100
for x,y in lst_in:
    if x<y:
        A=A-y
    elif x>y:
        D=D-x

print(A)
print(D)
