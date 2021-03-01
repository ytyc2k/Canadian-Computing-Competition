###########################################
# Canadian Computing Conpetition ( CCC )  #
# 2021 Junior J4                          #
# Arranging Books                         #
# Author : Tony Yang                      #
# 2021-02-17                              #
###########################################
ss = input()
# ss = 'LMMMS'  # sample input 1  --> 0
# ss = 'SSLML'  # sample input 2  --> 2
st = sorted(ss)
# print(list(ss))
# print(st)

lCount = ss.count('L')
mCount = ss.count('M')
L = [ss[i] for i in range(lCount) if ss[i] != st[i]]
M = [ss[i] for i in range(lCount, lCount + mCount) if ss[i] != st[i]]
S = [ss[i] for i in range(lCount + mCount, len(ss)) if ss[i] != st[i]]
# print(L, M, S)

swap = a = b = c = 0
Lm = L.count('M')
Ls = L.count('S')
Ms = M.count('S')
Ml = M.count('L')
Sl = S.count('L')
Sm = S.count('M')
# print(Lm, Ls, Ms, Ml, Sl, Sm)
if Ls and Sl:
    a = Ls if Ls <= Sl else Sl
    swap += a
    Ls -= a
    Sl -= a
# print(Lm, Ls, Ms, Ml, Sl, Sm)
if Lm and Ml:
    b = Lm if Lm <= Ml else Ml
    swap += b
    Lm -= b
    Ml -= b
# print(Lm, Ls, Ms, Ml, Sl, Sm)
if Ms and Sm:
    c = Ms if Ms <= Sm else Sm
    swap += c
    Ms -= c
    Sm -= c
# print(Lm, Ls, Ms, Ml, Sl, Sm)
# print(swap)

swap += (Lm + Ls + Ms + Ml + Sl + Sm) / 3 * 2
print(int(swap))
