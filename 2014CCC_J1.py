# 2020-2-2 12:43pm
# 2020-2-2 12:55pm
'''
Sample Input 1
60
70
50

Output for Sample Input 1
Scalene
'''
a = int(input())
b = int(input())
c = int(input())
if a + b + c == 180:
    if a == b and b == c:
        print('Equilateral')
    elif a == b or b == c or c == a:
        print('Isosceles')
    elif a != b and b != c and c != a:
        print('Scalene')
else:
    print('Error')


