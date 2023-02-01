from tkinter import *
import mysql.connector as mcon
import tkinter.messagebox
root = Tk()
root.geometry("1920x1080")
root.title("Blood donation")

con = mcon.connect(host="localhost", user="root", password="1234")
c = con.cursor()
c.execute("use bloodbank")

def login():
    global login_b,login_i,login_f,login_c,login_na,login_pa,login_pa_i,login_na_i,register_f
    register_f.destroy()
    intro4_f.destroy()
    login_i=PhotoImage(file = "login_page.png")
    login_f = Frame(root)
    login_f.pack()
    login_c = Canvas(login_f, height=1080, width=1920)
    login_c.create_image(0, 0, image=login_i, anchor="nw")
    login_c.pack(fill="both", expand=True)
    login_na = Entry(login_c, width=15, font=('Poppins', 27, 'normal'),bg='#D6D6D6',bd=0)
    login_na.place(x=820, y=449)
    login_na_i = PhotoImage(file="mail.png")
    login_c.create_image(785, 456, image=login_na_i, anchor="nw")
    login_pa = Entry(login_c, width=15, font=('Poppins', 27, 'normal'),bg='#D6D6D6',bd=0)
    login_pa.place(x=820, y=540)
    
    login_pa_i = PhotoImage(file="password.png")
    login_c.create_image(785, 548, image=login_pa_i, anchor="nw")
    login_b = PhotoImage(file="login_b2.png")
    login_button = Button(login_c, image=login_b, borderwidth=0, command=login_sql, bg='#FFFFFF',text='LOGIN',cursor="hand2")
    login_button.place(x=773, y=684)

def login_sql():
    global user_name,password,pid,name,mail,password,phoneno,bloodtype,address
    password=login_pa.get()
    user_name=login_na.get()
    print(user_name,password)
    c.execute("select * from user where mail='"+user_name+"' and password='"+password+"'")
    ls=c.fetchall()
    if(len(ls)!=0):
        pid=ls[0][0]
        name=ls[0][1]
        mail=ls[0][2]
        password=ls[0][3]
        phoneno=ls[0][4]
        bloodtype=ls[0][5]
        address=ls[0][6]
        print('login successful')
    else:
        tkinter.messagebox.showinfo("ERROR",  "Incorrect credentials")
    print(ls)
def register_sql():
    global register_na, register_pa,register_ma,register_ph,register_bl,register_ad,name,mail,password,phoneno,bloodtype,address
    name=register_na.get()
    mail=register_ma.get()
    password=register_pa.get()
    phoneno=register_ph.get()
    bloodtype=register_bl.get()
    address=register_ad.get()
    str="Insert into user (name,mail,password,phoneno,bloodtype,address) values('"+name+"','"+mail+"','"+password+"','"+phoneno+"','"+bloodtype+"','"+address+"')"
    c.execute(str)
    con.commit()
    login()
