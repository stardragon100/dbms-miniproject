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
    login_pa = Entry(login_c, width=15, font=('Poppins', 27, 'normal'),bg='#D6D6D6',bd=0,show='*')
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
        report()
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

class donate:
    def __init__(self,id,name,location,group,x1,y1) -> None:
        self.id=id
        self.name=name
        self.location=location
        self.group=group
        self.block_f=Frame(search_f,height=168,width=418)
        self.donate_b_i=PhotoImage(file = 'donate_b.png')
        self.block=Canvas(self.block_f,height=168,width=418)
        self.block.create_text(10, 10,text= 'name',font=('poppins',14,'normal'),fill='#7E7E7E',anchor='nw')
        self.block.create_text(10, 35,text= self.name,font=('poppins',14,'normal'),fill='#272A2F',anchor='nw')
        self.block.create_text(10, 70,text= 'Location :  ',font=('poppins',14,'normal'),fill='#7E7E7E',anchor='nw')
        self.block.create_text(10, 95,text=self.location,font=('poppins',14,'normal'),fill='#272A2F',anchor='nw')
        self.view_all_b = Button ( self.block,font=('poppins',18,'normal'),image=self.donate_b_i,text='VIEW ALL',command=lambda:donated(0,id),cursor='hand2',borderwidth = 0)
        self.view_all_b.place(x=320,y=130)
        str=group[0:-1]
        if(group[-1]=='+'):
            str=str+'P'
        else:
            str=str+'N'
        print(str)
        self.group_i=PhotoImage(file = str+'.png')
        self.block.create_image( 350, 20, image = self.group_i, anchor = "nw")
        self.block.pack(fill = "both")
        self.block_f.place(x=x1,y=y1)
    def clicked(self):
        print(self.name)
    def delete(self):
        self.block_f.destroy()

