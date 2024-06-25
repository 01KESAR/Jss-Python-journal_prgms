# write python prgm to Implement a sequential search

lst=[]
n=int(input('enter the limit'))
print('enter',n,'integers')
for i in range(n):
    e=int(input())
    lst.append(e)
k=int(input('enter the key to be searched'))
if k in lst:
    print('found')
else:
    print('not found')