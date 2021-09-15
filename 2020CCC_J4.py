'''
ABCCDEABAA
ABCDE

yes

ABCDDEBCAB
ABA

no
'''

Str=input()
ss=input()
for i in range(len(Str)):
    ss=ss[1:]+ss[0]
    if ss in Str:
        print('yes')
        break
else:
    print('no')