def report():
    global intro1_f,login_f,donate_f,search_f,report_f,report_i,report_c,bp,op,abp,ap,bn,on,abn,an,report_home_i,report_report_i,report_search_i,report_user_i,report_home_b,report_search_b,report_report_b
    intro1_f.destroy()
    login_f.destroy()
    report_f.destroy()
    search_f.destroy()
    request_f.destroy()
    donate_f.destroy()
    profile_f.destroy()
    report_i = PhotoImage(file = 'report.png')
    report_user_i = PhotoImage(file = 'user.png')
    report_search_i = PhotoImage(file = 'search.png')
    report_report_i = PhotoImage(file = 'report_b_r.png')
    report_home_i = PhotoImage(file = 'home.png')
    c.execute("select * from blood")
    ls=c.fetchall()
    report_f=Frame(root)
    report_f.pack()
    report_c=Canvas(report_f,height=1080,width=1920,bg='#FFFFFF')
    report_c.pack(fill = "both", expand = True)
    report_c.create_image( 0, 0, image = report_i, anchor = "nw")
    report_c.create_text(453,300,text= "B+",font=('poppins',36,'normal'), anchor = "nw")
    report_c.create_text(739,300,text= "O+",font=('poppins',36,'normal'), anchor = "nw")
    report_c.create_text(1015,300,text= "AB+",font=('poppins',36,'normal'), anchor = "nw")
    report_c.create_text(1308,300,text= "A+",font=('poppins',36,'normal'), anchor = "nw")
    report_c.create_text(453,573,text= "B-",font=('poppins',36,'normal'), anchor = "nw")
    report_c.create_text(739,573,text= "O-",font=('poppins',36,'normal'), anchor = "nw")
    report_c.create_text(1015,573,text= "AB-",font=('poppins',36,'normal'), anchor = "nw")
    report_c.create_text(1308,573,text= "A-",font=('poppins',36,'normal'), anchor = "nw")
    report_home_b=Button(report_c, image = report_home_i,borderwidth = 0,bg='#FFFFFF',command=request,cursor="hand2")
    report_home_b.place(x=61,y=114)
    report_search_b=Button(report_c, image = report_search_i,borderwidth = 0,bg='#FFFFFF',command=search,cursor="hand2")
    report_search_b.place(x=61,y=326)
    report_report_b=Button(report_c, image = report_report_i,borderwidth = 0,bg='#FFFFFF',command=report,cursor="hand2")
    report_report_b.place(x=61,y=731)
    report_user_b=Button(report_c, image = report_user_i,borderwidth = 0,bg='#FFFFFF',command=profile,cursor="hand2")
    report_user_b.place(x=51,y=893)
    bp=ls[5][1]
    op=ls[7][1]
    abp=ls[3][1]
    ap=ls[1][1]
    bn=ls[4][1]
    on=ls[6][1]
    abn=ls[2][1]
    an=ls[0][1]
    if(bp<=20):
        height=136
        width=256
        x=361
        y=378
        report_c.create_rectangle(x, y, x+width, y+height,outline = '#FF2929',width = 2)
        report_c.create_text(x+100,y+40,text= str(bp),font=('poppins',32,'normal'), anchor = "nw",fill='#FF2929')
    else:
        height=136
        width=256
        x=361
        y=378
        report_c.create_rectangle(x, y, x+width, y+height,outline = '#07B623',width = 2)
        report_c.create_text(x+100,y+40,text= str(bp),font=('poppins',32,'normal'), anchor = "nw",fill='#07B623')

    if(op<=20):
        height=136
        width=256
        x=645
        y=378
        report_c.create_rectangle(x, y, x+width, y+height,outline = '#FF2929',width = 2)
        report_c.create_text(x+100,y+40,text= str(op),font=('poppins',32,'normal'), anchor = "nw",fill='#FF2929')
    else:
        height=136
        width=256
        x=645
        y=378
        report_c.create_rectangle(x, y, x+width, y+height,outline = '#07B623',width = 2)
        report_c.create_text(x+100,y+40,text= str(op),font=('poppins',32,'normal'), anchor = "nw",fill='#07B623')

    if(abp<=20):
        height=136
        width=256
        x=928
        y=378
        report_c.create_rectangle(x, y, x+width, y+height,outline = '#FF2929',width = 2)
        report_c.create_text(x+100,y+40,text= str(abp),font=('poppins',32,'normal'), anchor = "nw",fill='#FF2929')
    else:
        height=136
        width=256
        x=928
        y=378
        report_c.create_rectangle(x, y, x+width, y+height,outline = '#07B623',width = 2)
        report_c.create_text(x+100,y+40,text= str(abp),font=('poppins',32,'normal'), anchor = "nw",fill='#07B623')

    if(ap<=20):
        height=136
        width=256
        x=1212
        y=378
        report_c.create_rectangle(x, y, x+width, y+height,outline = '#FF2929',width = 2)
        report_c.create_text(x+100,y+40,text= str(ap),font=('poppins',32,'normal'), anchor = "nw",fill='#FF2929')
    else:
        height=136
        width=256
        x=1212
        y=378
        report_c.create_rectangle(x, y, x+width, y+height,outline = '#07B623',width = 2)
        report_c.create_text(x+100,y+40,text= str(ap),font=('poppins',32,'normal'), anchor = "nw",fill='#07B623')

    if(bn<=20):
        height=136
        width=256
        x=361
        y=678
        report_c.create_rectangle(x, y, x+width, y+height,outline = '#FF2929',width = 2)
        report_c.create_text(x+100,y+40,text= str(bn),font=('poppins',32,'normal'), anchor = "nw",fill='#FF2929')
    else:
        height=136
        width=256
        x=361
        y=678
        report_c.create_rectangle(x, y, x+width, y+height,outline = '#07B623',width = 2)
        report_c.create_text(x+100,y+40,text= str(bn),font=('poppins',32,'normal'), anchor = "nw",fill='#07B623')

    if(on<=20):
        height=136
        width=256
        x=645
        y=678
        report_c.create_rectangle(x, y, x+width, y+height,outline = '#FF2929',width = 2)
        report_c.create_text(x+100,y+40,text= str(on),font=('poppins',32,'normal'), anchor = "nw",fill='#FF2929')
    else:
        height=136
        width=256
        x=645
        y=678
        report_c.create_rectangle(x, y, x+width, y+height,outline = '#07B623',width = 2)
        report_c.create_text(x+100,y+40,text= str(on),font=('poppins',32,'normal'), anchor = "nw",fill='#07B623')

    if(abn<=20):
        height=136
        width=256
        x=928
        y=678
        report_c.create_rectangle(x, y, x+width, y+height,outline = '#FF2929',width = 2)
        report_c.create_text(x+100,y+40,text= str(abn),font=('poppins',32,'normal'), anchor = "nw",fill='#FF2929')
    else:
        height=136
        width=256
        x=928
        y=678
        report_c.create_rectangle(x, y, x+width, y+height,outline = '#07B623',width = 2)
        report_c.create_text(x+100,y+40,text= str(abn),font=('poppins',32,'normal'), anchor = "nw",fill='#07B623')

    if(an<=20):
        height=136
        width=256
        x=1212
        y=678
        report_c.create_rectangle(x, y, x+width, y+height,outline = '#FF2929',width = 2)
        report_c.create_text(x+100,y+40,text= str(an),font=('poppins',32,'normal'), anchor = "nw",fill='#FF2929')
    else:
        height=136
        width=256
        x=1212
        y=678
        report_c.create_rectangle(x, y, x+width, y+height,outline = '#07B623',width = 2)
        report_c.create_text(x+100,y+40,text= str(an),font=('poppins',32,'normal'), anchor = "nw",fill='#07B623')
