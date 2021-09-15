'''
5
44,62
34,69
24,78
42,44
64,10

23,9
65,79
'''

N=int(input())
Points=[(int(x),int(y)) for x,y in [input().split(',') for i in range(N)]]
# print(Points)
# N=5
# Points=[(44, 62), (34, 69), (24, 78), (42, 44), (64, 10)]
R=tuple(zip(*Points))
print(min(R[0])-1,min(R[1])-1,sep=',')
print(max(R[0])+1,max(R[1])+1,sep=',')


