n=int(input())
lst=sorted([int(input()) for i in range(n)])
# lst=[0, 4, 10, 15, 16]
lst1=[(lst[i+1]-lst[i])/2 for i in range(len(lst)-1)]
lst2=[lst1[i+1]+lst1[i] for i in range(len(lst1)-1)]
print(min(lst2))
