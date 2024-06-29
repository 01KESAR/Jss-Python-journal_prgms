# write a python prgm to Demonstrate use of advanced regular expressions for data validation

import re
while True:
    print('1 for mobile number validation')
    print('2 for email id validation')
    print('3 for strong password validation')
    print('4 for exit')
    ch=int(input('enter your choice'))
    if ch==1:
        mb=input('enter the mobile number')
        if re.search('^[6789][0-9]{9}$',mb):
            print('valid mobile no')
        else:
            print('invalid mobile number')
    elif ch==2:
        mid=input('enter the email id')
        if re.search('^[A-Za-z0-9]{3,6}[@][A-Za-z].*[.][A-Za-z]{3}$',mid):
            print('valid Email ID')
        else:
            print('invalid Email ID')
    elif ch==3:
        psw = input('enter the password')
        pattern = r"^(?=.\d)(?=.[a-z])(?=.[A-Z])(?=.[!@#$%^&*?+-/]).{8,}$"
        if re.search(pattern, psw):
            print('valid password')
        else:
            print('invalid password')
    else:
        print('invalid choice')