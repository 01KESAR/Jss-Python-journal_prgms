# write a python prgm demonstrate use of list

print("demonstrating list operations")
lst=[10,20,30,10,50,60,70]
print('elements of the list are',lst)
print('length of the list is',len(lst))
print('elements from 3rd to 5th index',lst[3:6])
print('add the value 80 at the end of the list')
lst.append(80)
print('updated list is',lst)
print('no of occurances of element 10 in a list is',lst.count(10))
print('removing topmost element in the list',lst.pop())
print('updated list is',lst)
lst.sort()
print('sorted list is',lst)
del(lst[3:6])
print('after deleting elements from 3rd to 5th index',lst)