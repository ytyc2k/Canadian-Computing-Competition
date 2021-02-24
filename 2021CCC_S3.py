###########################################
# Canadian Computing Conpetition ( CCC )  #
# 2021 Senior S3                          #
# Author : Tony Yang                      #
# 2021-02-17                              #
###########################################
'''
1
0 1000 0
0

2
10 4 3
20 4 2

3
6 8 3
1 4 1
14 5 2
'''

n = int(input())
lst = [tuple(map(int, input().split())) for i in range(n)]
Max = max(lst)[0]
Min = min(lst)[0]
Scope = Max + 1
R = []
for k, n in enumerate(range(Min, Scope), start=Min):
    s = 0
    for x, y, z in lst:
        if x - z > k:
            s += y * (x - k - z)
        elif x + z < k:
            s += y * (k - x - z)
        if k == 9:
            print(s, k, x, y, z)
    R.append((s, k))
    # print(k,x,y,z,s)
print(min(R)[0])
