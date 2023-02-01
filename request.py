from tkinter import *
import mysql.connector as mcon

root = Tk()
root.geometry("1920x1080")
root.title("Blood donation")

con = mcon.connect(host="localhost", user="root", password="1234")
c = con.cursor()
c.execute("use bloodbank")

def dummy():
    print('hi')

def request():
    global intro1_f,request_f,request_i,request_c,request_home_i,request_request_i,request_search_i,request_user_i,request_home_b,request_search_b,request_request_b,intro4_city_bi,intro4_city_b
    global request_b, request_i, request_f, request_c,request_city, request_bt, request_bt_i,request_city_i,request_button,request_ho,request_ph,request_bl,request_ad, request_ad_i,request_ph_i,request_ho_i,request_bl_i,city_i

    intro1_f.destroy()
    request_i = PhotoImage(file = 'request_bg.png')
 
    request_user_i = PhotoImage(file = 'user.png')
    request_search_i = PhotoImage(file = 'search.png')
    request_request_i = PhotoImage(file = 'report_b.png')
    request_home_i = PhotoImage(file = 'home.png')


    request_f=Frame(root) 
    request_f.pack()
    request_c=Canvas(request_f,height=1080,width=1920,bg='#FFFFFF')
    request_c.pack(fill = "both", expand = True)
    request_c.create_image( 0, 0, image = request_i, anchor = "nw")


    request_home_b=Button(request_c, image = request_home_i,borderwidth = 0,bg='#FFFFFF',command=dummy,cursor="hand2")
    request_home_b.place(x=61,y=114)
    request_search_b=Button(request_c, image = request_search_i,borderwidth = 0,bg='#FFFFFF',command=dummy,cursor="hand2")
    request_search_b.place(x=61,y=326)
    request_request_b=Button(request_c, image = request_request_i,borderwidth = 0,bg='#FFFFFF',command=dummy,cursor="hand2")
    request_request_b.place(x=61,y=731)
    request_user_b=Button(request_c, image = request_user_i,borderwidth = 0,bg='#FFFFFF',command=dummy,cursor="hand2")
    request_user_b.place(x=51,y=893)


    
    
    request_city = Entry(request_c,width=15, font=('Poppins', 27, 'normal'), bg='#D6D6D6', bd=0)
    request_city.place(x=810, y=319.2)
    request_city.insert(0,"City")
    request_ho = Entry(request_c, width=15, font=('Poppins', 27, 'normal'), bg='#D6D6D6', bd=0)
    request_ho.place(x=810, y=396.2)
    request_ho.insert(0,"Hospital")
    request_bt = Entry(request_c, width=15, font=('Poppins', 27, 'normal'), bg='#D6D6D6', bd=0)
    request_bt.place(x=810, y=473.2)
    request_bt.insert(0,"Blood Type")
    request_ph = Entry(request_c, width=15, font=('Poppins', 27, 'normal'), bg='#D6D6D6', bd=0)
    request_ph.place(x=810, y=551.2)
    request_ph.insert(0,"Mobile")
   
    request_city_i = PhotoImage(file="address.png")
    request_c.create_image(770, 326, image=request_city_i, anchor="nw")
    request_ho_i = PhotoImage(file="la_city.png")
    request_c.create_image(770, 403, image=request_ho_i, anchor="nw")
    request_bt_i = PhotoImage(file="blood.png")
    request_c.create_image(770, 480, image=request_bt_i, anchor="nw")
    request_ph_i = PhotoImage(file="phone.png")
    request_c.create_image(770, 558, image=request_ph_i, anchor="nw")


   


    request_b = PhotoImage(file="request_bi.png")
    request_button = Button(request_c, image=request_b, borderwidth=0, command=request_blood, bg='#FFFFFF', text='REQUEST', cursor="hand2")
    request_button.place(x=830, y=705)
pno=5
def request_blood():
    global request_city,request_ho,request_bt,request_ph
    s1=request_city.get()
    s2=request_ho.get()
    s3=request_bt.get()
    s4=request_ph.get()
    c.execute("insert into request values("+str(pno)+",'"+s1+"','"+s2+"','"+s3+"','"+s4+"')")
    con.commit()

def search():
        global intro1_f,request_f,request_i,request_c,bp,op,abp,ap,bn,on,abn,an,request_home_i,request_request_i,request_search_i,request_user_i,request_home_b,request_search_b,request_request_b
        intro1_f.destroy()  

intro1_i = PhotoImage(file = "intro.png")


intro1_f=Frame(root)
intro1_f.pack()


intro1_c=Canvas(intro1_f,height=1080,width=1920,bg='BLUE')
intro1_c.pack(fill = "both", expand = True)


intro1_login_b=Button(intro1_c, image = intro1_i,borderwidth = 0,command=request ,cursor="hand2")
intro1_login_b.place(x=0,y=0)

root.mainloop()
