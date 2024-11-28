from tkinter import*
from tkinter import messagebox as m
from PIL import ImageTk,Image
import webbrowser

def tech():
   webbrowser.open_new("https://techcrunch.com/")

def edu():
   webbrowser.open_new("https://www.educationupdates.org/")
   
def he():
   webbrowser.open_new("https://www.who.int/")

def ai():
   webbrowser.open_new("www.instagram.com")

def af():
   webbrowser.open_new("www.facebook.com")
   
def aw():
   webbrowser.open_new("www.whatsapp.com")


def at():
    webbrowser.open_new("www.twitter.com")



def asearch():
   word2=we.get()
   search="http://google.com/search?q="+word2
   webbrowser.open_new(search)
   
def ainsta():
    global photo2,img_l2
    w22=Tk()
    w22.title("Instagram")
    w22.geometry("1900x2000")
    w22.config(bg="#EE34D2")
    img2=Image.open("ig.jpg")
    photo2=ImageTk.PhotoImage(img2,master=w22)
    img_l2=Label(w22,image=photo2)
    img_l2.place(width=1900,height=2000)
    ail=Label(w22,text="Instagram Information & updates:",font="Timesnewroman 30 bold",bg="black",fg="white").pack(fill="x")
    uil1=Label(w22,text="Click the below link for more updates",font="Timesnewroman 30").place(x=400,y=100)
    ain=Button(w22,text="Instagram",font="Timesnewroman 20",command=ai,bg="white",fg="black").place(x=800,y=350)
    b2=Button(w22,text="Cancel",font="TimesNewRoman 20",command=w22.destroy,bg="white",fg="black")
    b2.place(x=500,y=350)
def afb():
    w21=Tk()
    w21.title("Facebook")
    w21.geometry("1900x2000")
    w21.config(bg="#0066FF")
    afbl=Label(w21,text="Facebook Information & updates:",font="Timesnewroman 30 bold",bg="black",fg="white").pack(fill="x")
    ufbl1=Label(w21,text="Click the below link for more updates",font="Timesnewroman 30").place(x=400,y=100)
    ab=Button(w21,text="Facebook",font="Timesnewroman 20",command=af,bg="white",fg="black").place(x=800,y=350)          
    b2=Button(w21,text="Cancel",font="TimesNewRoman 20",command=w21.destroy,bg="white",fg="black")
    b2.place(x=500,y=350)
def awa():
    w20=Tk()
    w20.title("Whatsapp")
    w20.geometry("1900x2000")
    w20.config(bg="#3AA655")
    awl=Label(w20,text="Whatsapp Information &  updates:",font="Timesnewroman 30 bold",bg="black",fg="white").pack(fill="x")
    uwl1=Label(w20,text="Click the below link for more updates",font="Timesnewroman 30",bg="white",fg="black").place(x=400,y=100)
    awap=Button(w20,text="Whatsapp",font="Timesnewroman 20",command=aw,bg="white",fg="black").place(x=800,y=350)
    b2=Button(w20,text="Cancel",font="TimesNewRoman 20",command=w20.destroy,bg="white",fg="black")
    b2.place(x=500,y=350)    
def atw():
    w19=Tk()
    w19.title("Twitter")
    w19.geometry("1900x2000")
    w19.config(bg="#4997D0")
    atl=Label(w19,text="Twitter Information & updates:",font="Timesnewroman 30 bold",bg="black",fg="white").pack(fill="x")
    utl1=Label(w19,text="Click the below link for more updates",font="Timesnewroman 30").place(x=400,y=100)
    atwi=Button(w19,text="Twitter",font="Timesnewroman 20",command=at,bg="white",fg="black").place(x=800,y=350)
    b2=Button(w19,text="Cancel",font="TimesNewRoman 20",command=w19.destroy,bg="white",fg="black")
    b2.place(x=500,y=350)



def ui():
   webbrowser.open_new("www.instagram.com")

def uf():
   webbrowser.open_new("www.facebook.com")
   
def uw():
   webbrowser.open_new("www.whatsapp.com")


def ut():
    webbrowser.open_new("www.twitter.com")
   
