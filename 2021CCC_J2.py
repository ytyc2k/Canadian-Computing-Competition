###########################################
# Canadian Computing Conpetition ( CCC )  #
# 2021 Junior J2                          #
# Silent Auction                          #
# Author : Tony Yang                      #
# 2021-02-17                              #
###########################################

'''
3
Ahmed
400
Suzanne
500
Ivona
500
'''

# n=int(input())
# lst=[(input(),int(input())) for _ in range(n)]
# # lst=[('Ahmed', 400), ('Suzanne', 500), ('Ivona', 500)]
# print(max(lst,key=lambda x:x[1])[0])

# n=int(input())
# lst=[input() for i in range(n*2)]
lst=['Ahmed', '400', 'Suzanne', '500', 'Ivona', '500']
a=lst[::2]
b=lst[1::2]
# print(a[b.index(max(b))])
#
# b.index(max(b))
print(a)
print(b)
lst=list(zip(a,b))
print(lst)
print(max(lst,key=lambda x:x[1])[0])