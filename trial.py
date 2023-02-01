from tkinter import *
root = Tk()
root.geometry("1920x1080")
root.title("Blood donation")
def dummy():
    print('clicked')
def dummy2(event=None):
    print('clicked2')
def dummy3(event=None):
    global trial
    trial.config(fg='blue')
def dummy4(event=None):
    global trial
    trial.config(fg='red')
def intro4():
    global intro1_f,intro4_i,intro4_f,intro4_login_bi,intro4_login_ri,intro4_c,intro4_login_b,intro4_login_r,trial,drop
    print('hi')
    intro1_f.destroy()
    intro4_i = PhotoImage(file = "intro4.png")
    intro4_login_bi = PhotoImage(file = "login_b.png")
    intro4_login_ri = PhotoImage(file = "register_b.png")
    options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
    ]
    intro4_f=Frame(root)
    intro4_f.pack()
    intro4_c=Canvas(intro4_f,height=1080,width=1920)
    intro4_c.create_image( 0, 0, image = intro4_i, anchor = "nw")
    intro4_c.pack(fill = "both", expand = True)
    intro4_f1=Frame(intro4_c)
    intro4_f1.place(x=700,y=700)
    intro4_login_b=Button(intro4_c, image = intro4_login_bi,borderwidth = 0,bg='#FFFFFF',command=dummy)
    intro4_login_b.place(x=172,y=585)
    intro4_login_r=Button(intro4_c, image = intro4_login_ri,borderwidth = 0,bg='#FFFFFF',command=dummy)
    intro4_login_r.place(x=172,y=666)
    clicked = StringVar()
    clicked.set( "Monday" )
    drop = OptionMenu( intro4_f1 , clicked , *options )
    drop.pack(expand=True)
    drop.config(width=20)
    trial=Label(intro4_c,bg='#FFFFFF',fg='red',text='click',cursor="hand2",font=('semi bold',40,'normal'))
    trial.place(x=172,y=766)
    trial.bind("<Button-1>",dummy2)
    trial.bind("<Enter>",dummy3)
    trial.bind("<Leave>",dummy4)


intro1_i = PhotoImage(file = "intro.png")


intro1_f=Frame(root)
intro1_f.pack()


intro1_c=Canvas(intro1_f,height=1080,width=1920,bg='BLUE')
intro1_c.pack(fill = "both", expand = True)


intro1_login_b=Button(intro1_c, image = intro1_i,borderwidth = 0,command=intro4)
intro1_login_b.place(x=0,y=0)


root.mainloop()