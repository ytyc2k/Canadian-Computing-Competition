'''
Fibonacci sequence
1,1,2,3,5,8,13,21,34, ......
'''

from time import time
T=time()
def fab(x):
    a,b = 0,1
    for _ in range(x):
      a,b=b,a+b
      yield a

for i in fab(10):
    print(i)