import math
from time import *
import threading
import turtle
from threading import Thread
from tkinter import *
import base64


f=open("data/password.txt",'rb+')             #password file
f2=open("data/background.txt",'r+')           #bg color file
background=f2.readline()
encodedPassword=f.readline()
password = base64.b64decode(encodedPassword).decode('utf-8')

f.close()
f2.close()

home_screen=None
home=None
tries=6
truth=True

"""Real time Clock"""
ddate=asctime().split()
day=ddate[0]+" "+ddate[1]+" "+ddate[2]
time1 = ''
sh=False
welcome_screen=None
clock=None
AFTER=None
def tick():
    global AFTER
    global truth
    global time1
    global ddate
    global day
    global welcome_screen
    global clock
    time2=strftime('%H:%M')
    newday=time2.split(":")
    clock.config(text=day+"      "+time2+"  ")
    if newday[0]=="00" and newday[1]=="00":
        ddate=asctime().split()
        day=ddate[0]+" "+ddate[1]+" "+ddate[2]
    if time2 != time1:
        time1 = time2
        clock.config(text=day+"      "+time2+"  ")
    if truth==True:
        try:
            AFTER=welcome_screen.after(200, tick)
        except:
            welcome_screen.after_cancel(AFTER)
    else:
        welcome_screen.after_cancel(AFTER)

"""Function to open WELCOME SCREEN - Login screen that opens when you run."""
def welcome(o=""):
    global clock
    global welcome_screen
    global home_screen
    global truth
    truth=True
    global home
    if o!="f":
        home.after_cancel(Home.AFTER)
        home.destroy()

    """Show button function"""
    def show():
        global sh
        if sh==False:
            e["show"]=""
            sh=True
        elif sh==True:
            e["show"]="*"
            sh=False

    def try_again():
        output_label["text"]="Try again."
        confirmbtn["bg"]="cyan"
        confirmbtn["state"]="normal"

    """Confirm button function"""
    def confirm(event=None):
        global welcome_screen
        global password
        global tries
        global truth
        global AFTER
        global home_screen
        global clock
        p=e.get()
        if p==password:
            truth=False
            welcome_screen.after_cancel(AFTER)
            clock=None
            """Argument "y" tells that welcome screen exists and needs to be destroyed"""
            home_screen=Home("y")
        elif p!=password:
            tries-=1
            output_label.place(x=0,y=320)
            output_label["text"]="Incorrect password, "+str(tries)+" tries remaining"
            if p!="":
                e.delete(0,END)
            e.focus_set()
            if tries==0:
                output_label["text"]="5 incorrect attempts, Try again after 30 seconds! "
                tries=6
                confirmbtn["bg"]="black"
                confirmbtn["state"]="disabled"
                t = threading.Timer(30.0,try_again)
                t.start()

    welcome_screen=Tk()                                                                                                        #welcome screen
    truth=True
    welcome_screen.geometry("325x400")
    welcome_screen.resizable(False,False)
    welcome_screen.title('MarvellOS')
    welcome_screen.config(bg=background)

    title_label=Label(welcome_screen,text="MarvellOS",bg=background,fg="dark blue",font=("Curlz MT",35))
    title_label.place(x=70,y=100)

    shbtn=Button(welcome_screen,text="Show",bg="light blue",fg="black",font=("Agency",8),command=show)
    shbtn.place(x=265,y=237)

    confirmbtn=Button(welcome_screen,text="Confirm",bg="cyan",fg="black",font=("Arial black",9),command=confirm, width=20,height=2)                              #confirm button
    confirmbtn.place(x=71,y=263)
    welcome_screen.bind("<Return>", confirm) #Binding Enter key for login confirmation

    welcome_frame=Frame(welcome_screen, relief=RIDGE, borderwidth=2)
    welcome_frame.pack()

    enterpass=Label(welcome_screen,text="Enter password:",font=("Century"),bg=background,fg="black")
    enterpass.place(x=96,y=215)
    e=Entry(welcome_screen,show="*",width=30)
    e.focus_set()                                                                                                                            #password entry field
    e.place(x=45,y=240)

    output_label=Label(welcome_screen,bg="red",fg="black",width=41,font=("Calibri",12))              #output label

    """--------------------------------------------VERSION UPDATE LABEL-------------------------------------------"""
    t="MarvellOS v1.3"

    inf=Label(welcome_screen,text=t,bg=background,fg="red",font=("Century",10,"bold"))
    inf.place(x=10,y=355)
    """Clock on the home screen"""
    global clock
    clock = Label(welcome_screen,font=("TIMES NEW ROMAN",10),anchor="e", bg='black',fg="white",width=46,height=2)                     #clock label
    clock.place(x=0,y=0)
    if truth:
        try:
            tick()
        except:
            welcome_screen.after_cancel(tick)

    welcome_screen.mainloop()