def usearch():
   word=se.get()
   search="http://google.com/search?q="+word
   webbrowser.open_new(search)
   
def uinsta():
    w15=Tk()
    w15.title("Instagram")
    w15.geometry("1900x2000")
    w15.config(bg="#EE34D2")
    
    f = Frame(w15, width=1900, height=200)
    f.pack()
    f.place(anchor='center', relx=0.5, rely=0.5)

    img = ImageTk.PhotoImage(Image.open("C:\\Users\\sangamithra\\Desktop\\Python Mini Project\\ig.jpg"))

    l = Label(f, image = img)
    l.pack()
 
    
    uil=Label(w15,text="Instagram Information & updates",font="Timesnewroman 30 bold",bg="black",fg="white").pack(fill="x")
    uil1=Label(w15,text="Click the below link for more updates",font="Timesnewroman 30").place(x=400,y=100)
    uib=Button(w15,text="Instagram",font="Timesnewroman 20",command=ui,bg="white",fg="black").place(x=800,y=350)
    b2=Button(w15,text="Cancel",font="TimesNewRoman 20",command=w15.destroy,bg="white",fg="black")
    b2.place(x=500,y=350)
def ufb():
    w16=Tk()
    w16.title("Facebook")
    w16.geometry("1900x2000")        
    w16.config(bg="#0066FF")
    ufbl=Label(w16,text="Facebook Information & updates",font="Timesnewroman 30 bold",bg="black",fg="white").pack(fill="x")
    ub=Button(w16,text="Facebook",font="Timesnewroman 20",command=uf,bg="white",fg="black").place(x=800,y=350)          
    ufbl1=Label(w16,text="Click the below link for more updates",font="Timesnewroman 30").place(x=400,y=100)
    b2=Button(w16,text="Cancel",font="TimesNewRoman 20",command=w16.destroy,bg="white",fg="black")
    b2.place(x=500,y=350)       
def uwa():
    w17=Tk()
    w17.title("Whatsapp")
    w17.geometry("1900x2000")
    w17.config(bg="#3AA655")
    uwl=Label(w17,text="Whatsapp Information & updates",font="Timesnewroman 30 bold",bg="black",fg="white").pack(fill="x")
    uwl1=Label(w17,text="Click the below link for more updates",font="Timesnewroman 30").place(x=400,y=100)
    uwb=Button(w17,text="Whatsapp",font="Timesnewroman 20",command=uw,bg="white",fg="black").place(x=800,y=350)
    b2=Button(w17,text="Cancel",font="TimesNewRoman 20",command=w17.destroy,bg="white",fg="black")
    b2.place(x=500,y=350) 
def utw():
    w18=Tk()
    w18.title("Twitter")
    w18.geometry("1900x2000")
    w18.config(bg="#4997D0")
    utl=Label(w18,text="Twitter Information & updates",font="Timesnewroman 30 bold",bg="black",fg="white").pack(fill="x")
    utl1=Label(w18,text="Click the below link for more updates",font="Timesnewroman 30").place(x=400,y=100)
    utb=Button(w18,text="Twitter",font="Timesnewroman 20",command=ut,bg="white",fg="black").place(x=800,y=350)
    b2=Button(w18,text="Cancel",font="TimesNewRoman 20",command=w18.destroy,bg="white",fg="black")
    b2.place(x=500,y=350)
    
def aedu():
    w14=Tk()
    w14.geometry("1900x2000")
    w14.title("Education Page-Admin")
    w14.config(bg="#ACACE6")
    l1=Label(w14,text="Education Page-Admin",font="TimesNewRoman 30 bold",bg="black",fg="white").pack(fill="x")
    al1=Label(w14,text="Click the below link for more updates",font="Timesnewroman 30").place(x=400,y=100)
    b1=Button(w14,text="Education",font="TimesNewRoman 20",command=edu,bg="white",fg="black")
    b1.place(x=800,y=350)
    b2=Button(w14,text="Cancel",font="TimesNewRoman 20",command=w14.destroy,bg="white",fg="black")
    b2.place(x=500,y=350)

