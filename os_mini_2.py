import mysql.connector as mcon
import os
from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
import glob
import shutil

con = mcon.connect(host="localhost", user="root", password="1234")
c = con.cursor()
c.execute("use carshowroom")

class cars:
    def __init__(self,name,type,year,price,x1,y1) -> None:
        self.block_f=Frame(interior,height=800,width=408,bg='#444444')
        self.car_image = PhotoImage(file = name+".png")
        self.block=Canvas(self.block_f,bg='#fafafa',height=500,width=408)
        self.name=name
        self.type=type
        self.year=year
        self.price=price
        self.block.create_image( 0, 0, image = self.car_image, anchor = "nw")
        self.block.create_text(210, 260,text= self.name,font=('bold',40,'normal'),fill='#C72542')
        self.block.create_text(100, 305,text= 'type :  '+self.type,font=('semi bold',20,'normal'),fill='#C72542',anchor='nw')
        self.block.create_text(100, 340,text= 'year :  '+str(self.year),font=('semi bold',20,'normal'),fill='#C72542',anchor='nw')
        self.block.create_text(100, 370,text= 'price:  '+str(self.price),font=('semi bold',20,'normal'),fill='#C72542',anchor='nw')
        self.block.pack(fill = "both")
        self.block_f.place(x=x1,y=y1)
    def delete(self):
        self.block_f.destroy()

user_name=''
def login_check():
    global user_name
    user_name=name_e.get()
    password=password_e.get()
    interior.create_text(240, 95,text= "WELCOME",font=('semi bold',25,'normal'),fill='#C72542')
    interior.create_text(180, 125,text= user_name,font=('semi bold',25,'normal'),fill='#C72542')
    c.execute("select * from login where name='"+user_name+"'and password='"+password+"'")
    d=c.fetchall()
    if(len(d)!=0):
        print('login successful')
        login_f.destroy()
        interior.pack(fill = "both", expand = True)
    else:
        tkinter.messagebox.showinfo("ERROR",  "Incorrect credentials")
        print('login unsuccessful')

def view_all():
    for i in car:
        i.delete()
    c.execute("select * from cars")
    ls=c.fetchall()
    x=75
    y=350
    for d in ls:
        car.append(cars(d[0],d[1],d[2],d[3],x,y))
        x=x+450
        print(d)
        if(x>=1875):
            x=75
            y=y+520

def view():
    for i in car:
        i.delete()
    name=name_ei.get()
    c.execute("select * from cars where name='"+name+"'")
    d=c.fetchall()
    car.append(cars(d[0][0],d[0][1],d[0][2],d[0][3],75,350))


def user():
    return user_name

def insert():
    global user_name
    global name_ei2,type_e,year_e,price_e,color_e,loc_e,path_b,insertion_f,insertion
    insertion_f=Frame(root)
    insertion_f.pack()
    insertion=Canvas(insertion_f,height=1080,width=1920,bg='#171717')
    insertion.pack(fill = "both", expand = True)
    insertion.create_image( 75, 75, image = user_icon, anchor = "nw")
    interior_f.destroy()
    insertion_f.pack()
    insertion.create_image( 75, 75, image = user_icon, anchor = "nw")
    insertion.create_text(240, 95,text= "WELCOME",font=('semi bold',25,'normal'),fill='#C72542')
    insertion.create_text(180, 125,text= user_name,font=('semi bold',25,'normal'),fill='#C72542') 
    global name_ei2,type_e,year_e,price_e,color_e,loc_e,path_b
    name_ei2=Entry(insertion,width=15,font=('semi bold',40,'normal'))
    name_ei2.place(x=650,y=228)
    type_e=Entry(insertion,width=15,font=('semi bold',40,'normal'))
    type_e.place(x=650,y=298)
    year_e=Entry(insertion,width=15,font=('semi bold',40,'normal'))
    year_e.place(x=650,y=368)
    price_e=Entry(insertion,width=15,font=('semi bold',40,'normal'))
    price_e.place(x=650,y=438)
    color_e=Entry(insertion,width=15,font=('semi bold',40,'normal'))
    color_e.place(x=650,y=508)
    loc_e=Label(insertion,width=15,font=('semi bold',40,'normal'))
    loc_e.place(x=650,y=578)
    path_b = Button ( insertion, width=13,height=1,font=('semi bold',20,'normal'),bg='#C72542',text='CHOOSE FILE',command=get_path)
    path_b.place(x=1150,y=585)
    insertion_b = Button ( insertion, width=10,height=1,font=('semi bold',35,'normal'),bg='#C72542',text='INSERT',command=insert_val)
    insertion_b.place(x=780,y=820)
    insertion_b = Button ( insertion, width=10,height=1,font=('semi bold',35,'normal'),bg='#C72542',text='HOME',command=home)
    insertion_b.place(x=1600,y=50)
    insertion.create_text(550, 260,text= "NAME:",font=('semi bold',40,'normal'),fill='#C72542')
    insertion.create_text(550, 330,text= "TYPE:",font=('semi bold',40,'normal'),fill='#C72542')
    insertion.create_text(550, 400,text= "YEAR:",font=('semi bold',40,'normal'),fill='#C72542')
    insertion.create_text(550, 470,text= "PRICE:",font=('semi bold',40,'normal'),fill='#C72542')
    insertion.create_text(550, 540,text= "COLOR:",font=('semi bold',40,'normal'),fill='#C72542')
    insertion.create_text(530, 610,text= "PICTURE:",font=('semi bold',40,'normal'),fill='#C72542')

