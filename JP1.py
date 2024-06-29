# Write a Python Prgm check if a number belongs to fibonacci sequences 

n=int(input('enter the number'))
f1=f3=0
f2=1
while f3<=n:
    if f3==n:
        print(n,'belongs to fibonacci sequences')
        break
    f3=f1+f2
    f1=f2
    f2=f3
else:
    print(n,'does not belong to fibonacci sequences')   
