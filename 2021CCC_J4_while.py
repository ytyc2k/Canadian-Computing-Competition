###########################################
# Canadian Computing Conpetition ( CCC )  #
# 2021 Junior J4                          #
# Arranging Books                         #
# Author : Tony Yang                      #
# 2021-02-17                              #
###########################################
# ss = input()
# ss = 'LMMMS'  # sample input 1  --> 0
ss = 'SSLML'  # sample input 2  --> 3
# ss='SSSSMMMMMLLMMLSMMMMSSLLLLLSLL'
# ss='SSMLLSLLMM'
st = sorted(ss)
print(list(ss))
print(st)
#
lCount = ss.count('L')
mCount = ss.count('M')
L = [ss[i] for i in range(lCount) if ss[i] != st[i]]
M = [ss[i] for i in range(lCount, lCount + mCount) if ss[i] != st[i]]
S = [ss[i] for i in range(lCount + mCount, len(ss)) if ss[i] != st[i]]
print(L, M, S)
#
swap = 0
while True:
    if L==[] and M==[] and S==[]:
        break
    if set(L)=={'M'} and set(M)=={'S'} and set(S)=={'L'}:
        swap+=len(L)*2
        break
    if set(L)=={'S'} and set(M)=={'L'} and set(S)=={'M'}:
        swap+=len(L)*2
        break
    if 'S' in L and 'L' in S:
        L.remove('S')
        S.remove('L')
        swap+=1
    if 'M' in L and 'L' in M:
        L.remove('M')
        M.remove('L')
        swap+=1
    if 'S' in M and 'M' in S:
        M.remove('S')
        S.remove('M')
        swap+=1

print(L,M,S)
print(swap)