def ahealth():
    w13=Tk()
    w13.geometry("1900x2000")
    w13.title("Health Page-Admin")
    w13.config(bg="#ACACE6")
    l1=Label(w13,text="HealthPage-Admin",font="TimesNewRoman 30 bold",bg="black",fg="white").pack(fill="x")
    ahl1=Label(w13,text="Click the below link for more updates",font="Timesnewroman 30").place(x=400,y=100)
    b1=Button(w13,text="Health",font="TimesNewRoman 20",command=he,bg="white",fg="black")
    b1.place(x=800,y=350)
    b2=Button(w13,text="Cancel",font="TimesNewRoman 20",command=w13.destroy,bg="white",fg="black")
    b2.place(x=500,y=350)

def atech():
    w12=Tk()
    w12.geometry("1900x2000")
    w12.title("Technology Page-Admin")
    w12.config(bg="#ACACE6")
    l1=Label(w12,text="Technology Page-Admin",font="TimesNewRoman 30 bold",bg="black",fg="white").pack(fill="x")
    atl1=Label(w12,text="Click the below link for more updates",font="Timesnewroman 30").place(x=400,y=100)
    b1=Button(w12,text="Technology",font="TimesNewRoman 20",command=tech,bg="white",fg="black")
    b1.place(x=800,y=350)
    b2=Button(w12,text="Cancel",font="TimesNewRoman 20",command=w12.destroy)
    b2.place(x=500,y=350)

def asoc():
    w11=Tk()
    w11.geometry("1900x2000")
    w11.title("Social Media Page-Admin")
    w11.config(bg="#ACACE6")
    l1=Label(w11,text="Social Media Page-Admin",font="TimesNewRoman 30 bold",bg="black",fg="white").pack(fill="x")
    ib2=Button(w11,text="Instagram",font="TimesNewRoman 20",command=ainsta,bg="#EE34D2",fg="white")
    ib2.place(x=700,y=100)

    fb2=Button(w11,text="Facebook",font="TimesNewRoman 20",command=afb,bg="#0066FF",fg="white")
    fb2.place(x=700,y=200)
 
    tb2=Button(w11,text="   Twitter  ",font="TimesNewRoman 20",command=atw,bg="#4997D0",fg="white")
    tb2.place(x=700,y=300)
 
    wb2=Button(w11,text="Whatsapp",font="TimesNewRoman 20",command=awa,bg="#3AA655",fg="white")
    wb2.place(x=700,y=400)
   
    
    b1=Button(w11,text="Cancel",font="TimesNewRoman 20",command=w11.destroy,bg="white",fg="black")
    b1.place(x=720,y=500)

def uedu():
    w10=Tk()
    w10.geometry("1500x800")
    w10.title("Education Page-User")
    w10.config(bg="#ACACE6")
    l1=Label(w10,text="Education Page-User",font="TimesNewRoman 30 bold",bg="black",fg="white").pack(fill="x")
    uel1=Label(w10,text="Click the below link for more updates",font="Timesnewroman 30").place(x=400,y=100)
    b1=Button(w10,text="Education",font="TimesNewRoman 20",command=edu,bg="white",fg="black")
    b1.place(x=800,y=350)
    b2=Button(w10,text="Cancel",font="TimesNewRoman 20",command=w10.destroy,bg="white",fg="black")
    b2.place(x=500,y=350)

def uhealth():
    w9=Tk()
    w9.geometry("1900x2000")
    w9.title("Health Page-User")
    w9.config(bg="#ACACE6")
    l1=Label(w9,text="Health Page-User",font="TimesNewRoman 30 bold",bg="black",fg="white").pack(fill="x")
    uhl1=Label(w9,text="Click the below link for more updates",font="Timesnewroman 30").place(x=400,y=100)
    b1=Button(w9,text="Health",font="TimesNewRoman 20",command=he,bg="white",fg="black")
    b1.place(x=800,y=350)
    b2=Button(w9,text="Cancel",font="TimesNewRoman 20",command=w9.destroy,bg="white",fg="black")
    b2.place(x=500,y=350)