pid=1
def submit(x,y):
    global o1,o2,o3,o4,o5,o6,donate_f
    donate_f.destroy()
    c1=o1.get()
    c2=o2.get()
    c3=o3.get()
    c4=o4.get()
    c5=o5.get()
    c6=-o6.get()
    if(c2==1 or c3==1 or c5==1):
        tkinter.messagebox.showinfo("ERROR",  "Sorry you are not eligible to donate")
    elif(c4==1):
        tkinter.messagebox.showinfo("WAIT",  "Please wait for approval")
    else:
        if(x==0):
            c.execute("insert into donation values("+str(pid)+","+str(c1)+","+str(c2)+","+str(c3)+","+str(c4)+","+str(c5)+","+str(c6)+")")
            c.execute("delete from request where id="+str(y))
            con.commit()
        else:
            c.execute("insert into donation values("+str(pid)+","+str(c1)+","+str(c2)+","+str(c3)+","+str(c4)+","+str(c5)+","+str(c6)+")")
            c.execute("update blood set quantity=quantity + 1 where bloodtype='"+y+"'")
            con.commit()

        tkinter.messagebox.showinfo("SUCCESS",  "Procced with donation")
    report()
def search():
    global intro1_f,report_f,search_f,search_i,donations,search_home_i,search_report_i,search_search_i,search_user_i,donate_b_i,search_donate_direct_i,donate_f,name,profile_f
    intro1_f.destroy()
    login_f.destroy()
    report_f.destroy()
    search_f.destroy()
    request_f.destroy()
    donate_f.destroy()
    profile_f.destroy()
    search_f=Frame(root)
    search_i = PhotoImage(file = 'donate_bg.png')
    search_user_i = PhotoImage(file = 'user.png')
    search_search_i = PhotoImage(file = 'search_r.png')
    search_report_i = PhotoImage(file = 'report_b.png')
    search_home_i = PhotoImage(file = 'home.png')
    search_f.pack()
    search_c=Canvas(search_f,height=1080,width=1920,bg='#FFFFFF')
    search_c.pack(fill = "both", expand = True)
    search_c.create_image( 0, 0, image = search_i, anchor = "nw")
    for i in donations:
        i.delete()
    c.execute("select * from request")
    ls=c.fetchall()
    x=302
    y=204
    for d in ls:
        donations.append(donate(d[0],d[5],d[2],d[3],x,y))
        x=x+514
        print(d)
        if(x>=1660):
            x=302
            y=y+200
    block_f=Frame(search_f,height=168,width=418)
    donate_b_i=PhotoImage(file = 'donate_b.png')
    block=Canvas(block_f,height=168,width=418)
    search_donate_direct_i = PhotoImage(file = 'donate_direct.png')
    block.create_image( 0, 0, image = search_donate_direct_i, anchor = "nw")
    search_donate_b = Button ( block,font=('poppins',18,'normal'),image=donate_b_i,command=lambda:donated(1,bloodtype),cursor='hand2',borderwidth = 0)
    search_donate_b.place(x=180,y=130)
    block.pack(fill = "both")
    block_f.place(x=x,y=y)
    search_home_b=Button(search_c, image = search_home_i,borderwidth = 0,bg='#FFFFFF',command=request,cursor="hand2")
    search_home_b.place(x=61,y=114)
    search_search_b=Button(search_c, image = search_search_i,borderwidth = 0,bg='#FFFFFF',command=search,cursor="hand2")
    search_search_b.place(x=61,y=326)
    search_report_b=Button(search_c, image = search_report_i,borderwidth = 0,bg='#FFFFFF',command=report,cursor="hand2")
    search_report_b.place(x=61,y=731)
    search_user_b=Button(search_c, image = search_user_i,borderwidth = 0,bg='#FFFFFF',command=profile,cursor="hand2")
    search_user_b.place(x=51,y=893)
