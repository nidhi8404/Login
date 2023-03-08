from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql


#Functionality Part

def forget_pass():
    def change_password():
        if userentry.get()=='' or newpassentry.get()=='' or confirmpassentry.get()=='':
            messagebox.showerror('Error','All fields are Required',parent=window)
        elif newpassentry.get()!=confirmpassentry.get():
            messagebox.showerror('Error','Password and Confirm Password are not mmatching',paren=window)
        else:
            con=pymysql.connect(host='localhost',user='root',password='Nidhi123*',database='userdata')
            mycursor=con.cursor()
            query='select * from data where username=%s'
            mycursor.execute(query,(userentry.get()))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror('Error','Incorrect Username',parent=window)
            else:
                query='update data set password=%s where username=%s'
                mycursor.execute(query,(newpassentry.get(),userentry.get()))
                con.commit()
                con.close()
                messagebox.showerror('Success','Password is Reset',parent=window)
                window.destroy()
            
    window =Toplevel()
    window.resizable(0,0)
    window.title("Change Password")

    bgImage=ImageTk.PhotoImage(file='bg.jpg')
    bgLabel=Label(window,image=bgImage)
    bgLabel.grid(row=0,column=0)

    heading=Label(window,text='Reset Password',font=('Arial',22,"bold"),bg='white',fg='darkviolet')
    heading.place(x=405,y=70)

    userLabel=Label(window,text='Username',font=('arial',12,'bold'),bg='white',fg='blueviolet')
    userLabel.place(x=400,y=130)

    userentry=Entry(window,width=30,fg='darkviolet',font=('arial',11,'bold'),bd=0)
    userentry.place(x=400,y=155)

    Frame(window,width=250,height=2,bg='blueviolet').place(x=400,y=175)

    passwordLabel=Label(window,text='New Password',font=('arial',12,'bold'),bg='white',fg='blueviolet')
    passwordLabel.place(x=400,y=190)

    newpassentry=Entry(window,width=30,fg='darkviolet',font=('arial',11,'bold'),bd=0)
    newpassentry.place(x=400,y=215)

    Frame(window,width=250,height=2,bg='blueviolet').place(x=400,y=235)

    cpasswordLabel=Label(window,text='Confirm Password',font=('arial',12,'bold'),bg='white',fg='blueviolet')
    cpasswordLabel.place(x=400,y=250)

    confirmpassentry=Entry(window,width=30,fg='darkviolet',font=('arial',11,'bold'),bd=0)
    confirmpassentry.place(x=400,y=275)

    Frame(window,width=250,height=2,bg='blueviolet').place(x=400,y=295)

    submitButton=Button(window,text='Submit',font=('Open Sans',14,'bold'),activeforeground='white',activebackground='blueviolet',
                       bd=0,width=20,fg='white',bg='blueviolet',command=change_password)
    submitButton.place(x=400,y=320)



    window.mainloop()


def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All Fields are Required')

    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='Nidhi123*')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Connection is not established')
            return
        
        query = 'use userdata'
        mycursor.execute(query)
        query='select * from data where username=%s and password=%s'
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Invalid username or Password')
        else:
            messagebox.showinfo('Welcome','Login is sucessful')


def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)

def hide():
    openeye.config(file='close-eye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='open-eye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

def newacc():
    loginpage.destroy()
    import signup

#GUI part
loginpage=Tk()
loginpage.geometry('800x450+50+50')
loginpage.resizable(0,0)
loginpage.title('Login Page')

bgImage=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(loginpage,image=bgImage)
bgLabel.grid(row=0,column=0)

heading=Label(loginpage,text='USER LOGIN',font=('Arial',25,"bold"),bg='white',fg='blue4')
heading.place(x=400,y=70)

usernameEntry=Entry(loginpage,width=30,font=('Arial',11,"bold"),bd=0,fg='blue4')
usernameEntry.place(x=400,y=150)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>',user_enter)

Frame(loginpage,width=250,height=2,bg='pink').place(x=400,y=172)

passwordEntry=Entry(loginpage,width=20,font=('Arial',11,"bold"),bd=0,fg='blue4')
passwordEntry.place(x=400,y=210)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',password_enter)

Frame(loginpage,width=250,height=2,bg='pink').place(x=400,y=232)

openeye=PhotoImage(file='open-eye.png')
eyeButton=Button(loginpage,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=608,y=204)

forgetButton=Button(loginpage,text='Forget Password?',bd=0,bg='white',
activeforeground='blue4',activebackground='white',cursor='hand2',font=('Arial',9,"bold"),fg='blue4',command=forget_pass)
forgetButton.place(x=545,y=240)

loginButton=Button(loginpage,text='Login',font=('Open Sans',14,'bold'),activeforeground='white',activebackground='blue4',
bd=0,width=20,fg='white',bg='blue4',command=login_user)
loginButton.place(x=400,y=265)

orLabel=Label(loginpage,text='------------------OR------------------',font=('Open Sans',9,'bold'),fg='blue4',bg='white')
orLabel.place(x=435 ,y=300)

GButton=Button(loginpage,text='Continue with Google?',font=('Open Sans',9,'bold'),fg='blue4',bd=0,bg='white',
activeforeground='blue4',activebackground='white')
GButton.place(x=450 ,y=320)
#GButton=PhotoImage(file='gmail.png')

signLabel=Label(loginpage,text='Dont have an account?',font=('Open Sans',9,'bold'),fg='blue4',bg='white')
signLabel.place(x=400 ,y=340)

newaccButton=Button(loginpage,text='Create new one',font=('Open Sans',9,'bold underline'),activeforeground='blue4',activebackground='white',
bd=0,width=15,fg='blue4',bg='white',command=newacc)
newaccButton.place(x=550,y=340)


loginpage.mainloop()
