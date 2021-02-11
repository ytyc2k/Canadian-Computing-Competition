#2021-2-4 15:04
'''
14
R 12
W 2
R 23
W 3
R 45
S 45
R 45
S 23
R 23
W 2
S 23
R 34
S 12
S 34

5
R 2
R 3
W 5
S 2
S 3

'''
n=int(input())
lst=[input().split() for i in range(n)]
# print(lst)
# lst=[['R', '12'], ['W', '2'], ['R', '23'], ['W', '3'], ['R', '45'], ['S', '45'], ['R', '45'], ['S', '23'], ['R', '23'], ['W', '2'], ['S', '23'], ['R', '34'], ['S', '12'], ['S', '34']]
lst=[(x,int(y)) for x,y in lst]
dic={y:[0,-1] for x,y in lst if x!='W'}
time=0
for x,y in lst:
    if x=='R':
        dic[y][0]=time-dic[y][0]
        dic[y][1] = -1
    if x=='W':
        time=time+y-2
    if x=='S':
        dic[y][0] = time - dic[y][0]
        dic[y][1]=0
    time=time+1
# print(lst)
# print(dic)
for x,y in sorted(dic.items()):
    if y[1]==-1:
        print(x,y[1])
    else:
        print(x,y[0])

