# Write a Python Prgm to Solve Quadratic Equation

import math
a,b,c=input("enter 3 values").split() 
a=int(a)
b=int(b)
c=int(c)
if a==0:
    print('Incorrect equation')
else:
    d=b*b-4*a*c
    sq=math.sqrt(abs(d))
if d>0:
    print('real and different roots')
    s1=(-b+sq)/(2*a) 
    s2=(-b-sq)/(2*a)
    print(f'{s1:.2f}') 
    print(f'{s2:.2f}')        
elif d==0: 
    print('real & same roots') 
    s1=(-b/(2*a))
    print(f'{s1:.2f}')
else:
    print('complex roots')
    s1=-b/(2*a) 
    s2=sq/(2*a) 
    print(f'{s1:.2f}+i{s2:.2f}')
    print(f'{s1:.2f}-i{s2:.2f}')