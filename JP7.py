# write a python prgm to create a calculator program

import math
while True:
    a=int(input('enter the first number'))
    b=int(input('enter the second number'))
    print('1.addition\n2.substraction\n3.multiplication\n4.true division\n5.exit')
    ch=int(input('enter your choice'))
    if ch==1:
        print(a,'+',b,'=',a+b)
    elif ch==2:
        print(a,'-',b,'=',a-b)
    elif ch==3:
        print(a,'*',b,'=',a*b)
    elif ch==4:
        print(a,'/',b,'=', a / b)
    elif ch==5:
        break
    else:
        print('invalid choice')