def donated(x,y):
    global donate_f,search_f,donate_b_i,o1,o2,o3,o4,o5,o6,donate_home_i,donate_report_i,donate_search_i,donate_user_i
    o1 = IntVar()
    o2 = IntVar()
    o3 = IntVar()
    o4 = IntVar()
    o5 = IntVar()
    o6 = IntVar()
    search_f.destroy()
    donate_b_i=PhotoImage(file = 'donate.png')
    donate_f=Frame(root)
    donate_f.pack()
    donate_c=Canvas(donate_f,height=1080,width=1920,bg='#FFFFFF')
    donate_c.pack(fill = "both", expand = True)
    donate_c.create_image( 0, 0, image = donate_b_i, anchor = "nw")
    donate_option1_cb=Checkbutton(donate_c, text = "Donated blood in the past ?", 
                      variable = o1,
                      onvalue = 1,
                      offvalue = 0,
                      font=('poppins',20,'normal'),
                      height = 2,
                      width = 22,
                      activebackground='#FF2156',
                      bg='#FFFFFF')
    donate_option1_cb.place(x=356,y=264)
    donate_option2_cb=Checkbutton(donate_c, text = "Are you pregnant or breast feeding?", 
                      variable = o2,
                      onvalue = 1,
                      offvalue = 0,
                      font=('poppins',20,'normal'),
                      height = 2,
                      width = 30,
                      activebackground='#FF2156',
                      bg='#FFFFFF')
    donate_option2_cb.place(x=1056,y=264)
    donate_option3_cb=Checkbutton(donate_c, text = "Had a meal or snack in the past 4 hrs?", 
                      variable = o3,
                      onvalue = 1,
                      offvalue = 0,
                      font=('poppins',20,'normal'),
                      height = 2,
                      width = 30,
                      activebackground='#FF2156',
                      bg='#FFFFFF')
    donate_option3_cb.place(x=356,y=364)
    donate_option4_cb=Checkbutton(donate_c, text = "Any previous record of diseases?\n(if yes please see the nurse)   ", 
                      variable = o4,
                      onvalue = 1,
                      offvalue = 0,
                      font=('poppins',20,'normal'),
                      height = 2,
                      width = 30,
                      activebackground='#FF2156',
                      bg='#FFFFFF')
    donate_option4_cb.place(x=1040,y=364)
    donate_option5_cb=Checkbutton(donate_c, text = "Ingested alcohol in the past 48hrs?", 
                      variable = o5,
                      onvalue = 1,
                      offvalue = 0,
                      font=('poppins',20,'normal'),
                      height = 2,
                      width = 30,
                      activebackground='#FF2156',
                      bg='#FFFFFF')
    donate_option5_cb.place(x=330,y=464)
    donate_option6_cb=Checkbutton(donate_c, text = "Travelled to a foreign country in the\npast month or year?", 
                      variable = o6,
                      onvalue = 1,
                      offvalue = 0,
                      font=('poppins',20,'normal'),
                      height = 2,
                      width = 30,
                      activebackground='#FF2156',
                      bg='#FFFFFF')
    donate_option6_cb.place(x=1056,y=464)
    insert_b = Button ( donate_c, width=10,height=1,font=('semi bold',24,'normal'),bg='#C72542',text='SUBMIT',fg='#FFFFFF',command=lambda:submit(x,y))
    insert_b.place(x=827,y=864)
    donate_user_i = PhotoImage(file = 'user.png')
    donate_search_i = PhotoImage(file = 'search.png')
    donate_report_i = PhotoImage(file = 'report_b.png')
    donate_home_i = PhotoImage(file = 'home.png')
    donate_home_b=Button(donate_c, image = donate_home_i,borderwidth = 0,bg='#FFFFFF',command=request,cursor="hand2")
    donate_home_b.place(x=61,y=114)
    donate_search_b=Button(donate_c, image = donate_search_i,borderwidth = 0,bg='#FFFFFF',command=search,cursor="hand2")
    donate_search_b.place(x=61,y=326)
    donate_report_b=Button(donate_c, image = donate_report_i,borderwidth = 0,bg='#FFFFFF',command=report,cursor="hand2")
    donate_report_b.place(x=61,y=731)
    donate_user_b=Button(donate_c, image = donate_user_i,borderwidth = 0,bg='#FFFFFF',command=profile,cursor="hand2")
    donate_user_b.place(x=51,y=893)
