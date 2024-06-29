# write python prgm to implement selection sort

n=int(input('enter the no of elements to be stored'))
a=[]
print('enter the elements')
for i in range(n):
    e=int(input())
    a.append(e)
for i in range(n-1):
    min=i
    for j in range(i+1,n):
        if a[j]<a[min]:
            min=j
    if i!=min:
        a[i],a[min]=a[min],a[i]
print('sorted array')
print(a)