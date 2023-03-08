from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def clear():
   emailEntry.delete(0,END)
   usernameEntry.delete(0,END)
   passwordEntry.delete(0,END)
   confirmpasswordEntry.delete(0,END)
   check.set(0)

   
def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or confirmpasswordEntry.get()=='':
       messagebox.showerror('Error','All Fields Are Required')
    elif passwordEntry.get() != confirmpasswordEntry.get():
       messagebox.showerror('Error','Password Mismatched')
    elif check.get()==0:
       messagebox.showerror('Error','Please Accept Terms and Conditions')
    else:
       try:
          con=pymysql.connect(host='localhost',user='root',password='Nidhi123*')
          mycursor=con.cursor()
       except:
          messagebox.showerror('Error','Database Connectivity Issue')
          return
       
       try:
          query='create database userdata'
          mycursor.execute(query)
          query='use userdata'
          mycursor.execute(query)
          query='create table data(id int auto_increment primary key not null,email varchar(50),username varchar(100),password varchar(20))'
          mycursor.execute(query)
       except:
        mycursor.execute('use userdata') 

       query='insert into data(email,username,password) values(%s,%s,%s)'
       mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
       con.commit()
       con.close()
       messagebox.showinfo('Success','Registation is Successful')
       clear()
       signup_window.destroy()
       import signpage


def loginpage():
    signup_window.destroy()
    import signpage

signup_window=Tk()
signup_window.title('Signup Page')
signup_window.resizable(False,False)

background=ImageTk.PhotoImage(file='bg.jpg')


bgLabel=Label(signup_window,image=background)
bgLabel.grid(row=0,column=0)


frame=Frame(signup_window,bg='white')
frame.place(x=400,y=70)

heading=Label(frame,text='CREATE AN ACCOUNT',font=('Arial',16,"bold"),bg='white',fg='blue4')
heading.grid(row=0,column=0,padx=10,pady=5)

emailLabel=Label(frame,text='Email',font=('Arial',10,'bold'),bg='white',fg='blue4')
emailLabel.grid(row=1,column=0,sticky='w',padx=25)

emailEntry=Entry(frame,width=30,font=('Arial',10,'bold'),fg='white',bg='blue4')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)

usernameLabel=Label(frame,text='Username',font=('Arial',10,'bold'),bg='white',fg='blue4')
usernameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(2,0))

usernameEntry=Entry(frame,width=30,font=('Arial',10,'bold'),fg='white',bg='blue4')
usernameEntry.grid(row=4,column=0,sticky='w',padx=25)

passwordLabel=Label(frame,text='Password',font=('Arial',10,'bold'),bg='white',fg='blue4')
passwordLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(2,0))

passwordEntry=Entry(frame,width=30,font=('Arial',10,'bold'),fg='white',bg='blue4')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)

confirmpasswordLabel=Label(frame,text='Confirm Password',font=('Arial',10,'bold'),bg='white',fg='blue4')
confirmpasswordLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(2,0))

confirmpasswordEntry=Entry(frame,width=30,font=('Arial',10,'bold'),fg='white',bg='blue4')
confirmpasswordEntry.grid(row=8,column=0,sticky='w',padx=25)

check=IntVar()
tc=Checkbutton(frame,text='I agree to the Terms & conditions',font=('Arial',9,'bold'),bg='white',fg='blue4',
               activebackground='white',activeforeground='blue4',cursor='hand2',variable=check)
tc.grid(row=9,column=0,padx=15,pady=2)

signupButton=Button(frame,text='Sign Up',font=('Open Sans',14,'bold'),activeforeground='white',activebackground='blue4',
bd=0,width=18,fg='white',bg='blue4',command=connect_database)
signupButton.grid(row=10,column=0,pady=2)

signLabel=Label(frame,text='Dont have an account?',font=('Open Sans',9,'bold'),fg='blue4',bg='white')
signLabel.grid(row=11,column=0,sticky='w',padx=25,pady=2)

loginButton=Button(frame,text='Log in',font=('Open Sans',9,'bold underline'),activeforeground='blue4',activebackground='white',
bd=0,width=12,fg='blue4',bg='white',command=loginpage)
loginButton.grid(row=11,column=0,sticky='e')

signup_window.mainloop()