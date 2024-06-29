# write a python prgm Demonstrate usage of basic regular expression

import re
txt="Python Programming Language3"
if re.search('Program',txt):
    print('program is found in ',txt)
else:
    print('program is not found in ', txt)
if re.search('^Python',txt):
    print(txt,'text starts with the word Python')
else:
    print(txt, 'text does not start with the word Python')
if re.search('Language$',txt):
    print(txt, 'text ends with the word Language')
else:
    print(txt, 'text does not end with the word Language')
if re.search('^[A-Z]',txt):
    print("first charcter in the line",txt,'is capital letter')
else:
    print("first charcter in the line", txt, 'is not capital letter')
if re.search('\d',txt):
    print('number is found in',txt)
else:
    print('number is not found in',txt)