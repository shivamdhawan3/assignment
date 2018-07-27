  Assignment-19
                ------------------


Q.1 Create a database. Create the following tables:
#1. Book
#2. Titles
#3. Publishers
#4. Zipcodes
#5. AuthorsTitles
#6. Authors

Q.2- Insert values in the tables.

Q.3- Update any values in any of the tables. Print the original and updated values.


import pymysql as pm
try:
    con=pm.connect(host="localhost",database="user",user="root",password="123456")
    print("connection done")
    cursor=con.cursor()
    query="create table book07(book_id int(10) primary key,title_id int(10),location varchar(10),genre varchar(10))"
    cursor.execute(query)
    query1="create table titles07(title_id int(10) primary key, title varchar(10),isbn int(10),publisher_id int(10),publisher_year int(10))"
    cursor.execute(query1)
    query2="create table publishers07(publisher_id int(10) primary key,name varchar(10),street_add varchar(10),state_no int(10),zipcode_id int(10))"
    cursor.execute(query2)
    query3="create table zipcodes07(zip_code_id int(10) primary key,city varchar(10),state varchar(10),zip_code int(10))"
    cursor.execute(query3)
    query4="create table author_titles07(author_title_id int(10) primary key,author_id int(10),title_id int(10))"
    cursor.execute(query4)
    query5="create table authors07(author_id int(10) primary key,first_name varchar(10),middle_name varchar(10),last_name varchar(10))"
    cursor.execute(query5)
    query6="insert into book07 values(1,1,'x1','horror')"
    cursor.execute(query6)
    query7="insert into titles07 values(1,'y',1234,2,1998)"
    cursor.execute(query7)
    query8="insert into publishers07 values(1,'abc','street',37,456)"
    cursor.execute(query8)
    query9="insert into zipcodes07 values(1,'xyz','abc',238)"
    cursor.execute(query9)
    query10="insert into author_titles07 values(1,2,3)"
    cursor.execute(query10)
    query11="insert into authors07 values(1,'shubham','ankit','sharma')"
    cursor.execute(query11)
    print("table created")
    print("values inserted")
    query12="select * from authors07"
    cursor.execute(query12)
    data=cursor.fetchall()
    for row in data:
        print("id:{},first name:{},middle name:{},last name:{}".format(row[0],row[1],row[2],row[3]))
    query13="update authors07 set last_name='sanyal' where author_id=1"
    cursor.execute(query13)
    query="select * from authors07"
    cursor.execute(query)
    data1=cursor.fetchall()
    for row1 in data1:
        print("id:{},first name:{},middle name:{},last name:{}".format(row1[0],row1[1],row1[2],row1[3]))
    print("table updated")
    con.commit()

except pm.DatabaseError as e:
    if con:
        con.rollback()
        print(e)

finally:
    cursor.close()
    con.close()