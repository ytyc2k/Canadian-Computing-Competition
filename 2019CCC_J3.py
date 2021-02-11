'''
4
+++===!!!!
777777......TTTTTTTTTTTT
(AABBC)
3.1415555
#
# '''
# from itertools import groupby
# # n=int(input())
# # lst=[input() for i in range(n)]
# # lst=['+++===!!!!', '777777......TTTTTTTTTTTT', '(AABBC)', '3.1415555']
# for x in lst:
#     print(' '.join([' '.join((str(len(list(g))),k)) for k,g in groupby(x)]))

lst=[1,2,3]
lst=[str(i) for i in lst]
print(lst)
print(tuple(map(str,lst)))
ll=zip([1,2,3],
       [4,5,6],
       [7,8,9])
print(list(ll))

