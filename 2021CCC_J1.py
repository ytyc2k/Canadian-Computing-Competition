###########################################
# Canadian Computing Conpetition ( CCC )  #
# 2021 Junior J1                          #
#  Boiling Water                          #
# Author : Tony Yang                      #
# 2021-02-17                              #
###########################################

'''
Sample Input 2
102

Output for Sample Input 2
110
-1
'''

B = int(input())
P = 5 * B - 400
print(P)
if B<100:
    print(1)
elif B>100:
    print(-1)
elif B==100:
    print(0)

