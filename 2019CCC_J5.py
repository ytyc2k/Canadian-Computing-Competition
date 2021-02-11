#Input:
'''
AA AB
AB BB
B AA
4 AB AAAB

'''

#Output
'''
2 1 BB
3 1 AAB
3 3 AAAA
1 3 AAAB
'''

lst=[input() for i in range(4)]
# lst=['AA AB', 'AB BB', 'B AA', '4 AB AAAB']
Rules=dict([i.split() for i in lst[:3]])
N=int(lst[3].split()[0])
SIN=lst[3].split()[1]
SOT=lst[3].split()[2]
#4 AB AAAB {'AA': 'AB', 'AB': 'BB', 'B': 'AA'}

def f():
    ss=Stack[0]
    rs=Record[0]
    for k,x in enumerate(Rules.keys(),start=1):
        i=0
        while (n := ss.find(x, i)) != -1:
            t=ss[:n] + Rules[x] + ss[n + len(x):]
            if t not in Stack:
                Stack.append(t)
                Record.append(f'{rs}{k} {n+1} {t} \n')
            i = n + 1
    Stack.pop(0)
    Record.pop(0)

Stack=[SIN]
Record=['']

for i in range(4):
    for j in range(len(Stack)):
        f()
# print(Stack)
# print(Record)

lst=[i for i in Record if SOT==i.split()[-1]]
if lst:
    print(lst[0])