def request():
    global intro1_f,request_f,request_i,request_c,request_home_i,request_request_i,request_search_i,request_user_i,request_home_b,request_search_b,request_request_b,intro4_city_bi,intro4_city_b
    global request_b, request_i, request_f, request_c,request_city, request_bt, request_bt_i,request_city_i,request_button,request_ho,request_ph,request_bl,request_ad, request_ad_i,request_ph_i,request_ho_i,request_bl_i,city_i
    global login_f,report_f,search_f,donate_f,request_f
    login_f.destroy()
    report_f.destroy()
    search_f.destroy()
    request_f.destroy()
    donate_f.destroy()
    profile_f.destroy()
    request_i = PhotoImage(file = 'request_bg.png')
 
    request_user_i = PhotoImage(file = 'user.png')
    request_search_i = PhotoImage(file = 'search.png')
    request_request_i = PhotoImage(file = 'report_b.png')
    request_home_i = PhotoImage(file = 'home_r.png')


    request_f=Frame(root) 
    request_f.pack()
    request_c=Canvas(request_f,height=1080,width=1920,bg='#FFFFFF')
    request_c.pack(fill = "both", expand = True)
    request_c.create_image( 0, 0, image = request_i, anchor = "nw")


    request_home_b=Button(request_c, image = request_home_i,borderwidth = 0,bg='#FFFFFF',command=request,cursor="hand2")
    request_home_b.place(x=61,y=114)
    request_search_b=Button(request_c, image = request_search_i,borderwidth = 0,bg='#FFFFFF',command=search,cursor="hand2")
    request_search_b.place(x=61,y=326)
    request_request_b=Button(request_c, image = request_request_i,borderwidth = 0,bg='#FFFFFF',command=report,cursor="hand2")
    request_request_b.place(x=61,y=731)
    request_user_b=Button(request_c, image = request_user_i,borderwidth = 0,bg='#FFFFFF',command=profile,cursor="hand2")
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
def request_blood():
    global request_city,request_ho,request_bt,request_ph,pid
    s1=request_city.get()
    s2=request_ho.get()
    s3=request_bt.get()
    s4=request_ph.get()
    bg=s3
    if((bg=='B+' and bp==0) or (bg=='A+' and ap==0) or (bg=='O+' and op==0)or (bg=='AB+' and abp==0) or (bg=='B-' and bn==0) or (bg=='A-' and an==0) or (bg=='AB-' and abn==0) or (bg=='O-' and on==0)):
        c.execute("insert into request values("+str(pid)+",'"+s1+"','"+s2+"','"+s3+"','"+s4+"','"+name+"')")
        tkinter.messagebox.showinfo("WAIT",  "Your request has been added to the queue.")
        con.commit()
    else:
        c.execute("update blood set quantity=quantity - 1 where bloodtype='"+bg+"'")
        con.commit()
        tkinter.messagebox.showinfo("SUCCESS",  "Blood will be transferred.")
    report()
