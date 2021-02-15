# 2020-2-2 12:55pm
# 2020-2-2 13:01pm
'''
Sample Input 1
6
ABBABB

Output for Sample Input 1
B
'''
n=int(input())
s=input()
A=s.count('A')
B=s.count('B')
if A>B:
    print('A')
elif A<B:
    print('B')
elif A==B:
    print('Tie')