def register():
    global register_b, register_i, register_f, register_c, register_na, register_pa, register_pa_i, register_na_i,register_button,register_ma,register_ph,register_bl,register_ad, register_ad_i,register_ph_i,register_ma_i,register_bl_i
    intro4_f.destroy()
    register_i = PhotoImage(file="register_page.png")
    register_f = Frame(root)
    register_f.pack()
    register_c = Canvas(register_f, height=1080, width=1920)
    register_c.create_image(0, 0, image=register_i, anchor="nw")
    register_c.pack(fill="both", expand=True)
    register_na = Entry(register_c, width=15, font=('Poppins', 27, 'normal'), bg='#D6D6D6', bd=0)
    register_na.place(x=810, y=319.2)
    register_ma = Entry(register_c, width=15, font=('Poppins', 27, 'normal'), bg='#D6D6D6', bd=0)
    register_ma.place(x=810, y=396.2)
    register_pa = Entry(register_c, width=15, font=('Poppins', 27, 'normal'), bg='#D6D6D6', bd=0)
    register_pa.place(x=810, y=473.2)
    register_ph = Entry(register_c, width=15, font=('Poppins', 27, 'normal'), bg='#D6D6D6', bd=0)
    register_ph.place(x=810, y=551.2)
    register_bl = Entry(register_c, width=15, font=('Poppins', 27, 'normal'), bg='#D6D6D6', bd=0)
    register_bl.place(x=810, y=628.2)
    register_ad = Entry(register_c, width=15, font=('Poppins', 27, 'normal'), bg='#D6D6D6', bd=0)
    register_ad.place(x=810, y=705.2)

    register_na_i = PhotoImage(file="person.png")
    register_c.create_image(780, 319, image=register_na_i, anchor="nw")
    register_ma_i = PhotoImage(file="mail.png")
    register_c.create_image(780, 396, image=register_ma_i, anchor="nw")
    register_pa_i = PhotoImage(file="password.png")
    register_c.create_image(780, 473, image=register_pa_i, anchor="nw")
    register_ph_i = PhotoImage(file="phone.png")
    register_c.create_image(780, 551, image=register_ph_i, anchor="nw")
    register_bl_i = PhotoImage(file="blood.png")
    register_c.create_image(780, 628, image=register_bl_i, anchor="nw")
    register_ad_i = PhotoImage(file="address.png")
    register_c.create_image(780, 705, image=register_ad_i, anchor="nw")

    register_b = PhotoImage(file="register_b.png")
    register_button = Button(register_c, image=register_b, borderwidth=0, command=register_sql, bg='#FFFFFF', text='LOGIN', cursor="hand2")
    register_button.place(x=762, y=817)

def dummy():
    print('clicked')

def intro3():
    global intro3_i,intro3_f,intro3_ne,intro3_sk,intro3_c
    intro2_f.destroy()
    intro3_i=PhotoImage(file="intro3.png")
    intro3_f = Frame(root)
    intro3_f.pack()
    intro3_c = Canvas(intro3_f, height=1080, width=1920)
    intro3_c.create_image(0, 0, image=intro3_i, anchor="nw")
    intro3_c.pack(fill="both", expand=True)

    def sk1(event=None):
        print('clicked1')
        intro3_f.destroy()
        intro4()
    def sk2(event=None):
        intro3_sk.config(fg='blue')
    def sk3(event=None):
        intro3_sk.config(fg='#3A4351')
    def ne1(event=None):
        print('clicked2')
        intro3_f.destroy()
        intro4()
    def ne2(event=None):
        intro3_ne.config(fg='blue')
    def ne3(event=None):
        intro3_ne.config(fg='red')

    intro3_ne = Label(intro3_c, bg='#FFFFFF', fg='red', text='Next', cursor="hand2", font=('semi bold', 40, 'normal'))
    intro3_ne.place(x=1477, y=600)
    intro3_ne.bind("<Button-1>", ne1)
    intro3_ne.bind("<Enter>", ne2)
    intro3_ne.bind("<Leave>", ne3)

    intro3_sk = Label(intro3_c, bg='#FFFFFF', fg='#3A4351', text='Skip', cursor="hand2", font=('semi bold', 40, 'normal'))
    intro3_sk.place(x=864, y=603)
    intro3_sk.bind("<Button-1>", sk1)
    intro3_sk.bind("<Enter>", sk2)
    intro3_sk.bind("<Leave>", sk3)


