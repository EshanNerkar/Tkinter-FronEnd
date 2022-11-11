from tkinter import *
from tkinter import font
from PIL import ImageTk,Image
from tkinter import messagebox
root = Tk()
root.geometry('1350x1500')
root['bg'] = "#247676"
root.iconbitmap("main_pics/1.jpg")

#functions
#drop_down-language
def drop_down1(str1):
    
    greet= drop1.get()
    l2=messagebox.showinfo(str1 + " selected ","You've selected " + str1)
    l2.grid(row=5,column=3)

#search2
def search_bar():
    
    greetings = e.get()
    l1=messagebox.showinfo("You've searched for " + greetings,"Thanks for searching for " + e.get())
    l1.grid(row=5,column=3)
#drop_down2
def drop_down2(str1):
    greet= drop1.get()
    l2=messagebox.showinfo(str1 + " selected ","You've selected " + str1)
    l2.grid(row=5,column=3)
#img-
def img():
    Label(root,text="hello!").grid(row=3,column=3)

def  open_new():
    top = Toplevel()
    top.geometry('800x700')
    top['bg'] = "#247676"
    global img_logo1 
    img_logo1 =  ImageTk.PhotoImage(Image.open("main_pics/1.jpg"))
    img_lab1 = Label(top,image=img_logo1)
    img_lab1.grid(row=0,column=0,pady=25,padx=15)
    lab_head = Label(top,text="HOUSING",fg="white",bg="#247676",font=("DM Sans",40))
    lab_head.grid(row=0,column=1,columnspan=2)
    bt1 = Button(top,text="APARTMENTS",bg="#247676",border=5,fg="white").grid(row=3,column=0,ipadx=60,ipady=20,padx=70,pady=10,)
    bt2 = Button(top,text=" COMMERCIALS ",bg="#247676",border=5,fg="white").grid(row=3,column=1,ipadx=60,ipady=20,padx=70,pady=10,)
    bt3 = Button(top,text="PARKING",bg="#247676",border=5,fg="white").grid(row=4,column=0,ipadx=72,ipady=20,padx=70,pady=10,)
    bt4 = Button(top,text="  STORAGE  ",bg="#247676",border=5,fg="white").grid(row=4,column=1,ipadx=75,ipady=20,padx=30,pady=10,)
    bt5 = Button(top,text="REAL ESTATE",bg="#247676",border=5,fg="white").grid(row=5,column=0,ipadx=65,ipady=20,padx=30,pady=10)
    bt6 = Button(top,text="ROOMS/SHARED",bg="#247676",border=5,fg="white").grid(row=5,column=1,ipadx=60,ipady=18,padx=10,pady=10)
    bt7 = Button(top,text="ROOMS WANTED",bg="#247676",border=5,fg="white").grid(row=6,column=0,ipadx=52,ipady=20,padx=10,pady=10)
    bt8 = Button(top,text="TEMPORARY",bg="#247676",border=5,fg="white").grid(row=6,column=1,ipadx=70,ipady=18,padx=10,pady=10)


frame1 = LabelFrame(root,padx=100).grid(row=0,column=0)
img_logo = ImageTk.PhotoImage(Image.open("main_pics/1.jpg"))
img_lab1 = Label(frame1,image=img_logo)
img_lab1.grid(row=0,column=0,pady=15)



#heading
lab_head = Label(frame1,text="CRAIGSLIST",fg="white",bg="#247676",font=("DM Sans",40))
lab_head.grid(row=0,column=1,columnspan=2)

#language
languages = ["ENGLISH","HINDI","MARATHI","GERMAN","SPANISH","FRENCH"]
drop1 = StringVar()
drop1.set("SELECT LANGUAGE")
dr1 = OptionMenu(frame1,drop1,*languages,command=drop_down1)
dr1.config(bg="#7bc9c0",fg="black")
dr1.grid(row=1,column=3,padx=10)

#search
e=Entry(root,font=("DM Sans",15))
e.grid(row=2,column=0,padx=15,pady=30,ipadx=30,ipady=8)
b_search = Button(root,text=" SEARCH ",font=("DM Sans",15),command=search_bar).grid(row=2,column=1)

#location
languages = ["PUNE","MUMBAI","CHENNAI","KOLKATA","DELHI","NAGPUR"]
drop2 = StringVar()
drop2.set("SELECT LOCATION")
dr2 = OptionMenu(frame1,drop2,*languages,command=drop_down2)
dr2.config(bg="#7bc9c0",fg="black")
dr2.grid(row=2,column=3,padx=10,)

#imagesforbuttons
img1 = ImageTk.PhotoImage(Image.open("main_pics/2.png"))
img2 = ImageTk.PhotoImage(Image.open("main_pics/3.png"))
img3 = ImageTk.PhotoImage(Image.open("main_pics/4.png"))
img4 = ImageTk.PhotoImage(Image.open("main_pics/5.png"))
img5 = ImageTk.PhotoImage(Image.open("main_pics/6.png"))
img6 = ImageTk.PhotoImage(Image.open("main_pics/7.png"))
img7 = ImageTk.PhotoImage(Image.open("main_pics/8.png"))
img8 = ImageTk.PhotoImage(Image.open("main_pics/9.png"))
img9 = ImageTk.PhotoImage(Image.open("main_pics/10.png"))


#buttons
bt1 = Button(root,text="COMMUNITY",image=img1,compound="top",command=open_new,bg="#247676",border=5,fg="white").grid(row=3,column=0,ipadx=70,ipady=20,padx=70,pady=10,)
bt2 = Button(root,text=" HOUSING ",image=img2,compound="top",bg="#247676",border=5,fg="white").grid(row=3,column=1,ipadx=75,ipady=10,padx=70,pady=10,)
bt3 = Button(root,text="JOB",image=img3,compound="top",bg="#247676",border=5,fg="white").grid(row=3,column=2,ipadx=80,ipady=10,padx=70,pady=10,)
bt4 = Button(root,text="  SERVICES  ",image=img4,compound="top",bg="#247676",border=5,fg="white").grid(row=4,column=0,ipadx=75,ipady=20,padx=30,pady=10,)
bt5 = Button(root,text="SALES",image=img5,compound="top",bg="#247676",border=5,fg="white").grid(row=4,column=1,ipadx=82,ipady=20,padx=30,pady=10)
bt6 = Button(root,text="DISCUSSION FORUMS",image=img6,compound="top",bg="#247676",border=5,fg="white").grid(row=4,column=2,ipadx=55,ipady=20,padx=10,pady=10)
bt7 = Button(root,text="RESUMES",image=img7,compound="top",bg="#247676",border=5,fg="white").grid(row=5,column=0,ipadx=82,ipady=20,padx=10,pady=10)
bt8 = Button(root,text="GIGS",image=img8,compound="top",bg="#247676",border=5,fg="white").grid(row=5,column=1,ipadx=78,ipady=20,padx=10,pady=10)
bt9 = Button(root,text="EVENT CALENDAR",image=img9,compound="top",bg="#247676",border=5,fg="white").grid(row=5,column=2,ipadx=60,ipady=20,padx=10,pady=10)



root.mainloop()