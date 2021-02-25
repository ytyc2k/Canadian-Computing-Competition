###########################################
# Canadian Computing Conpetition ( CCC )  #
# 2021 Junior J4                          #
# Arranging Books                         #
# Author : Tony Yang                      #
# 2021-02-17                              #
###########################################
# ss = input()
# ss = 'LMMMS'  # sample input 1  --> 0
# ss = 'LLSLM'  # sample input 2  --> 2
ss = 'MSLSLSMLSLM'  # sample input 3  --> 3
st = sorted(ss)
print(list(ss))
print(st)

lCount = ss.count('L')
mCount = ss.count('M')
L=[ss[i] for i in range(lCount) if ss[i] != st[i]]
M=[ss[i] for i in range(lCount,lCount+mCount) if ss[i] != st[i]]
S=[ss[i] for i in range(lCount+mCount,len(ss)) if ss[i] != st[i]]
print(L,M,S)

swap=0
n=len(L) + len(M) + len(S)
while n>3:
    n=len(L) + len(M) + len(S)
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
    print(n)


print(swap)
print(L,M,S)

swap=swap+(len(L)+len(M)+len(S))/3*2
print(swap)
print(int(swap))



# lCount = ss.count('L')
# mCount = ss.count('M')
# print(lCount, mCount)
#
# section1Ems = ss[:lCount].count('M')
# section1Esses = ss[:lCount].count('S')
#
# section2Els = ss[lCount:lCount + mCount].count('L')
# section2Esses = ss[lCount:lCount + mCount].count('S')
#
# section3Els = ss[lCount + mCount:len(ss)].count('L')
# section3Ems = ss[lCount + mCount:len(ss)].count('M')
#
# print(section1Esses, section1Ems, section2Esses, section2Els, section3Els, section3Ems)
#
#
# swaps = 0
#
# if section1Esses != 0 and section3Els != 0:
#     if section1Esses == section3Els:
#         swaps += section3Els
#         section1Esses = 0
#         section3Els = 0
#     elif section1Esses < section3Els:
#         swaps += section1Esses
#         section3Els -= section1Esses
#         section1Esses = 0
#     else:
#         swaps += section3Els
#         section1Esses -= section3Els
#         section3Els = 0
# print(section1Esses, section1Ems, section2Esses, section2Els, section3Els, section3Ems)
# print(swaps)
#
# if section1Ems != 0 and section2Els != 0:
#     if section1Ems == section2Els:
#         swaps += section2Els
#         section1Ems = 0
#         section2Els = 0
#     elif section1Ems < section2Els:
#         swaps += section1Ems
#         section2Els -= section1Ems
#         section1Ems = 0
#     else:
#         swaps += section2Els
#         section1Ems -= section2Els
#         section2Els = 0
# print(section1Esses, section1Ems, section2Esses, section2Els, section3Els, section3Ems)
# print(swaps)
#
# if section3Ems != 0 and section2Esses != 0:
#     if section3Ems == section2Esses:
#         swaps += section2Esses
#         section3Ems = 0
#         section2Esses = 0
#     elif section3Ems < section2Esses:
#         swaps += section3Ems
#         section2Esses -= section3Ems
#         section3Ems = 0
#     else:
#         swaps += section2Esses
#         section3Ems -= section2Esses
#         section2Esses = 0
# print(section1Esses, section1Ems, section2Esses, section2Els, section3Els, section3Ems)
# print(swaps)
#
# swaps += (section1Esses + section1Ems + section2Esses + section2Els + section3Els + section3Ems) / 3 * 2
# print(int(swaps))