def utech():
    w8=Tk()
    w8.geometry("1900x2000")
    w8.title("Technology Page-User")
    w8.config(bg="#ACACE6")
    l1=Label(w8,text="Technology Page-User",font="TimesNewRoman 30 bold",bg="black",fg="white").pack(fill="x")
    b1=Button(w8,text="Technology",font="TimesNewRoman 20",command=tech,bg="white",fg="black")
    b1.place(x=800,y=350)
    utl1=Label(w8,text="Click the below link for more updates",font="Timesnewroman 30").place(x=400,y=100)
    b2=Button(w8,text="Cancel",font="TimesNewRoman 20",bg="white",fg="black",command=w8.destroy)
    b2.place(x=500,y=350)

def usoc():
    w7=Tk()
    w7.geometry("1900x2000")
    w7.title("Social Media Page-User")
    w7.config(bg="#ACACE6")
    l1=Label(w7,text="Social Media Page-User",font="TimesNewRoman 30 bold",bg="black",fg="white").pack(fill="x")
    
    ib1=Button(w7,text="Instagram",font="TimesNewRoman 20",bg="#EE34D2",fg="white",command=uinsta)
    ib1.place(x=650,y=200)

    fb1=Button(w7,text="Facebook",font="TimesNewRoman 20",command=ufb,bg="#0066FF",fg="white")
    fb1.place(x=650,y=300)
   
    tb1=Button(w7,text="   Twitter  ",font="TimesNewRoman 20",command=utw,bg="#4997D0",fg="white")
    tb1.place(x=650,y=400)
   
    wb1=Button(w7,text="Whatsapp",font="TimesNewRoman 20",command=uwa,bg="#3AA655",fg="white")
    wb1.place(x=650,y=500)
   
    
    b1=Button(w7,text="Cancel",font="TimesNewRoman 20",command=w7.destroy,bg="white",fg="black")
    b1.place(x=670,y=600)




def AWelcome():
    global se,sp,le,lp,we
    se=e4.get()
    sp=e5.get()
    le=mail.get()
    lp=pas.get()
    if se==le and sp==lp:
        w6=Tk()
        w6.geometry("1900x2000")
        w6.title("Search My Directory")
        w6.config(bg="#ACACE6")
        l1=Label(w6,text="Search My Directory",font="TimesNewRoman 30 bold",bg="black",fg="white").pack(fill="x")
        word1=Label(w6,text="Enter the Word :",font="TimesNewRoman 20 bold",bg="white",fg="black").place(x=350,y=111)
        we=Entry(w6,width=50,font="TimesNewRoman 20")
        we.place(x=600,y=114,width=300)
        
        sb=Button(w6,text="Search",font="TimesNewRoman 20",bg="white",fg="black",command=asearch)
        sb.place(x=920,y=105)
        b1=Button(w6,text="Social Media",font="TimesNewRoman 20",bg="white",fg="black",command=asoc)
        b1.place(x=600,y=250)
        b2=Button(w6,text=" Technology ",font="TimesNewRoman 20",bg="white",fg="black",command=atech)
        b2.place(x=600,y=350)
        b3=Button(w6,text="    Health     ",font="TimesNewRoman 20",bg="white",fg="black",command=ahealth)
        b3.place(x=600,y=450)
        b4=Button(w6,text="  Education  ",font="TimesNewRoman 20",bg="white",fg="black",command=aedu)
        b4.place(x=600,y=550)
        b5=Button(w6,text="Cancel",font="TimesNewRoman 20",command=w6.destroy,bg="white",fg="black")
        b5.place(x=620,y=650)

    else:
        l=Label(w4,text="Incorrect Password or Email ID",font="TimesNewRoman 15",fg="red")
        l.place(x=300,y=300)

