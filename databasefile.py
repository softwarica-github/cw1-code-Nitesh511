
from tkinter import *
from computing import *
from PIL import ImageTk,Image
l=login()


def register_user():
    fullname_info=fullname.get()
    username_info = username.get()
    password_info = password.get()
    print(fullname_info,username_info,password_info)
    l.sign_up(fullname_info,username_info,password_info)

    Label(screen1, text="Registration Sucess", fg="green", font=("calibri", 11)).pack()
def login_user():
    username_info = signin_username.get()
    password_info = signin_password.get()
    if (l.user_login(username_info,password_info)):
        Label(screen1, text="Login Sucess", fg="green", font=("calibri", 11)).pack()
        open()
    else:
        Label(screen1, text="Login Failed", fg="red", font=("calibri", 11)).pack()

def customerinfo():
    phonenumber_info=cust_phonenumber.get()
    name_info = cust_name.get()
    gender_info = cust_gender.get()
    gmail_info = cust_gmail.get()
    if(l.customer_info(name_info,phonenumber_info,gmail_info,gender_info)):
        Label(screen1, text="Saved Sucessfully", fg="green", font=("calibri", 11)).place(x=150,y=220)
    else:
        Label(screen1, text="FAILED", fg="green", font=("calibri", 11)).pack()
def deleteuser():
    delete_id=delete_cid.get()
    if l.delete(delete_id) == True and delete_id != "":
        Label(screen1, text="Delete Sucessfully", fg="green", font=("calibri", 11)).place(x=150, y=290)
    else:
        Label(screen1, text="ID not found", fg="red", font=("calibri", 11)).place(x=150,y=320)
def show_user():
    l.showuser()





def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("400x400")
    screen1.config(background="lightblue")

    global username
    global password
    global fullname
    global username_entry
    global password_entry
    global fullname_entry
    fullname=StringVar()
    username = StringVar()
    password = StringVar()


    Label(screen1, text="Please enter details below",bg="lightblue").pack()
    Label(screen1, text="",bg="lightblue").pack()

    Label(screen1, text="Fullname * ",bg="lightblue").pack()
    fullname_entry = Entry(screen1, textvariable=fullname,bg="lightblue")
    fullname_entry.pack()
    Label(screen1, text="Username * ",bg="lightblue").pack()
    username_entry = Entry(screen1, textvariable=username,bg="lightblue")
    username_entry.pack()
    Label(screen1, text="Password * ",bg="lightblue").pack()
    password_entry = Entry(screen1, textvariable=password,bg="lightblue")
    password_entry.pack()
    Label(screen1, text="",bg="lightblue").pack()
    Button(screen1, text="Register", width=10, height=1, command=register_user).pack()


def login():
    global screen1
    global signin_username
    global signin_password
    screen1 = Toplevel(screen)
    screen1.title("Login")
    screen1.geometry("400x400")
    screen1.config(background="lightblue")


    signin_username = StringVar()
    signin_password = StringVar()

    Label(screen1, text="Please enter details below",bg="lightblue").pack()
    Label(screen1, text="",bg="lightblue").pack()

    Label(screen1, text="Username * ",bg="lightblue").pack()
    username_entry = Entry(screen1, textvariable=signin_username,bg="lightblue")
    username_entry.pack()
    Label(screen1, text="Password * ",bg="lightblue").pack()
    password_entry = Entry(screen1, textvariable=signin_password,bg="lightblue")
    password_entry.pack()
    Label(screen1, text="",bg="lightblue").pack()
    Button(screen1, text="Login", width=10, height=1,command=login_user).pack()
def open():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("400x400")
    screen1.config(background="lightyellow")
    global Adduser
    global Removeuser
    global showuser
    global Adduser_entry
    global Removeuser_entry
    global showuser_entry
    Adduser = StringVar()
    Removeuser= StringVar()
    showuser=StringVar()
    Label(screen1, text="Please enter details below",bg="lightyellow").pack()
    Label(screen1, text="").pack()
    Button(screen1,text="ADD USER",width="10",height="2",bg="green",command=details,font=("Calibri",13)).pack()
    Button(screen1, text="REMOVE USER", width="10", height="2",bg="red",command=details2, font=("Calibri", 13)).pack()
    Button(screen1, text="SHOW USER", width="10", height="2",bg="lightblue",command=show_user,font=("Calibri", 13)).pack()
    Label(screen1, text="").pack()

def details():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("400x400+0+0")
    screen1.config(background="lightblue")
    global cust_name
    global cust_phonenumber
    global cust_gmail
    global cust_gender
    global cust_name_entry
    global cust_phonenumber_entry
    global cust_gmail_entry
    global cust_gender_entry
    cust_name = StringVar()
    cust_phonenumber=StringVar()
    cust_gender= StringVar()
    cust_gmail = StringVar()
    Label(screen1, text="CUSTOMER NAME ", bg="lightblue").place(x=0,y=0)
    cust_name_entry = Entry(screen1, textvariable=cust_name, bg="lightblue")
    cust_name_entry.place(x=150,y=0)
    Label(screen1, text="PHONE NUMBER ", bg="lightblue").place(x=0, y=40)
    cust_phonenumber_entry = Entry(screen1, textvariable=cust_phonenumber, bg="lightblue")
    cust_phonenumber_entry.place(x=150, y=40)
    Label(screen1, text="G_Mail ", bg="lightblue").place(x=0, y=80)
    cust_gmail_entry = Entry(screen1, textvariable=cust_gmail, bg="lightblue")
    cust_gmail_entry.place(x=150, y=80)
    Label(screen1, text="GENDER", bg="lightblue").place(x=0, y=120)
    cust_gender_entry = Entry(screen1, textvariable=cust_gender, bg="lightblue")
    cust_gender_entry.place(x=150, y=120)
    Label(screen1, text="", bg="lightblue").pack()
    Button(screen1, text="Saved", width=10, height=1,bg='lightblue', command=customerinfo).place(x=150,y=190)



def details2():
    global screen1
    global delete_cid
    delete_cid=StringVar()
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("400x400+0+0")
    Label(screen1, text="Please enter costumer id  below", bg="lightyellow").pack()
    Label(screen1, text="").pack()
    label1 = Label(screen1, text="CUSTOMER_ID:", font=("arial", 15, "bold"), fg="black").place(x=0, y=20)
    user_id = StringVar()
    entry_box = Entry(screen1, textvariable=delete_cid, width=25, bg="lightgreen").place(x=180, y=30)


    Button(screen1, text="REMOVE", width="10", height="2", bg="RED",command=deleteuser,font=("Calibri", 13)).place(x=150, y=230)








def main_screen():#creating the main screen
    global screen
    screen = Tk()
    screen.geometry("400x400+0+0")
    screen.title("ManagementSystem")
    canvas=Canvas(screen,width=150,height=150,)#image place
    image=ImageTk.PhotoImage(Image.open("C:\\gui\\micky.png"))#importint a image from directory
    canvas.create_image(0,0,anchor=NW,image=image)
    canvas.pack()
    Label(text="Welcome", width="40", height="2",font=("Calibri",25)).pack()
    Label(text="").pack()
    Button(text="Login", bg="gray", height="3", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", bg="lightblue", height="3", width="30", command=register).pack()


    screen.mainloop()


main_screen()
