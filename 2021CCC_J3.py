###########################################
# Canadian Computing Conpetition ( CCC )  #
# 2021 Junior J3                          #
# Secret Instructions                     #
# Author : Tony Yang                      #
# 2021-02-17                              #
#
###########################################
# '''
# Sample Input
'''
56234
00907
34100
99999

Output for Sample Input
right 234
right 907
left 100
'''
pre=''
while True:
    ss=input()
    if ss=='99999':
        break
    he=int(ss[0])+int(ss[1])
    if he==0:
        print(pre+ss[2:])
    elif he%2==0:
        print('right '+ss[2:])
        pre='right '
    elif he%2==1:
        print('left '+ss[2:])
        pre='left '

# pre = ''
# while True:
#     ss = input()
#     if ss == '99999':
#         break
#     he = int(ss[0]) + int(ss[1])
#     if  he == 0:
#         print(pre, ss[2:])
#     elif he % 2 == 0:
#         print('right', ss[2:])
#         pre = 'right'
#     elif he % 2 == 1:
#         print('left', ss[2:5])
#         pre = 'left'
#
# ss='562344564654654654564655'
# print(ss[:-1])