def UWelcome():
    #e1,e2,mail,psw
    global se,sp,le,lp,se
    se=e4.get()
    sp=e5.get()
    le=mail.get()
    lp=pas.get()
    if se==le and sp==lp:
        w5=Tk()
        w5.geometry("1900x2000")
        w5.title("Search My Directory-User")
        w5.config(bg="#ACACE6")
        l1=Label(w5,text="Search My Directory-User",font="TimesNewRoman 30 bold",bg="black",fg="white").pack(fill="x")
        word=Label(w5,text="Enter the Word :",font="TimesNewRoman 20 bold",bg="white",fg="black").place(x=280,y=111)
        se=Entry(w5,width=20,font="TimesNewRoman 20")
        se.place(x=550,y=112)
        eb=Button(w5,text="Search",font="TimesNewRoman 20",command=usearch,bg="white",fg="black")
        eb.place(x=900,y=100)   
        b1=Button(w5,text="Social Media",font="TimesNewRoman 20",command=usoc,bg="white",fg="black")
        b1.place(x=600,y=200)
        b2=Button(w5,text=" Technology ",font="TimesNewRoman 20",command=utech,bg="white",fg="black")
        b2.place(x=600,y=300)
        b3=Button(w5,text="     Health     ",font="TimesNewRoman 20",command=uhealth,bg="white",fg="black")
        b3.place(x=600,y=400)
        b4=Button(w5,text="   Education  ",font="TimesNewRoman 20",command=uedu,bg="white",fg="black")
        b4.place(x=600,y=500)
        b5=Button(w5,text="Cancel",font="TimesNewRoman 20",command=w5.destroy,bg="white",fg="black")
        b5.place(x=650,y=600)
    else:
        l=Label(w1,text="Incorrect Password or Email ID",font="TimesNewRoman 15",fg="red")
        l.place(x=300,y=300)
   

def ALogin():
    global mail,pas,w1,w4
    w4=Tk()
    w4.geometry("1900x2000")
    w4.title("Admin Login Page")
    w4.config(bg="#ACACE6")
    l1=Label(w4,text="Admin Login Page",font="TimesNewRoman 30 bold",bg="black",fg="white").pack(fill="x")
    l2=Label(w4,text="E-Mail ID :",font="TimesNewRoman 20",bg="white",fg="black")
    l2.place(x=50,y=100)
    mail=Entry(w4,width=30,font="TimesNewRoman 20 bold")
    mail.place(x=199,y=107)
    l3=Label(w4,text="Password :",font="TimesNewRoman 20",bg="white",fg="black")
    l3.place(x=50,y=200)
    pas=Entry(w4,width=30,show="*",font="TimesNewRoman 20 bold")
    pas.place(x=199,y=207)
    b1=Button(w4,text="Cancel",font="TimesNewRoman 20",command=w4.destroy,width=10,bg="white",fg="black")
    b1.place(x=200,y=400)
    b2=Button(w4,text="Login",font="TimesNewRoman 20",command=AWelcome,width=10,bg="white",fg="black")
    b2.place(x=500,y=400)
        
def ASignUp():
    global e4,e5
    w2=Tk()
    w2.title("Admin SignUp Page")
    w2.geometry("1900x2000")
    w2.config(bg="#ACACE6")
    l1=Label(w2,text="Admin SignUp Page",font="TimesNewRoman 30 bold",bg="black",fg="white").pack(fill="x")
    l2=Label(w2,text="Name :",font="TimesNewRoman 20 ",bg="white",fg="black")
    l2.place(x=50,y=100)
    e1=Entry(w2,width=20,font="TimesNewRoman 20 ")
    e1.place(x=300,y=107)
    l3=Label(w2,text="Age :",font="TimesNewRoman 20",bg="white",fg="black")
    l3.place(x=50,y=200)
    e2=Entry(w2,width=20,font="TimesNewRoman 20 ")
    e2.place(x=300,y=207)
    l4=Label(w2,text="Mobile Number :",font="TimesNewRoman 20",bg="white",fg="black")
    l4.place(x=50,y=300)
    e3=Entry(w2,width=20,font="TimesNewRoman 20 ")
    e3.place(x=300,y=307)
    l5=Label(w2,text="E-Mail ID :",font="TimesNewRoman 20",bg="white",fg="black")
    l5.place(x=50,y=400)
    e4=Entry(w2,width=20,font="TimesNewRoman 20 ")
    e4.place(x=300,y=407)
    l6=Label(w2,text="Password :",font="TimesNewRoman 20",bg="white",fg="black")
    l6.place(x=50,y=500)
    e5=Entry(w2,show="*",width=20,font="TimesNewRoman 20 ")
    e5.place(x=300,y=507)
    b1=Button(w2,text="Cancel",font="TimesNewRoman 20",command=w2.destroy,width=10,bg="white",fg="black")
    b1.place(x=200,y=600)
    b2=Button(w2,text="Sign Up",font="TimesNewRoman 20",command=ALogin,width=10,bg="white",fg="black")
    b2.place(x=550,y=600)


