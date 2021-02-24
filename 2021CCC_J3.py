###########################################
# Canadian Computing Conpetition ( CCC )  #
# 2021 Junior J3                          #
# Secret Instructions                     #
# Author : Tony Yang                      #
# 2021-02-17                              #
###########################################
'''
Sample Input
57234
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
    direction=int(ss[0])+int(ss[1])
    if direction!=0 and direction%2==0:
        print('right',ss[2:])
        pre='right'
    elif direction%2==1:
        print('left', ss[2:])
        pre='left'
    elif direction%2==0 and pre!='':
        print(pre,ss[2:])

