# Write a Python Prgm to find the sum of n natural numbers

n=int(input("enter the limit"))
s=0
i=1
while i<=n:
    s=s+i
    i+=1
    print(f'sum of first {n} numbers={s}')
    
    
    