# '''
# 3
# 2 2 3
# 0
# 1 1
#
# '''

# Pages=int(input())
# lst=[tuple(map(int,input().split())) for i in range(Pages)]
#lst=[(2, 2, 3), (0,), (1, 1)]
#    1
#   / \
#  2   3
#     /
#    1


Pages=6
lst=[(2, 2, 3),(0,),(2,5,6),(0,),(1,2)]
#     1
#    / \
#   2   3
#  /   / \
# 0   5   6
#    /     \
#   0       2
lst=[i if i[0] else (1,0) for i in lst]
print(lst) #lst=[(2, 2, 3), (1, 0), (2, 5, 6), (1, 0), (1, 2)]

lst_in=['1']
while lst:
    for i in range(lst[0][0]):
        lst_in.append(f'{lst_in[0]}-{lst[0][i+1]}')
    lst.pop(0)
    lst_in.pop(0)
    if lst_in[0][-1]=='0':
        lst_in.append(lst_in.pop(0))

print(lst_in) # ['1-2-0', '1-3-5-0', '1-3-6-2']

if len(set('-'.join(lst_in)))-2==Pages:
    print('Y')
else:
    print('N')

print(min([i for i in lst_in if i[-1]=='0' ]).split('-')[-2]) # 1-2-0

# answer:
# N  # Less page 4
# 2  # The shortest path is 1-2-0