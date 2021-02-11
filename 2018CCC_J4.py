'''
input:
3
3 7 9
2 5 6
1 3 4

'''

# n=int(input())
# lst_in=[[int(j) for j in input().split()] for i in range(n)]
lst_in=[
    [3, 7, 9],
    [2, 5, 6],
    [1, 3, 4]]
print(lst_in)

top=lst_in
right=[[row[i] for row in lst_in] for i in range(2,-1,-1)]
bottom=lst_in[::-1]
left=[[row[i] for row in lst_in[::-1]] for i in range(3)]
min=min([top[0],right[0],bottom[0],left[0]])
if min==top[0]:
    pass
elif min==right[0]:
    lst_in=right
elif min==bottom[0]:
    lst_in=bottom
elif min==left[0]:
    lst_in=left
for x in lst_in:
    for j in x:
        print(j,end=' ')
    print('')
