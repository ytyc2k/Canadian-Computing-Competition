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

Stack=[(4,1)]
while Stack:
    x,y=Stack.pop(0)
    if Matrix[x][y] in 'w0':
        continue
    Matrix[x][y] = '0'
    Stack.append((x-1,y))
    Stack.append((x+1,y))
    Stack.append((x,y-1))
    Stack.append((x,y+1))

for i in Matrix:
    print(i)