def insert_val():
    print('inserted')
    name=name_ei2.get()
    type=type_e.get()
    year=year_e.get()
    price=price_e.get()
    color=color_e.get()
    if(name=='' or type=='' or year=='' or price=='' or color==''):
        tkinter.messagebox.showinfo("ERROR",  "OOPS!I think you forgot to add something")
    elif(year.isnumeric()==False):
        tkinter.messagebox.showinfo("ERROR",  "year has to be an integer")
        print(year)
    elif(price.isnumeric()==False):
        tkinter.messagebox.showinfo("ERROR",  "price has to be an integer")
    elif(color.isnumeric()==True):
        tkinter.messagebox.showinfo("ERROR",  "Color has to be a string")
    else:
        c.execute("insert into cars values('"+name+"','"+type+"',"+year+","+price+",'"+color+"')")
        con.commit()
        tkinter.messagebox.showinfo("SUCCESS",  "Inserted successfully")
        src_dir = insertion.filename
        dst_dir = "E:\python trial"
        shutil.copy(src_dir, dst_dir)
        os.rename(src_dir, name+'.png')
    print(name,type,year,price,color)

def get_path():
    insertion.filename=filedialog.askopenfilename(initialdir='Pictures',title='select a file',filetypes=(("png file","*.png"),("gif files","*.gif")))
    print(insertion.filename)
    loc_e.config(text = insertion.filename)

def home():
    insertion_f.destroy()
    global interior_f,interior,name_ei,view_all_b,view_b,insert_b
    interior_f=Frame(root)
    interior_f.pack()
    interior=Canvas(interior_f,height=1080,width=1920,bg='#171717')
    interior.pack(fill = "both", expand = True)
    interior.create_image( 75, 75, image = user_icon, anchor = "nw")
    name_ei=Entry(interior,width=15,font=('semi bold',40,'normal'))
    name_ei.place(x=250,y=228)
    view_all_b = Button ( interior, width=15,height=1,font=('semi bold',35,'normal'),bg='#C72542',text='VIEW ALL',command=view_all)
    view_all_b.place(x=1450,y=228)
    view_b = Button ( interior, width=10,height=1,font=('semi bold',35,'normal'),bg='#C72542',text='VIEW',command=view)
    view_b.place(x=1013,y=228)
    insert_b = Button ( interior, width=10,height=1,font=('semi bold',35,'normal'),bg='#C72542',text='INSERT',command=insert)
    insert_b.place(x=1585,y=90)
    interior.create_text(150, 260,text= "NAME:",font=('semi bold',40,'normal'),fill='#C72542')

root = Tk()
root.geometry("1920x1080")
root.title("Car showroom")

bg = PhotoImage(file = "login.png")
user_icon = PhotoImage(file = "user_icon.png")
car=[] 

login_f=Frame(root)
login_f.pack()
interior_f=Frame(root)
interior_f.pack()
login=Canvas(login_f,height=1080,width=1920,bg='BLUE')
login.create_image( 0, 0, image = bg, anchor = "nw")
login.pack(fill = "both", expand = True)
interior=Canvas(interior_f,height=1080,width=1920,bg='#171717')
interior.pack(fill = "both", expand = True)
interior.create_image( 75, 75, image = user_icon, anchor = "nw")

name_e=Entry(login,width=15,font=('semi bold',40,'normal'))
name_e.place(x=935,y=450)
password_e=Entry(login,width=15,font=('semi bold',40,'normal'),show='*')
password_e.place(x=935,y=565)
login_b = Button ( login, width=10,height=1,font=('semi bold',40,'normal'),bg='#C72542',text='LOGIN',command=login_check)
login_b.place(x=750,y=700)
name_ei=Entry(interior,width=15,font=('semi bold',40,'normal'))
name_ei.place(x=250,y=228)
view_all_b = Button ( interior, width=15,height=1,font=('semi bold',35,'normal'),bg='#C72542',text='VIEW ALL',command=view_all)
view_all_b.place(x=1450,y=228)
view_b = Button ( interior, width=10,height=1,font=('semi bold',35,'normal'),bg='#C72542',text='VIEW',command=view)
view_b.place(x=1013,y=228)
insert_b = Button ( interior, width=10,height=1,font=('semi bold',35,'normal'),bg='#C72542',text='INSERT',command=insert)
insert_b.place(x=1585,y=90)

login.create_text(644, 480,text= "NAME:",font=('semi bold',40,'normal'))
login.create_text(560, 594,text= "PASSWORD:",font=('semi bold',40,'normal'))
login.create_text(900, 300,text= "LOGIN",font=('semi bold',96,'normal'))
interior.create_text(150, 260,text= "NAME:",font=('semi bold',40,'normal'),fill='#C72542')

root.mainloop()