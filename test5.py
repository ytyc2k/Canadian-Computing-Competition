import time
T = time.time()
R, C, k = 10000, 5000, 7
lst = ['R 3', 'C 2', 'R 2', 'R 2', 'C 1', 'R 4']
lst.sort()
lst=[i for i in lst if lst.count(i)%2]
# matrix=['B'*C for i in range(R)]
# for k in lst:
#     x,y=k.split()
#     if x=='R':
#         matrix[y-1]=''.join(['G' if i=='B' else 'B' for i in matrix[y-1]])
#     if x=='C':
#         matrix=[i[:y-1]+'G'+i[y:] if i[y-1]=='B' else i[:y-1]+'B'+i[y:]  for i in matrix ]
# s=0
# for i in matrix:
#     s=s+i.count('G')
# print(s)

print(time.time()-T)
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

# R=[]
# for i in range(7):
#     s=input().split()
#     s=s[0]+s[1]
#     if s in R:
#         R.remove(s)
#     else:
#         R.append(s)
