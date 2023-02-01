from tkinter import *
import mysql.connector as mcon
from tkinter import ttk

root = Tk()
root.geometry("1920x1080")
root.title("Blood donation")
con = mcon.connect(host="localhost", user="root", password="1234")
c = con.cursor()
c.execute("use carshowroom")

class donate:
    def __init__(self,name,location,group,x1,y1) -> None:
        self.name=name
        self.location=location
        self.group=group
        self.block_f=Frame(search_f,height=168,width=418)
        self.donate_b_i=PhotoImage(file = 'donate_b.png')
        self.block=Canvas(self.block_f,height=168,width=418)
        self.block.create_text(10, 10,text= 'name',font=('poppins',14,'normal'),fill='#C72542',anchor='nw')
        self.block.create_text(10, 35,text= self.name,font=('poppins',14,'normal'),fill='#C72542',anchor='nw')
        self.block.create_text(10, 70,text= 'Location :  '+self.location,font=('poppins',14,'normal'),fill='#C72542',anchor='nw')
        self.block.create_text(10, 95,text=self.location,font=('poppins',14,'normal'),fill='#C72542',anchor='nw')
        self.view_all_b = Button ( self.block,font=('poppins',18,'normal'),image=self.donate_b_i,text='VIEW ALL',command=donated,cursor='hand2',borderwidth = 0)
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

def dummy():
    print('hi')

def report():
    global intro1_f,donate_f,search_f,report_f,report_i,report_c,bp,op,abp,ap,bn,on,abn,an,report_home_i,report_report_i,report_search_i,report_user_i,report_home_b,report_search_b,report_report_b
    intro1_f.destroy()
    report_f.destroy()
    search_f.destroy()
    donate_f.destroy()
    report_i = PhotoImage(file = 'report.png')
    report_user_i = PhotoImage(file = 'user.png')
    report_search_i = PhotoImage(file = 'search.png')
    report_report_i = PhotoImage(file = 'report_b_r.png')
    report_home_i = PhotoImage(file = 'home.png')

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
    report_home_b=Button(report_c, image = report_home_i,borderwidth = 0,bg='#FFFFFF',command=dummy,cursor="hand2")
    report_home_b.place(x=61,y=114)
    report_search_b=Button(report_c, image = report_search_i,borderwidth = 0,bg='#FFFFFF',command=search,cursor="hand2")
    report_search_b.place(x=61,y=326)
    report_report_b=Button(report_c, image = report_report_i,borderwidth = 0,bg='#FFFFFF',command=report,cursor="hand2")
    report_report_b.place(x=61,y=731)
    report_user_b=Button(report_c, image = report_user_i,borderwidth = 0,bg='#FFFFFF',command=dummy,cursor="hand2")
    report_user_b.place(x=51,y=893)
    bp=10
    op=40
    abp=10
    ap=3
    bn=30
    on=40
    abn=10
    an=3
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
def submit():
    global o1,o2,o3,o4,o5,o6,donate_f
    donate_f.destroy()
    print(o1.get(),o2.get(),o3.get(),o4.get(),o5.get(),o6.get())
    report()
def search():
    global intro1_f,report_f,search_f,search_i,donations,search_home_i,search_report_i,search_search_i,search_user_i,donate_b_i,search_donate_direct_i,donate_f
    intro1_f.destroy()
    report_f.destroy()
    search_f.destroy()
    donate_f.destroy()
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
    c.execute("select * from donate")
    ls=c.fetchall()
    x=302
    y=204
    for d in ls:
        donations.append(donate(d[0],d[1],d[2],x,y))
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
    search_donate_b = Button ( block,font=('poppins',18,'normal'),image=donate_b_i,command=donated,cursor='hand2',borderwidth = 0)
    search_donate_b.place(x=180,y=130)
    block.pack(fill = "both")
    block_f.place(x=x,y=y)
    search_home_b=Button(search_c, image = search_home_i,borderwidth = 0,bg='#FFFFFF',command=dummy,cursor="hand2")
    search_home_b.place(x=61,y=114)
    search_search_b=Button(search_c, image = search_search_i,borderwidth = 0,bg='#FFFFFF',command=search,cursor="hand2")
    search_search_b.place(x=61,y=326)
    search_report_b=Button(search_c, image = search_report_i,borderwidth = 0,bg='#FFFFFF',command=report,cursor="hand2")
    search_report_b.place(x=61,y=731)
    search_user_b=Button(search_c, image = search_user_i,borderwidth = 0,bg='#FFFFFF',command=dummy,cursor="hand2")
    search_user_b.place(x=51,y=893)
def donated():
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
    donate_option4_cb.place(x=1056,y=364)
    donate_option5_cb=Checkbutton(donate_c, text = "Ingested alcohol in the past 48hrs?", 
                      variable = o5,
                      onvalue = 1,
                      offvalue = 0,
                      font=('poppins',20,'normal'),
                      height = 2,
                      width = 30,
                      activebackground='#FF2156',
                      bg='#FFFFFF')
    donate_option5_cb.place(x=356,y=464)
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
    insert_b = Button ( donate_c, width=10,height=1,font=('semi bold',24,'normal'),bg='#C72542',text='SUBMIT',fg='#FFFFFF',command=submit)
    insert_b.place(x=827,y=864)
    donate_user_i = PhotoImage(file = 'user.png')
    donate_search_i = PhotoImage(file = 'search.png')
    donate_report_i = PhotoImage(file = 'report_b.png')
    donate_home_i = PhotoImage(file = 'home.png')
    donate_home_b=Button(donate_c, image = donate_home_i,borderwidth = 0,bg='#FFFFFF',command=dummy,cursor="hand2")
    donate_home_b.place(x=61,y=114)
    donate_search_b=Button(donate_c, image = donate_search_i,borderwidth = 0,bg='#FFFFFF',command=search,cursor="hand2")
    donate_search_b.place(x=61,y=326)
    donate_report_b=Button(donate_c, image = donate_report_i,borderwidth = 0,bg='#FFFFFF',command=report,cursor="hand2")
    donate_report_b.place(x=61,y=731)
    donate_user_b=Button(donate_c, image = donate_user_i,borderwidth = 0,bg='#FFFFFF',command=dummy,cursor="hand2")
    donate_user_b.place(x=51,y=893)


intro1_i = PhotoImage(file = "intro.png")

donations=[]

intro1_f=Frame(root)
intro1_f.pack()
search_f=Frame(root)
report_f=Frame(root)
donate_f=Frame(root)


intro1_c=Canvas(intro1_f,height=1080,width=1920,bg='BLUE')
intro1_c.pack(fill = "both", expand = True)


intro1_login_b=Button(intro1_c, image = intro1_i,borderwidth = 0,command=search,cursor="hand2")
intro1_login_b.place(x=0,y=0)

root.mainloop()