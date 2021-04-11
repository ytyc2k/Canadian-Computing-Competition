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
57234
00907
34100
99999

Output for Sample Input
right 234
right 907
left 100
'''

# direction=''
# while True:
#     ss=input()
#     if ss=='99999':
#         break
#     pre=int(ss[0])+int(ss[1])
#     if pre!=0 and pre%2==0:
#         direction='right '
#     else:
#         direction='left '
#     print(direction+ss[2:])

direction=''
while (ss:=input())!='99999':
    pre=int(ss[0])+int(ss[1])
    if pre!=0 and pre%2==0:
        direction='right '
    else:
        direction='left '
    print(direction+ss[2:])
        