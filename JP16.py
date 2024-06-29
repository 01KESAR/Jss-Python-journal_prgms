# write a python prgm create SQLite Database & Perform Operations on tables

import sqlite3
con=sqlite3.connect('sample.db')
cur=con.cursor()
tn=input('enter the table name')
print("table created successfully")
cur.execute("CREATE TABLE "+tn+"(name VARCHAR(25));")
while True:
    print("sqlite3 transactions")
    print("1. insert record\n2.delete record\n3.update record\n4.display\n5.exit\n")
    ch=int(input('enter your choice'))
    if ch==1:
           n=input("enter the student name to be inserted")
           cur.execute("insert into "+tn+" values('"+n+"');")
           print('record inserted successfully')
    elif ch==2:
           n=input("enter the record name to be deleted")
           cur.execute("delete from "+tn+" where name='"+n+"';")
           print("record deleted successfully")
    elif ch==3:
            old_n=input("enter the  name to be changed")
            new_n=input("enter the  new name to be stored")
            cur.execute("update "+tn+" set name='"+new_n+"' where name='"+old_n+"';")
    elif ch==4:
            d=cur.execute("select * from "+tn+";")
            print(d)
            for i in d.fetchall():
                 print(i)
    elif ch==5:
           break
    else:
         print("invalid choice")
    con.commit()
con.close()