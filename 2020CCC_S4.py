# 2020 CCC S4
'''
Sample Input
BABCBCACCA

Output for Sample Input
2
'''
# ss=input()
m = 'BABCBCACCA'
# m='BCAABA'
dic = {'ABA': 'BAB', 'ACA': 'CAC', 'BAB': 'ABA', 'BCB': 'ACA', 'CAC': 'ABA', 'CBC': 'BCB', }
lst = [m[-i - 1:] + m[:-i - 1] for i in range(len(m))]
k = 0
ss=''
for lp in lst:
    for i, j in dic.items():
        a = lp.find(i)
        b = lp.find(j)
        if a != -1 and b != -1 and abs(a - b) >= 3:
            c = lp[a + 1]
            d = lp[b + 1]
            print(lp)
            ss = lp[:a] + c + lp[a + 1]
            ss = lp[:b] + d + lp[b + 1]
            print(ss, i, j)
            break
        # else:
        #     continue
            # a=m.find(i)
            # b=m.find(j)
            # c=m[a+1]
            # d=m[b+1]
            # m=m[:a]+d+m[:a+1]
            # m=m[:b]+c+m[:b+1]
