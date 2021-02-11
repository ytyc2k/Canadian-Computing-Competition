'''
input:
3 10 12 5
'''
ss='0 '+input()
lst=[int(i) for i in ss.split()]
lst1=[sum(lst[:i+1]) for i in range(len(lst))]
print(lst1)
for i in lst1:
    for j in lst1:
        print(abs(j-i),end=' ')
    print('')