class Home():
    """This is the class which makes the app grid screen - If you log in with correct password"""
    AFTER=None
    def __init__(self,a=""):
        global truth
        global background
        global home
        global welcome_screen
        self.time1=''
        self.a=a
        home=Tk()
        home.title('home')
        home.geometry("325x400")
        home.resizable(False,False)
        home.config(bg=background)
        home.lift()
        home.attributes('-topmost', True)
        self.clock = Label(home,font=("TIMES NEW ROMAN",10),anchor="e", bg='black',fg="white",width=46,height=2)                     #clock label
        self.clock.place(x=0,y=0)
        self.tick1()
        wel1=Label(home,text="Here are your apps",bg="black",fg="white",width=46,height=1,font=("century",9))
        wel1.place(x=-23,y=45)
        if self.a=="y":
            truth=False
            welcome_screen.after_cancel(tick)
            welcome_screen.destroy()
            welcome_screen=None
        else:
            pass
        """App buttons"""
        sett=Button(home,text="Settings", height=5, bg="sky blue", fg="brown", width=10, font=("Bahnschrift",12),command=self.settings)                                         #settings button
        sett.place(x=2,y=100)
        calcbtn=Button(home,text="Calculator",height=5, width=10,bg="grey",fg="black", font=("Bahnschrift",12),command=self.calc)                                                       #calculator button
        calcbtn.place(x=112,y=100)
        design=Button(home,text="Designs",height=5, width=10, bg="purple",fg="cyan", font=("Bahnschrift",12),command=self.design)                                                         #design button
        design.place(x=222,y=100)
        notepad=Button(home,text="Notepad",height=5, width=10, bg="orange", fg="black",font=("Bahnschrift",12),command=self.notepad)                                                       #notepad button
        notepad.place(x=2,y=250)
        click=Button(home,text="Click \n Game", height=5, width=10, bg="blue", fg="pink", font=("Bahnschrift",12),command=self.click_game)                                                       #click test button
        click.place(x=112,y=250)
        sample=Button(home,text="Sample \n Pictures", height=5, width=10, bg="red", fg="yellow", font=("Bahnschrift",12),command=self.sample)                                                       #sample pictures button
        sample.place(x=222,y=250)
        lock=Button(home, text="LOCK",bg="black",fg="yellow",command=welcome)                                                                                                                                          #lock button
        lock.place(x=143,y=368)

        home.mainloop()

    """Clock"""
    def tick1(self):
        global home
        time2=strftime('%H:%M')
        newday=time2.split(":")
        if newday[0]=="00" and newday[1]=="00":
            self.ddate=asctime().split()
            self.day=self.ddate[0]+" "+self.ddate[1]+" "+self.ddate[2]
        if time2 != self.time1:
            self.time1 = time2
            self.clock.config(text=day+"      "+time2+"  ")
        try:
            Home.AFTER=home.after(200, self.tick1)
        except:
            home.after_cancel(Home.AFTER)

        self.ddate=asctime().split()
        self.day=self.ddate[0]+" "+self.ddate[1]+" "+self.ddate[2]
        global truth
        if truth:
            welcome_screen.after_cancel(tick)

    def settings(self):
        """Called when Settings button is pressed"""
        global background
        self.setwin=Tk()
        self.setwin.lift()
        self.setwin.attributes('-topmost', True)
        self.setwin.geometry("325x400")
        self.setwin.resizable(False,False)
        self.homebtn=Button(self.setwin,text="HOME", bg="black",fg="white",command=self.home_button7)
        self.homebtn.place(x=140,y=370)
        self.setwin.config(bg=background)
        global home
        home.after_cancel(Home.AFTER)
        home.destroy()
        self.ss=Label(self.setwin,text="Choose a setting:",bg="black",fg="white",width=46,height=2,font=("Arial",15))
        self.ss.place(x=-90,y=0)
        self.changingbtn=Button(self.setwin,text="Change Password", height=1, bg="sky blue", fg="brown", width=25, font=("Bahnschrift",12),command=self.change_password)
        self.changingbtn.place(x=45,y=100)
        self.var=StringVar(self.setwin)
        self.var.set(background)
        self.bglab=Label(self.setwin,text="Background colour:",bg=background,fg="black",font=("Arial",10))
        self.bglab.place(x=100,y=178)
        self.option = OptionMenu(self.setwin, self.var, "yellow", "green", "light blue", "pink","white")
        self.option.place(x=120,y=200)
        background=self.var.get()
        def save1():
            global background
            background=self.var.get()
            f2=open("data/background.txt","w")
            f2.write(background)
            f2.close()
        self.sv=Button(self.setwin,text="Save",command=save1,bg="cyan",fg="black")
        self.sv.place(x=140,y=235)

    """NOT WORKING ON SOME DEVICES"""
    def click_game(self):
        """Calls when click button is pressed"""
        global background
        self.clickwin=Tk()
        self.clickwin.lift()
        self.clickwin.attributes('-topmost', True)
        self.clickwin.geometry("325x400")
        self.clickwin.resizable(False,False)
        self.n=0
        self.clickwin.config(bg="cyan")
        self.w=Label(self.clickwin, text="CLICK TEST!")
        self.w.config(bg="black", fg="white",font=("broadway",30))
        self.w.pack(side=TOP)
        self.bt2=Button(self.clickwin,text="Start timer", height="3",width="8", command=self.timer)
        self.bt2.config(bg="red")
        self.bt2.pack()
        self.tt=Label(self.clickwin)
        self.tt.pack()
        self.bt=Button(self.clickwin,text="CLICK!", height="10",width="20",state=DISABLED,command=self.number)
        self.bt.config(bg="yellow")
        self.bt.pack()
        self.ans=Label(self.clickwin)
        self.ans.pack()
        self.res=Label(self.clickwin, text="                                   ")
        self.res.config(bg="dark green", fg=background,font=("arial narrow",15))
        self.res.pack()
        self.bt3=Button(self.clickwin,text="Reset", height="5",width="8", command=self.reset)
        self.bt3.pack(side=RIGHT)
        global home
        home.after_cancel(Home.AFTER)
        home.destroy()
        self.homebtn=Button(self.clickwin,text="HOME", bg="black",fg="white",command=self.home_button4)
        self.homebtn.place(x=140,y=370)

    def timer(self):
        self.bt2.config(state=DISABLED)
        self.homebtn.config(state=DISABLED)
        self.bt3.config(state=DISABLED)
        self.bt.config(state='normal')
        self.func1()
    def number(self):
        self.n+=1
        self.ans.config(text=self.n)
    def reset(self):
        self.homebtn.config(state='normal')
        self.bt2.config(state='normal')
        self.bt.config(state=DISABLED)
        self.res["text"]="                        "
        self.ans.config(text="0")
        self.n=0
        self.tt.config(text="Reset")

    def func1(self):
        try:
            self.t = threading.Thread(target=self.func2)
            self.t.start()
        except:
            pass
    def func2(self):
        for i in range(0,10):
            self.tt.config(text=10-i)
            sleep(1)
        self.bt.config(state=DISABLED)
        self.tt.config(text="Time up")
        self.bt3.config(state='normal')
        if self.n<50:
            self.res["text"]=str(self.n)+" clicks in 10 seconds: Bad clicker!"
        elif 50<=self.n and self.n<60:
            self.res["text"]=str(self.n)+" clicks in 10 seconds: Average clicker!"
        elif self.n>=60 and self.n<70:
            self.res["text"]=str(self.n)+" clicks in 10 seconds: Master clicker!"
        elif self.n>=70:
            self.res["text"]=str(self.n)+" clicks in 10 seconds: Clicking god!"

    def notepad(self):
        """Called when notepad button is pressed"""
        global background
        self.notepad=Tk()
        f=open("data/notes.txt","r+")
        t=f.read()
        self.notepad.lift()
        self.notepad.attributes('-topmost', True)
        self.notepad.geometry("325x400")
        self.notepad.resizable(False,False)
        self.notepad.config(bg="purple")
        global home
        home.after_cancel(Home.AFTER)
        home.destroy()
        self.homebtn=Button(self.notepad,text="HOME", bg="black",fg="white",command=self.home_button3)
        self.homebtn.place(x=140,y=370)
        self.notes=Text(self.notepad, width=53,height=18,font=("Times New Roman",10))
        self.notes.place(x=1,y=60)
        self.notes.insert(END,t)
        self.head=Label(self.notepad, text="NOTEPAD",bg=background, width=23,fg="purple",font=("Arial black",15))
        self.head.place(x=0,y=10)
        self.sav=Button(self.notepad,text="Save",command=self.save)
        self.sav.place(x=146,y=340)

    def save(self):
        self.text=self.notes.get(0.0,END)
        f=open("data/notes.txt","w")
        f.write(self.text)
        f.close()

    def sample(self):
        """Called when Sample pictures button is pressed"""
        global background
        global home
        home.after_cancel(Home.AFTER)
        home.destroy()
        self.samwin=Tk()
        self.samwin.lift()
        self.samwin.attributes('-topmost', True)
        self.samwin.geometry("325x400")
        self.samwin.resizable(False,False)
        self.samwin.config(bg="black")
        self.homebtn=Button(self.samwin,text="HOME", bg="white",fg="black",command=self.home_button6)
        self.homebtn.place(x=140,y=370)
        self.img=PhotoImage(file="sample_pictures/sample1.gif")
        self.pics=Label(self.samwin, width = 325, image=self.img, bg="black", height = 300)
        self.pics.place(x=0,y=0)
        self.nxt=Button(self.samwin,text=">", bg="yellow", font=("Bauhaus 93",20),command=self.nxt)
        self.nxt.place(x=280,y=310)
        self.bck=Button(self.samwin,text="<", bg="yellow", font=("Bauhaus 93",20),command=self.bck, state=DISABLED)
        self.bck.place(x=10,y=310)
        self.i=1
    def nxt(self):
        self.i+=1
        self.bck["state"]="normal"
        if self.i==1:
            self.img = PhotoImage(file="sample_pictures/sample1.gif")
        elif self.i==2:
            self.img = PhotoImage(file="sample_pictures/sample2.gif")
        elif self.i==3:
            self.img = PhotoImage(file="sample_pictures/sample3.gif")
        elif self.i==4:
            self.img = PhotoImage(file="sample_pictures/sample4.gif")
        elif self.i==5:
            self.img = PhotoImage(file="sample_pictures/sample5.gif")
        elif self.i==6:
            self.img = PhotoImage(file="sample_pictures/sample6.gif")
        elif self.i==7:
            self.img = PhotoImage(file="sample_pictures/sample7.gif")
        elif self.i==8:
            self.img = PhotoImage(file="sample_pictures/sample8.gif")
        elif self.i==9:
            self.img = PhotoImage(file="sample_pictures/sample9.gif")
        elif self.i==10:
            self.img = PhotoImage(file="sample_pictures/sample10.gif")
            self.nxt["state"]=DISABLED
        self.pics["image"]=self.img
    def bck(self):
        self.i-=1
        self.nxt["state"]="normal"
        if self.i==1:
            self.img = PhotoImage(file="sample_pictures/sample1.gif")
            self.bck["state"]=DISABLED
        elif self.i==2:
            self.img = PhotoImage(file="sample_pictures/sample2.gif")
        elif self.i==3:
            self.img = PhotoImage(file="sample_pictures/sample3.gif")
        elif self.i==4:
            self.img = PhotoImage(file="sample_pictures/sample4.gif")
        elif self.i==5:
            self.img = PhotoImage(file="sample_pictures/sample5.gif")
        elif self.i==6:
            self.img = PhotoImage(file="sample_pictures/sample6.gif")
        elif self.i==7:
            self.img = PhotoImage(file="sample_pictures/sample7.gif")
        elif self.i==8:
            self.img = PhotoImage(file="sample_pictures/sample8.gif")
        elif self.i==9:
            self.img = PhotoImage(file="sample_pictures/sample9.gif")
        elif self.i==10:
            self.img = PhotoImage(file="sample_pictures/sample10.gif")
        self.pics["image"]=self.img

    def design(self):
        """Called when Designs button is pressed"""
        self.deswin=Tk()
        self.deswin.lift()
        self.deswin.attributes('-topmost', True)
        self.deswin.geometry("325x400")
        self.deswin.resizable(False,False)
        self.deswin.config(bg="black")
        global home
        home.after_cancel(Home.AFTER)
        home.destroy()
        self.homebtn=Button(self.deswin,text="HOME", bg="white",fg="black",command=self.home_button2)
        self.homebtn.place(x=140,y=370)
        self.choo=Label(self.deswin,text="Choose a design:",bg="black",fg="white",width=28,height=2,font=("Candara",15))
        self.choo.place(x=0,y=10)
        self.des1=Button(self.deswin,text="Design 1 ",font=("Elephant",20), command=self.des1)
        self.des1.place(x=80,y=80)
        self.des2=Button(self.deswin,text="Design 2",font=("Elephant",20), command=self.des2)
        self.des2.place(x=80,y=150)
        self.des3=Button(self.deswin,text="Design 3",font=("Elephant",20), command=self.des3)
        self.des3.place(x=80,y=220)
        self.des4=Button(self.deswin,text="Design 4",font=("Elephant",20), command=self.des4)
        self.des4.place(x=80,y=290)

    def des1(self):
        self.deswin.destroy()
        self.deswin=Tk()
        self.deswin.lift()
        self.deswin.attributes('-topmost', True)
        self.deswin.geometry("325x400")
        self.deswin.config(bg="yellow")
        self.deswin.resizable(False,False)
        self.homebtn=Button(self.deswin,text="HOME", bg="black",fg="white",command=self.home_button2)
        self.homebtn.place(x=140,y=370)
        self.canvas = Canvas(master=self.deswin,width=325,height=350, bg="black")
        self.t = turtle.RawTurtle(self.canvas)
        self.canvas.place(x=0,y=0)
        colors=['red','purple','blue','green','yellow','orange']
        self.t.speed(0)
        for x in range(160):
            self.t.pencolor(colors[x%6])
            self.t.width(x/100+1)
            self.t.forward(x)
            self.t.left(59)

    def des2(self):
        self.deswin.destroy()
        self.deswin=Tk()
        self.deswin.lift()
        self.deswin.attributes('-topmost', True)
        self.deswin.geometry("325x400")
        self.deswin.resizable(False,False)
        self.deswin.config(bg="yellow")
        self.homebtn=Button(self.deswin,text="HOME", bg="black",fg="white",command=self.home_button2)
        self.homebtn.place(x=140,y=370)
        self.canvas = Canvas(master=self.deswin,width=325,height=350, bg="black")
        self.t=turtle.RawTurtle(self.canvas)
        self.canvas.place(x=0,y=0)
        for i in range(0,24):
            self.t.speed(-9)
            self.t.right(46)
            self.t.pencolor("blue")
            self.t.circle(30)
            self.t.right(20)
            self.t.pencolor("green")
            self.t.circle(60)
            self.t.circle(70)
            self.t.pencolor("red")
            self.t.circle(55)
            self.t.circle(57)
            self.t.left(10)
            self.t.pencolor("yellow")
            self.t.right(5)

    def des3(self):
        self.deswin.destroy()
        self.deswin=Tk()
        self.deswin.lift()
        self.deswin.attributes('-topmost', True)
        self.deswin.geometry("325x400")
        self.deswin.resizable(False,False)
        self.deswin.config(bg="yellow")
        self.homebtn=Button(self.deswin,text="HOME", bg="black",fg="white",command=self.home_button2)
        self.homebtn.place(x=140,y=370)
        self.canvas = Canvas(master=self.deswin,width=325,height=350, bg="black")
        self.t=turtle.RawTurtle(self.canvas)
        self.canvas.place(x=0,y=0)
        for i in range(50):
            self.t.speed(20)
            self.t.pencolor("red")
            self.t.backward(100)
            self.t.pencolor("green")
            self.t.circle(30)
            self.t.right(70)

    def des4(self):
        self.deswin.destroy()
        self.deswin=Tk()
        self.deswin.lift()
        self.deswin.attributes('-topmost', True)
        self.deswin.geometry("325x400")
        self.deswin.resizable(False,False)
        self.deswin.config(bg="yellow")
        self.homebtn=Button(self.deswin,text="HOME", bg="black",fg="white",command=self.home_button2)
        self.homebtn.place(x=140,y=370)
        self.canvas = Canvas(master=self.deswin,width=325,height=350, bg="black")
        self.t=turtle.RawTurtle(self.canvas)
        self.canvas.place(x=0,y=0)
        self.t.speed(700)
        for i in range(180):
            self.t.forward(80)
            self.t.right(30)
            self.t.forward(20)
            self.t.left(60)
            self.t.forward(50)
            self.t.right(30)
            self.t.penup()
            self.t.setposition(0, 0)
            self.t.pendown()
            self.t.right(2)

    def calc(self):
        """Called when Calculator button is pressed"""
        try:
            global background
            self.calcwin=Tk()
            self.calcwin.lift()
            self.calcwin.attributes('-topmost', True)
            self.calcwin.geometry("325x400")
            self.calcwin.resizable(False,False)
            self.calcwin.config(bg=background)
            global home
            home.after_cancel(Home.AFTER)
            home.destroy()
            self.homebtn=Button(self.calcwin,text="HOME", bg="black",fg="white",command=self.home_button1)
            self.homebtn.place(x=140,y=370)
            self.num=Entry(self.calcwin,width=18,font=("Arial black",20))
            self.num.place(x=0,y=10)
            self.num.focus_set()
            self.ans=Label(self.calcwin,bg="light green", width=17,fg="black",font=("Arial black",20))
            self.ans.place(x=0,y=60)
            self.plus_btn=Button(self.calcwin,text="+",font=("Elephant",20), command=self.plus)
            self.plus_btn.config(width=3)
            self.plus_btn.place(x=0,y=120)
            self.calcwin.bind("+",self.plus)
            self.minus_btn=Button(self.calcwin,text="-",font=("Elephant",20), command=self.minus)
            self.minus_btn.config(width=3)
            self.minus_btn.place(x=85,y=120)
            self.calcwin.bind("-",self.minus)
            self.mult_btn=Button(self.calcwin,text="x",font=("Elephant",20), command=self.mult)
            self.mult_btn.config(width=3)
            self.mult_btn.place(x=170,y=120)
            self.calcwin.bind("*",self.mult)
            self.div_btn=Button(self.calcwin,text="/",font=("Elephant",20), command=self.div)
            self.div_btn.config(width=3)
            self.div_btn.place(x=255,y=120)
            self.calcwin.bind("/",self.div)
            self.sqroot_btn=Button(self.calcwin,text="sqrt",font=("Elephant",20), command=self.sqroot)
            self.sqroot_btn.config(height=1,width=3)
            self.sqroot_btn.place(x=0,y=200)
            self.fact_btn=Button(self.calcwin,text="!",font=("Elephant",20), command=self.fact)
            self.fact_btn.config(width=3)
            self.fact_btn.place(x=85,y=200)
            self.calcwin.bind("!",self.fact)
            self.power_btn=Button(self.calcwin,text="x^y",font=("Elephant",20), command=self.power)
            self.power_btn.config(height=1,width=3)
            self.power_btn.place(x=170,y=200)
            self.calcwin.bind("^",self.power)
            self.clr_btn=Button(self.calcwin,text="C",font=("Elephant",20), command=self.c)
            self.clr_btn.config(height=1,width=3)
            self.clr_btn.place(x=255,y=200)
            self.calcwin.bind("<Delete>",self.c)
            self.calcwin.bind("c",self.c)
            self.sin_btn=Button(self.calcwin,text="sin",font=("Elephant",20), command=self.sin)
            self.sin_btn.config(height=1,width=3)
            self.sin_btn.place(x=0,y=280)
            self.cos_btn=Button(self.calcwin,text="cos",font=("Elephant",20), command=self.cos)
            self.cos_btn.config(height=1,width=3)
            self.cos_btn.place(x=85,y=280)
            self.tan_btn=Button(self.calcwin,text="tan",font=("Elephant",20), command=self.tan)
            self.tan_btn.config(height=1,width=3)
            self.tan_btn.place(x=170,y=280)
            self.equal_btn=Button(self.calcwin,text="=",font=("Elephant",20), command=self.equal)
            self.equal_btn.config(width=3)
            self.equal_btn.place(x=255,y=280)
            self.calcwin.bind("<Return>",self.equal)
            
        except TypeError as e:
            self.ans["text"]="Invalid Input "
        except ValueError as e:
            self.ans["text"]="Invalid Input "
        except OverflowError as e:
            self.ans["text"]="Out of range"
    try:
        def plus(self,event=None):
            self.v=self.num.get()
            if "+" in self.v:
               self.a=self.v[:-1]
            else:
                self.a=self.v
            self.num.delete(0,END)
            self.num.focus_set()
            self.operator="+"
        def minus(self,event=None):
            self.v=self.num.get()
            if "-" in self.v:
               self.a=self.v[:-1]
            else:
                self.a=self.v
            self.num.delete(0,END)
            self.num.focus_set()
            self.operator="-"
        def mult(self,event=None):
            self.v=self.num.get()
            if "*" in self.v:
               self.a=self.v[:-1]
            else:
                self.a=self.v
            self.num.delete(0,END)
            self.num.focus_set()
            self.operator="x"
        def div(self,event=None):
            self.v=self.num.get()
            if "/" in self.v:
               self.a=self.v[:-1]
            else:
                self.a=self.v
            self.num.delete(0,END)
            self.num.focus_set()
            self.operator="/"
        def sqroot(self):
            try:
                self.a=self.num.get()
                if float(self.a)>=0:
                    self.ans["text"]=math.sqrt(float(self.a))
                else:
                    self.ans["text"]="Not a real number"
            except ValueError as e:
                self.ans["text"]="Invalid Input "
            except TypeError as e:
                self.ans["text"]="Invalid Input "
            except OverflowError as e:
                self.ans["text"]="Out of range"

        def fact(self,event=None):
            try:
                self.v=self.num.get()
                if "!" in self.v:
                   self.a=self.v[:-1]
                else:
                    self.a=self.v
                if int(self.a)>=0:
                    self.an=str(math.factorial(int(self.a)))
                    self.ans["text"]=self.an
                    if len(self.an)>17:
                        self.ans["text"]="Out of Range"
                else:
                    self.ans["text"]="Error"
            except ValueError as e:
                self.ans["text"]="Invalid Input "
            except TypeError as e:
                self.ans["text"]="Invalid Input "
            except OverflowError as e:
                self.ans["text"]="Out of range"
        def power(self,event=None):
            self.v=self.num.get()
            if "^" in self.v:
               self.a=self.v[:-1]
            else:
                self.a=self.v
            self.num.delete(0,END)
            self.num.focus_set()
            self.operator="^"
        def sin(self):
            try:
                self.a=self.num.get()
                self.a=float(self.a)/57.2958
                self.an=str(math.sin(float(self.a)))
                self.ans["text"]=self.an
                if len(self.an)>17:
                    self.ans["text"]="Out of Range"
            except ValueError as e:
                self.ans["text"]="Invalid Input "
            except TypeError as e:
                self.ans["text"]="Invalid Input "
            except OverflowError as e:
                self.ans["text"]="Out of range"
        def cos(self):
            try:
                self.a=self.num.get()
                self.a=float(self.a)/57.2958
                self.an=str(math.cos(float(self.a)))
                self.ans["text"]=self.an
                if len(self.an)>17:
                    self.ans["text"]="Out of Range"
            except ValueError as e:
                self.ans["text"]="Invalid Input "
            except TypeError as e:
                self.ans["text"]="Invalid Input "
            except OverflowError as e:
                self.ans["text"]="Out of range"
        def tan(self):
            try:
                self.a=self.num.get()
                self.a=float(self.a)/57.2958
                self.an=str(math.tan(float(self.a)))
                self.ans["text"]=self.an
                if len(self.an)>17:
                    self.ans["text"]="Out of Range"
            except ValueError as e:
                self.ans["text"]="Invalid Input "
            except TypeError as e:
                self.ans["text"]="Invalid Input "
            except OverflowError as e:
                self.ans["text"]="Out of range"
        def c(self,event=None):
            """clear button for calculator"""
            self.a=0
            self.b=0
            self.num.delete(0,END)
            self.ans["text"]=""
        def equal(self,event=None):
            try:
                self.b=self.num.get()
                if self.operator=="+":
                    self.an=str(float(self.a)+float(self.b))
                    if len(self.an)<17:
                        self.ans["text"]=self.an
                    else:
                        self.ans["text"]="Out of Range"
                elif self.operator=="-":
                    self.an=str(float(self.a)-float(self.b))
                    if len(self.an)<17:
                        self.ans["text"]=self.an
                    else:
                        self.ans["text"]="Out of Range"
                elif self.operator=="x":
                    self.an=str(float(self.a)*float(self.b))
                    if len(self.an)<17:
                        self.ans["text"]=self.an
                    else:
                        self.ans["text"]="Out of Range"
                elif self.operator=="^":
                    self.an=str(math.pow(float(self.a),float(self.b)))
                    if len(self.an)<17:
                        self.ans["text"]=self.an
                    else:
                        self.ans["text"]="Out of Range"
                elif self.operator=="/":
                    if float(self.b)!=0:
                        self.an=str(float(self.a)/float(self.b))
                        if len(self.an)<17:
                            self.ans["text"]=self.an
                        else:
                            self.ans["text"]="Out of Range"
                    else:
                        self.ans["text"]="Not a number"
            except ValueError as e:
                self.ans["text"]="Invalid Input "
            except TypeError as e:
                self.ans["text"]="Invalid Input "
            except OverflowError as e:
                self.ans["text"]="Out of range"
    except ValueError as e:
        self.ans["text"]="Invalid Input "+e.message
    except TypeError as e:
        self.ans["text"]="Invalid Input "+e.message
    except OverflowError as e:
                self.ans["text"]="Out of range"
    
    """Changing password"""
    def next(self):
            global password
            if self.co==1:
                self.next["text"]="Next"
                self.prev=self.ent.get()
                self.k["text"]="                      "
                if self.prev==password:
                    self.co=2
                    self.f=open("data/password.txt","r+")
                    self.ent.delete(0,END)
                    self.ent.focus_set()
                    self.l["text"]="Enter new password:"
                elif self.prev!=password:
                    self.k["text"]="Incorrect password, cannot change."
                    self.k.place(x=0,y=260)
                    self.next["text"]="Retry"
                    self.l["text"]="Enter previous password:"
                    self.ent.delete(0,END)
                    self.ent.focus_set()
                    self.co=1
            elif self.co==2:
                self.new_p=self.ent.get()
                self.ent.delete(0,END)
                self.ent.focus_set()
                self.l["text"]="Confirm new password:"
                self.co=3
            elif self.co==3:
                self.confirm=self.ent.get()
                if self.new_p==self.confirm:
                    self.f=open("data/password.txt","wb")
                    self.f.write(base64.b64encode(self.confirm.encode()))
                    self.f.close()
                    self.ent.delete(0,END)
                    password=self.confirm
                    self.l["text"]="Password changed!"
                    self.k["text"]="Password changed!"
                    self.co=1
                else:
                    self.k["text"]="Passwords do not match, try again."
                    self.k.place(x=0,y=260)
                    self.next["text"]="Retry"
                    self.l["text"]="Enter previous password:"
                    self.ent.delete(0,END)
                    self.ent.focus_set()
                    self.co=1

    def change_password(self):
        """Called when Change password button is pressed"""
        global password
        self.passwin=Tk()
        self.passwin.lift()
        self.passwin.attributes('-topmost', True)
        self.passwin.geometry("325x400")
        self.passwin.resizable(False,False)
        self.passwin.config(bg="light green")
        self.setwin.destroy()
        self.homebtn=Button(self.passwin,text="HOME", bg="black",fg="white",command=self.home_button5)
        self.homebtn.place(x=140,y=370)
        self.ent=Entry(self.passwin, show="*",width=18,font=("Arial black",20))
        self.ent.place(x=0,y=100)
        self.next=Button(self.passwin, text="Next",bg="blue",fg="yellow", command=self.next)
        self.next.place(x=100,y=200)
        self.next.config(width=15)
        self.l=Label(self.passwin, bg="light green",text="Enter previous password:",font=("Georgia",12),width=30)
        self.l.place(x=20,y=70)
        self.k=Label(self.passwin,text="",bg="red",fg="pink",font=("Onyx",20),width=40)
        self.k.place(x=0,y=260)
        self.show=Button(self.passwin, text="Show",bg="blue",fg="yellow" ,command=self.show)
        self.show.place(x=100,y=150)
        self.show.config(width=15)
        self.co=1
        self.sh=False
    def show(self):
        if self.sh==False:
            self.ent["show"]=""
            self.sh=True
        elif self.sh==True:
            self.ent["show"]="*"
            self.sh=False

    """Home buttons for all screens"""
    def home_button1(self):
        global home_screen                                     #home button for calculator
        self.calcwin.destroy()
        home_screen=Home()
    def home_button2(self):
        global home_screen                                      #home button for design window
        self.deswin.destroy()
        home_screen=Home()
    def home_button3(self):
        global home_screen                                     #home button for notepad window
        self.notepad.destroy()
        home_screen=Home()
    def home_button4(self):
        global home_screen                                     #home button for click game window
        self.clickwin.destroy()
        home_screen=Home()
    def home_button5(self):
        global home_screen                                     #home button for password change window
        self.passwin.destroy()
        home_screen=Home()
    def home_button6(self):
        global home_screen                                  #home button for sample pictures window
        self.samwin.destroy()
        home_screen=Home()
    def home_button7(self):
        global home_screen                                  #home button for settings window
        self.setwin.destroy()
        home_screen=Home()

welcome(o="f")
