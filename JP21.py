# write a python prgm create an array using numpy and perform operations on array.

import numpy as np
a=np.array([1,2,3,4,5])
b=np.array([6,7,8,9,10])
print('array a is',a)
print('array b is',b)
print('length of an array a is=',len(a))
print('type of array a is =',type(a))
print('array b is ',b.ndim,'dimensional array')
print('sum of array a and b is',a+b)
print('add 1 to all elements of a ',a+1)
print('minimum element in an array a is ',a.min())
print('maximum element in an array b is ',b.max())
print('index of element 4 in a is',np.where(a==4))