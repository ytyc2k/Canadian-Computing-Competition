ss='VVHH'
lst=[
    (1,2),
    (3,4)
    ]
for i in ss:
    if i=='H':
        lst=[(lst[0][1],lst[0][0]),(lst[1][1],lst[1][0])] # H
    else:
        lst=[(lst[1][0],lst[1][1]),(lst[0][0],lst[0][1])] # V
print(lst[0][0],lst[0][1])
print(lst[1][0],lst[1][1])

ss='VVHH'
lst=[
    (1,2),
    (3,4)
    ]
for i in ss:
    if i=='H':
        lst=[(lst[0][1],lst[0][0]),(lst[1][1],lst[1][0])] # H
    else:
        lst=lst[::-1] # V
print(lst[0][0],lst[0][1])
print(lst[1][0],lst[1][1])

ss='VVHH'
lst=[
    (1,2),
    (3,4)
    ]
for i in ss:
    if i=='H':
        lst=[(g,k) for k,g in lst] # H
    else:
        lst=lst[::-1] # V
print(lst[0][0],lst[0][1])
print(lst[1][0],lst[1][1])

ss='VVHH'
lst=[
    (1,2),
    (3,4)
    ]
a,b=lst[0][0],lst[0][1]
c,d=lst[1][0],lst[1][1]
for i in ss:
    if i=='H':
        a,b=b,a # H
        c,d=d,c
    else:
        a,c=c,a # V
        b,d=d,b
print(a,b)
print(c,d)