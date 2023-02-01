import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "bo1"
)





def addbook():
    bname = input("Enter book name: ")
    bcode = input("Enter book code:")
    total = input("Total books:")
    sub = input("Enter subject:")
    data = (bname,bcode,total,sub)
    sql = "insert into books(bname,bcode,total,subject) values(%s,%s,%s,%s)"
    c = mydb.cursor()
    c.execute(sql,data)
    mydb.commit()
    print(".............")
    print("Data entered successfully")
    main()


def issueb():
    name = input("Enter name:")
    rno  = input("Enter rno:")
    code = input("Enter book code:")
    date = input("Enter date:")
    sql  = "insert into issue(name,regno,bcode,idate) values(%s,%s,%s,%s)"
    data =(name,rno,code,date)
    c = mydb.cursor()
    c.execute(sql,data)
    mydb.commit()
    print("...............")
    print("Book issued to :",name)
    sql1 = "select * from books "
    da = (code)
    ci = mydb.cursor()
    #ci.execute(sql1,da)
    ci.execute(sql1)
    r=ci.fetchall()
    print(r)
    myresult = r[0]
    print(myresult)
    t= int(myresult[0])-1
    sql2 = "update books set TOTAL = %s where BCODE = %s"
    d = (t,code)
    ci.execute(sql2,d)
    mydb.commit()
    main()
    
    


def submitb():
    name = input("Enter name:")
    regno  = input("Enter rno:")
    code = input("Enter book code:")
    sdate = input("Enter date:")
    sql = "insert into submit(name,regno,bcode,sdate) values(%s,%s,%s,%s)"
    data = (name,regno,code,sdate)
    c = mydb.cursor()
    c.execute(sql,data)
    mydb.commit()
    print("...............")
    print("Book submitted from :",name)
    bookup(code,1)





def dbook():
    ac = input("Enter book code:")
    sql = "delete from books where BCODE = %s"
    data = (ac,)
    c = mydb.cursor()
    c.execute(sql,data)
    mydb.commit()
    main()


def dispbook():
    sql = "select * from books"
    c = mydb.cursor()
    c.execute(sql)
    myresult = c.fetchall()
    for i in myresult:
        print("Book name:",i[0])
        print("Book code:",i[1])
        print("Total:",i[2])
        print("................")
    main()


def main():
    print("""............LIBRARY MANAGEMENT.............
    1.Add book
    2.Issue book
    3.Submit book
    4.Delete book
    5.Display book
    """)
    choice = input("Enter task no:")
    print("............................")
    if(choice == '1'):
        addbook()
    elif(choice == '2'):
        issueb()
    elif(choice == '3'):
        submitb()
    elif(choice == '4'):
        dbook()
    elif(choice == '5'):
        dispbook()
    else:
        print("wrong choice")
        main()


def password():
    import random
    ps = random.randint(000000,100000)

    user = input("Enter Username: ")
    print("Your password is:",ps)

    verify = input("Enter password:")

    if verify == str(ps):
        main()
    else:
        verify != str(ps)
        print("wrong password")
        password()

main()