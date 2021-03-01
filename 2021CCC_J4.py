###########################################
# Canadian Computing Conpetition ( CCC )  #
# 2021 Junior J4                          #
# Arranging Books                         #
# Author : Tony Yang                      #
# 2021-02-17                              #
###########################################
ss = input()
# ss = 'LMMMS'  # sample input 1  --> 0
# ss = 'LLSLM'  # sample input 2  --> 2
# ss = 'MSLSLSMLSLM'  # sample input 3  --> 3
# ss='MSLLLLSLMLLMSSLMMMMSSSMSSSSMSSMMMMSSSMMSSMSLLMMLSMSLMMSLLMSSMMLMMSSMLLSSLMLMLMMSSLLLLSLLMLSMSMLMMMMSSMMSSSMMLMLLMMSLLLMSSLSLMSLLMSSLMSLMMMMMMSMMLMSLSSSMSLLLLMLMLLSSMSMLLSMLLLLMLLMSLSMMMLSMMMLSLLMSSMSLSSMLLSLMMSMSSLSMMMMLMLMMLSSSSSSLLMSMLSSSMMLLMMLSLLLLSSLLMMLSSMLLLLLMSSLMMMSLLLSLSMMLMLLLMMSSLMSSLMSMMMLSLMLMMLSLSMLMSMSMSMMMLSLMLSLLSMSSSMMLMLMLSSMLMSSMMSMMSSMLSSSSMSMLMLSMMLSMMSMLSMSLMMSLLMSLSLLLSMLSSLLSSLLSMMLSMSSMMLSSLMMLMLMMLMSMMMMSMSMSMMLLLMSSMLLMMSSSMLSSSLSSMMMSLLLSSMMSLMMSLMMSLSLMLSMMSSLMSMSLMMLMMSSSSLLSSMSMSLLSLMMSMLMLLLSSLSSLSSLLSMLLSLSMMSLSMLMSLMMMMLSLSMLMLSSSMSMSLMSLSLSSMSLSSMSSSLSSLMMLLSSLLSLSMMMMMLSSSMLMMMSSLMLMSSLMSLSSSSSMLSSMSSLLLLLLLMMLLLMLSMMLLSLSLMMSSLSLMMMSLSLLLMLMMMLSLMSMSMLMLSSSSSLSSSSLMMMSSSLMLLSMLSSSMLLMLMSLLMMMMSMLLSMSLMLSLLSMSSLLMMLLMLSMLLSLSLSSLSMSLMLSSLSLMMMLSLLSLSLLMSMLMLSSLMMLMLMSLMLLMMSMMLMLMMMMSLLMSSMLSMMSLLSSMLSMLMSLLMLMSMSMMSMSMSLLMSSLSMMMLMLLMSMMMMLLLSMLLSMSLLSSLMSSSMSMMSLLSLLSMSMLSMSMLLLMMLMSMSSSLSLMSMMLLSMLLSMMMLMSLLMMSMMLLLLMSSSMMLLSMSLSMMLMMLLLMSMLMLLS'
st = sorted(ss)
# print(list(ss))
# print(st)

lCount = ss.count('L')
mCount = ss.count('M')
L=[ss[i] for i in range(lCount) if ss[i] != st[i]]
M=[ss[i] for i in range(lCount,lCount+mCount) if ss[i] != st[i]]
S=[ss[i] for i in range(lCount+mCount,len(ss)) if ss[i] != st[i]]
# print(L,M,S)
n=1
swap=0
while swap!=n:
    n=swap
    if 'S' in L and 'L' in S:
        L.remove('S')
        S.remove('L')
        swap += 1
    if 'M' in L and 'L' in M:
        L.remove('M')
        M.remove('L')
        swap += 1
    if 'S' in M and 'M' in S:
        M.remove('S')
        S.remove('M')
        swap += 1

swap=swap+(len(L)+len(M)+len(S))/3*2
print(int(swap))