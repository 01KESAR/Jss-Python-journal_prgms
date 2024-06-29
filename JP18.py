# write a python prgm to demonstrate exceptions in python

import sys
try:
    a=int(sys.argv[1])
    b=int(sys.argv[2])
    c=a/b
    print("c=",c)
except ZeroDivisionError:
    print('cannot divide by zero')
except IndexError:
    print('provide enough values')
except ValueError:
    print('invalid values')
print('end of program')