def profile():
    global intro4_f,profile_f,profile_bg_i,profile_user_i,profile_search_i,profile_report_i,profile_home_i,profile_profile_i,name,address
    intro4_f.destroy()
    login_f.destroy()
    report_f.destroy()
    search_f.destroy()
    request_f.destroy()
    donate_f.destroy()
    profile_f.destroy()
    profile_bg_i = PhotoImage(file = "profile_bg.png")
    profile_f=Frame(root)
    profile_f.pack()
    profile_c=Canvas(profile_f,height=1080,width=1920,bg='#FFFFFF')
    profile_c.create_image( 0, 0, image = profile_bg_i, anchor = "nw")
    profile_c.pack(fill = "both", expand = True)
    profile_user_i = PhotoImage(file = 'user_r.png')
    profile_search_i = PhotoImage(file = 'search.png')
    profile_report_i = PhotoImage(file = 'report_b.png')
    profile_home_i = PhotoImage(file = 'home.png')
    profile_profile_i = PhotoImage(file = 'profile_img.png')
    profile_home_b=Button(profile_c, image = profile_home_i,borderwidth = 0,bg='#FFFFFF',command=request,cursor="hand2")
    profile_home_b.place(x=61,y=114)
    profile_search_b=Button(profile_c, image = profile_search_i,borderwidth = 0,bg='#FFFFFF',command=search,cursor="hand2")
    profile_search_b.place(x=61,y=326)
    profile_report_b=Button(profile_c, image = profile_report_i,borderwidth = 0,bg='#FFFFFF',command=report,cursor="hand2")
    profile_report_b.place(x=61,y=731)
    profile_user_b=Button(profile_c, image = profile_user_i,borderwidth = 0,bg='#FFFFFF',command=profile,cursor="hand2")
    profile_user_b.place(x=51,y=893)
    profile_c.create_image(323 , 215, image = profile_profile_i, anchor = "nw")
    profile_c.create_text(700,260,text= name,font=('poppins',40,'normal'), anchor = "nw",fill='#FF2929')
    profile_c.create_text(700,339,text= address,font=('poppins',24,'normal'), anchor = "nw",fill='#FF2929')

donations=[]

intro1_i = PhotoImage(file = "intro.png")
intro1_f=Frame(root)
intro1_f.pack()
login_f = Frame(root)
search_f=Frame(root)
request_f=Frame(root) 
report_f=Frame(root)
register_f = Frame(root)
search_f=Frame(root)
report_f=Frame(root)
donate_f=Frame(root)
profile_f=Frame(root)
intro1_c=Canvas(intro1_f,height=1080,width=1920,bg='BLUE')
intro1_c.pack(fill = "both", expand = True)
intro1_login_b=Button(intro1_c, image = intro1_i,borderwidth = 0,command=intro2,cursor="hand2")
intro1_login_b.place(x=0,y=0)

root.mainloop()