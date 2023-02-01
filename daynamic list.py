from tkinter import *
import mysql.connector as mcon

root = Tk()
root.geometry("1920x1080")
root.title("Blood donation")
con = mcon.connect(host="localhost", user="root", password="1234")
c = con.cursor()
c.execute("use carshowroom")

class table:
    def __init__(self,name,location,group,x1,y1) -> None:
        self.name=name
        self.location=location
        self.group=group
        self.block_f=Frame(f1,height=168,width=418)
        self.donate_b_i=PhotoImage(file = 'donate_b.png')
        self.block=Canvas(self.block_f,height=168,width=418)
        self.block.create_text(10, 10,text= 'name',font=('poppins',14,'normal'),fill='#C72542',anchor='nw')
        self.block.create_text(10, 35,text= self.name,font=('poppins',14,'normal'),fill='#C72542',anchor='nw')
        self.block.create_text(10, 70,text= 'Location :  '+self.location,font=('poppins',14,'normal'),fill='#C72542',anchor='nw')
        self.block.create_text(10, 95,text=self.location,font=('poppins',14,'normal'),fill='#C72542',anchor='nw')
        self.view_all_b = Button ( self.block,font=('poppins',18,'normal'),image=self.donate_b_i,text='VIEW ALL',command=self.clicked,cursor='hand2',borderwidth = 0)
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

def view_all():
    for i in t:
        i.delete()
    c.execute("select * from donate")
    ls=c.fetchall()
    x=302
    y=204
    for d in ls:
        t.append(table(d[0],d[1],d[2],x,y))
        x=x+514
        print(d)
        if(x>=1875):
            x=75
            y=y+258
t=[] 
f1=Frame(root,bg='#FFFFFF')
f1.pack(fill = "both", expand = True)
view_all_b = Button ( f1, width=15,height=1,font=('semi bold',35,'normal'),bg='#C72542',text='VIEW ALL',command=view_all)
view_all_b.place(x=100,y=228)
root.mainloop()