def ULogin():
    global mail,pas,w1
    w1=Tk()
    w1.geometry("1900x2000")
    w1.title("User Login Page")
    w1.config(bg="#ACACE6")
    l1=Label(w1,text="User Login Page",font="TimesNewRoman 30 bold",bg="black",fg="white").pack(fill="x")
    l2=Label(w1,text="E-Mail ID :",font="TimesNewRoman 20",bg="white",fg="black")
    l2.place(x=50,y=100)
    mail=Entry(w1,width=20,font="TimesNewRoman 20")
    mail.place(x=250,y=107)
    l3=Label(w1,text="Password :",font="TimesNewRoman 20",bg="white",fg="black")
    l3.place(x=50,y=200)
    pas=Entry(w1,width=20,show="*",font="TimesNewRoman 20")
    pas.place(x=250,y=207)
    b1=Button(w1,text="Cancel",font="TimesNewRoman 20",command=w1.destroy,width=10,bg="white",fg="black")
    b1.place(x=200,y=400)
    b2=Button(w1,text="Login",font="TimesNewRoman 20",command=UWelcome,width=10,bg="white",fg="black")
    b2.place(x=500,y=400)


def USignUp():
    global e4,e5
    w=Tk()
    w.title("User SignUp Page")
    w.geometry("1900x2000")
    w.config(bg="#ACACE6")
    l1=Label(w,text="User SignUp Page",font="TimesNewRoman 30 bold",bg="black",fg="white").pack(fill="x")
    l2=Label(w,text="Name :",font="TimesNewRoman 20 ",bg="white",fg="black")
    l2.place(x=50,y=100)
    e1=Entry(w,width=20,font="TimesNewRoman 20")
    e1.place(x=300,y=107)
    l3=Label(w,text="Age :",font="TimesNewRoman 20",bg="white",fg="black")
    l3.place(x=50,y=200)
    e2=Entry(w,width=20,font="TimesNewRoman 20")
    e2.place(x=300,y=207)
    l4=Label(w,text="Mobile Number :",font="TimesNewRoman 20",bg="white",fg="black")
    l4.place(x=50,y=300)
    e3=Entry(w,width=20,font="TimesNewRoman 20")
    e3.place(x=300,y=307)
    l5=Label(w,text="E-Mail ID :",font="TimesNewRoman 20",bg="white",fg="black")
    l5.place(x=50,y=400)
    e4=Entry(w,width=20,font="TimesNewRoman 20")
    e4.place(x=300,y=407)
    l6=Label(w,text="Password :",font="TimesNewRoman 20",bg="white",fg="black")
    l6.place(x=50,y=500)
    e5=Entry(w,show="*",width=20,font="TimesNewRoman 20")
    e5.place(x=300,y=507)
    b1=Button(w,text="Cancel",font="TimesNewRoman 20",width=15,command=w.destroy,bg="white",fg="black")
    b1.place(x=200,y=600)
    b2=Button(w,text="Sign Up",font="TimesNewRoman 20",width=15,command=ULogin,bg="white",fg="black")
    b2.place(x=500,y=600)

#f-first page
f=Tk()
f.title("First page")
f.geometry("1900x2000")
f.config(bg="#ACACE6")
l1=Label(f,text="Are you here as an User or Admin? ",font="TimesNewRoman 30 bold ",bg="black",fg="white").pack(fill="x")
b1=Button(f,text="USER",width=15,font="TimesNewRoman 20",command=USignUp,bg="white",fg="black")
b1.place(x=450,y=270)
b2=Button(f,text="ADMIN",width=15,font="TimesNewRoman 20",command=ASignUp,bg="white",fg="black")
b2.place(x=800,y=270)
f.mainloop()
































