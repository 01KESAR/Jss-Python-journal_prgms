# Write a python prgm to check if a given number is a prime or not

n=int(input('enter the number'))
i=2
while i<=n/2:
    if n%i==0:
        print("given number is not a prime number")
        break
    i+=1
else:
    print("given number is a prime number")
