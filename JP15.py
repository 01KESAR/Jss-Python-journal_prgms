# write a python prgm demonstrate use of dictionary

stud={'name':'aaa','course':'bca','regno':100}
print('student details=',stud)
print('regno of the student=',stud['regno'])
stud['course']='bsc' # changing the course name
print('after changing course name  dictionary is ')
print(stud)
print("adding new key:value pair to list")
stud['address']='dharwad'
print(stud)
print('removing last item from the dictionary=',stud.popitem())
print('updated dictionary is ')
for k,v in stud.items():
    print(k,v)
print('after removing ',stud.pop('course'))
print(stud)