def intro2():
    global intro2_i,intro2_f,intro2_ne,intro2_sk,intro2_c
    intro1_f.destroy()
    intro2_i=PhotoImage(file="intro2.png")
    intro2_f = Frame(root)
    intro2_f.pack()
    intro2_c = Canvas(intro2_f, height=1080, width=1920)
    intro2_c.create_image(0, 0, image=intro2_i, anchor="nw")
    intro2_c.pack(fill="both", expand=True)

    def sk1(event=None):
        print('clicked1')
        intro2_f.destroy()
        intro4()
    def sk2(event=None):
        intro2_sk.config(fg='blue')
    def sk3(event=None):
        intro2_sk.config(fg='#3A4351')
    def ne1(event=None):
        print('clicked2')
        intro3()
    def ne2(event=None):
        intro2_ne.config(fg='blue')
    def ne3(event=None):
        intro2_ne.config(fg='red')

    intro2_ne = Label(intro2_c, bg='#FFFFFF', fg='red', text='Next', cursor="hand2", font=('semi bold', 40, 'normal'))
    intro2_ne.place(x=802, y=615)
    intro2_ne.bind("<Button-1>", ne1)
    intro2_ne.bind("<Enter>", ne2)
    intro2_ne.bind("<Leave>", ne3)

    intro2_sk = Label(intro2_c, bg='#FFFFFF', fg='#3A4351', text='Skip', cursor="hand2", font=('semi bold', 40, 'normal'))
    intro2_sk.place(x=189, y=618)
    intro2_sk.bind("<Button-1>", sk1)
    intro2_sk.bind("<Enter>", sk2)
    intro2_sk.bind("<Leave>", sk3)

def intro4():
    global intro1_f,intro4_i,intro4_f,intro4_login_bi,intro4_login_ri,intro4_c,intro4_login_b,intro4_login_r
    print('hi')

    intro4_i = PhotoImage(file = "intro4.png")
    intro4_login_bi = PhotoImage(file = "login_b.png")
    intro4_login_ri = PhotoImage(file = "register_b.png")

    intro4_f=Frame(root)
    intro4_f.pack()
    intro4_c=Canvas(intro4_f,height=1080,width=1920)
    intro4_c.create_image( 0, 0, image = intro4_i, anchor = "nw")
    intro4_c.pack(fill = "both", expand = True)
    intro4_login_b=Button(intro4_c, image = intro4_login_bi,borderwidth = 0,bg='#FFFFFF',command=login,cursor="hand2")
    intro4_login_b.place(x=172,y=585)
    intro4_login_r=Button(intro4_c, image = intro4_login_ri,borderwidth = 0,bg='#FFFFFF',command=register,cursor="hand2")
    intro4_login_r.place(x=172,y=666)

def profile():
    global intro4_f
    intro4_f.destroy()

    profile_bg_i = PhotoImage(file = "profile_bg.png")
    profile_f=Frame(root)
    profile_f.pack()
    profile_c=Canvas(profile_f,height=1080,width=1920)
    profile_c.create_image( 0, 0, image = profile_bg_i, anchor = "nw")
    profile_c.pack(fill = "both", expand = True)
    profile_user_i = PhotoImage(file = 'user.png')
    profile_search_i = PhotoImage(file = 'search_r.png')
    profile_report_i = PhotoImage(file = 'report_b.png')
    profile_home_i = PhotoImage(file = 'home.png')
    profile_home_b=Button(profile_c, image = profile_home_i,borderwidth = 0,bg='#FFFFFF',command=request,cursor="hand2")
    profile_home_b.place(x=61,y=114)
    profile_search_b=Button(profile_c, image = profile_search_i,borderwidth = 0,bg='#FFFFFF',command=search,cursor="hand2")
    profile_search_b.place(x=61,y=326)
    profile_report_b=Button(profile_c, image = profile_report_i,borderwidth = 0,bg='#FFFFFF',command=report,cursor="hand2")
    profile_report_b.place(x=61,y=731)
    profile_user_b=Button(profile_c, image = profile_user_i,borderwidth = 0,bg='#FFFFFF',command=dummy,cursor="hand2")
    profile_user_b.place(x=51,y=893)



intro1_i = PhotoImage(file = "intro.png")
intro1_f=Frame(root)
intro1_f.pack()
login_f = Frame(root)
register_f = Frame(root)
intro1_c=Canvas(intro1_f,height=1080,width=1920,bg='BLUE')
intro1_c.pack(fill = "both", expand = True)
intro1_login_b=Button(intro1_c, image = intro1_i,borderwidth = 0,command=intro2,cursor="hand2")
intro1_login_b.place(x=0,y=0)

root.mainloop()