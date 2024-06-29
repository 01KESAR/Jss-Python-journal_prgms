# write a python prgmn for stack implementation
stk=[]
n=int(input('enter the size of the stack'))
while True:
    print('1 for push opeartion\n 2 for pop opeartion\n 3 for display\n 4 for exit\n')
    ch=int(input('enter your choice'))
    if ch==1:
        if len(stk)==n:
            print('stack is full')
        else:
         e=int(input('element to be inserted'))
         stk.append(e)
    elif ch==2:
         if not stk:
             print('stack is empty')
         else:
             print('element deleted from stack is',stk.pop())
    elif ch==3:
         if not stk:
             print('stack is empty')
         else:
             print('stack elements are')
             print(stk[::-1])
             
    elif ch==4:
          break
    else:
        print('invalid choice')
