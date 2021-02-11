# 2020-2-2 15:10pm
# 2020-2-2 15:32pm
'''
4
Ada Alan Grace John
John Grace Alan Ada

'''
n = int(input())
Lst_Grp = list(zip(input().split(), input().split()))
print(Lst_Grp)

Lst = [(x,y) for x, y in Lst_Grp if x == y or (y, x) not in Lst_Grp]
print(Lst)
if Lst:
    print('bad')
else:
    print('good')