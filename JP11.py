# write a prgm to read & write into a file

while True:
    print("1 create file")
    print("2 write file")
    print("3 read file")
    print("4 exit")
    ch=int(input('enter your choice'))
    if ch==1:
        filename=input('enter filename to create')
        f=open(filename,'x')
        print('successfully',filename,'has created')
        f.close()
    elif ch==2:
        filename=input('enter filename to write')
        f=open(filename,'w')
        c=input('enter the content to write')
        f.write(c)
        print('content has been written successfully into  file',filename)
        f.close()
    elif ch==3:
        filename=input('enter filename to read')
        f=open(filename,'r')
        print('content of file is')
        print(f.read())
        f.close()
    elif ch==4:
        break
else:
    print('invalid choice')
    
    