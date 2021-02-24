Matrix = [
    ['w', 'w', 'w', 'w', 'w', 'w'],
    ['w', 'w', '.', 'w', 'w', 'w'],
    ['w', '.', '.', 'w', 'w', 'w'],
    ['w', '.', '.', '.', 'w', 'w'],
    ['w', 'S', 'w', '.', '.', 'w'],
    ['w', '.', 'w', 'w', 'w', 'w'],
    ['w', '.', 'w', 'w', 'w', 'w'],
    ['w', 'w', 'w', '.', '.', 'w'],
    ['w', 'w', 'w', 'w', 'w', 'w'],
]

Stack = [(4, 1)]
Record = [f'{4, 1}']
R=[]
j=0
while Stack:
    x, y = Stack.pop(0)
    rs = Record.pop(0)
    if Matrix[x][y] in 'w0':
        continue
    Matrix[x][y] = '0'
    R.append(rs)
    Stack.append((x - 1, y))
    Record.append(f'{rs}-{x - 1, y}')
    Stack.append((x + 1, y))
    Record.append(f'{rs}-{x + 1, y}')
    Stack.append((x, y - 1))
    Record.append(f'{rs}-{x, y - 1}')
    Stack.append((x, y + 1))
    Record.append(f'{rs}-{x, y + 1}')
print(Record)
print(R)
for x in sorted(R):
    print(x)
for i in Matrix:
    print(i)
print(R)
print(R)
R.sort()
R2=[R[i] for i in range(len(R)+1) if R[i+1].find(R[i])]
R2.sort()

print(R2)
