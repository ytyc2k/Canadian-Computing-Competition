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
pre=''
while True:
    ss=input()
    if ss=='99999':
        break
    he=int(ss[0])+int(ss[1])
    if he!=0 and he%2==0:
        pre='right '
    elif he%2==1:
        pre='left '
    print(pre+ss[2:])
        