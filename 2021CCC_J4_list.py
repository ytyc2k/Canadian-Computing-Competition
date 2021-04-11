# ###########################################
# # Canadian Computing Conpetition ( CCC )  #
# # 2021 Junior J4                          #
# # Arranging Books                         #
# # Author : Tony Yang                      #
# # 2021-02-17                              #
# ###########################################
# ss = input()
ss = 'LMMMS'  # sample input 1  --> 0
ss = 'LLSLM'  # sample input 2  --> 2
# ss='SSLML'    # --> 3
ss = 'SSMLLSLLMM'  # ---> 5
st = sorted(ss)
# print(list(ss))
# print(st)
#
lCount = ss.count('L')
mCount = ss.count('M')
L = [ss[i] for i in range(lCount) if ss[i] != st[i]]
M = [ss[i] for i in range(lCount, lCount + mCount) if ss[i] != st[i]]
S = [ss[i] for i in range(lCount + mCount, len(ss)) if ss[i] != st[i]]
# print(L, M, S)
#
Ls = L.count('S')
Lm = L.count('M')
Ml = M.count('L')
Ms = M.count('S')
Sl = S.count('L')
Sm = S.count('M')

lst = [(Ls, Sl), (Lm, Ml), (Ms, Sm)]
print(lst)
swap = sum(y if x > y else x for x, y in lst)
swap += sum(abs(x - y) for x, y in lst) // 3 * 2

print(swap)

# tup='23 34'
# x,y=tup.split()
# print(x,y)
lst=[(1,0),(0,1),(0,1)]
lst=[j if i>j else i for i,j in lst]
print(lst)





