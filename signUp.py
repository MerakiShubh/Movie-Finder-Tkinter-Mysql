from tkinter import  *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def clear():
    emailEntry.delete(0, END)
    userEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confirmEntry.delete(0, END)
    check.set(0)

    
def SignIN():
    signp_window.destroy()
    import SignIN


# Database Connection 
def connect_database():
    if emailEntry.get()=='' or userEntry.get()=='' or passwordEntry.get()=='' or confirmEntry.get=='':
        messagebox.showerror('Error', 'All Fields Are Required')
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error', 'Password Mismatch')
    elif check.get()==0:
        messagebox.showerror('Error', 'Please Accept the Terms & Condtions')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='meraki' )
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error', 'Database Connectivity Issue, Please Try Again')
            return 
    try:
        query='create database JustMovies'
        mycursor.execute(query)
        query='use JustMovies'
        mycursor.execute(query)
        query='create table data(id int auto_increment key not null, email varchar(50), username varchar(100), password varchar(20))'
        mycursor.execute(query)
    
    except:
        mycursor.execute('use JustMovies')
    
    query='insert into data(email, username, password) values(%s, %s, %s)'
    mycursor.execute(query, (emailEntry.get(), userEntry.get(), passwordEntry.get()))
    con.commit()
    con.close()
    messagebox.showinfo('Success', 'Registration is Successful')
    clear()

        
       

 

signp_window=Tk()
signp_window.title('SignUp Page')

# Overview Section 

signp_window.resizable(False, False)
background=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(signp_window, image=background)
bgLabel.grid()

frame=Frame(signp_window, bg='white')
frame.place(x=554, y=100)

heading = Label(frame, text='CREATE AN ACCOUNT', font=(
    'Microsoft Yahi UI Light', 18, 'bold'), bg='white',  fg='firebrick1')
heading.grid(row=0, column=0, padx=10, pady=10)

# Hero Section 

# Email Section 
emaiLabel = Label(frame,text='Email', font=('Microsoft Yahi UI Light',10, 'bold'), bg='white', fg='firebrick1')
emaiLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10, 0) )
emailEntry=Entry(frame, width=30, font=('Microsoft Yahi UI Light', 10, 'bold'),
                 fg='white', bg='firebrick1')
emailEntry.grid(row=2, column=0, sticky='w', padx=25)


# UserName

userNameLabel = Label(frame,text='Username', font=('Microsoft Yahi UI Light',10, 'bold'), bg='white', fg='firebrick1')
userNameLabel.grid(row=3, column=0, sticky='w', padx=25,pady=(10, 0) )
userEntry=Entry(frame, width=30, font=('Microsoft Yahi UI Light', 10, 'bold'),
                 fg='white', bg='firebrick1')
userEntry.grid(row=4, column=0, sticky='w', padx=25)


# Password 


passwordLabel = Label(frame,text='Password', font=('Microsoft Yahi UI Light',10, 'bold'), bg='white', fg='firebrick1')
passwordLabel.grid(row=5, column=0, sticky='w', padx=25,pady=(10, 0) )
passwordEntry=Entry(frame, width=30, font=('Microsoft Yahi UI Light', 10, 'bold'),
                 fg='white', bg='firebrick1')
passwordEntry.grid(row=6, column=0, sticky='w', padx=25)


# Confirmation section 

confirmLabel = Label(frame,text='Confirm password', font=('Microsoft Yahi UI Light',10, 'bold'), bg='white', fg='firebrick1')
confirmLabel.grid(row=7, column=0, sticky='w', padx=25,pady=(10, 0) )
confirmEntry=Entry(frame, width=30, font=('Microsoft Yahi UI Light', 10, 'bold'),
                 fg='white', bg='firebrick1')
confirmEntry.grid(row=8, column=0, sticky='w', padx=25)

# CheckButton 

check=IntVar()
termsandcondition=Checkbutton(frame, text='I agree to the Terms & Conditons', font=('Microsoft Yahi UI Light',10, 'bold'), fg='firebrick', bg='white', activebackground='white', activeforeground='firebrick1', cursor='hand2', variable=check)
termsandcondition.grid(row=9, column=0, pady=10, padx=15)

# SignUp Button

signUpButton=Button(frame, text='Signup', font=('Open Sans',16, 'bold'), bd=0, bg='firebrick1', fg='white',
activebackground='firebrick1', activeforeground='white', width=17, command=connect_database)
signUpButton.grid(row=10, column=0, padx=10)

# AlreadyAccout

alreadyaccount=Label(frame, text="Don't have an account?", font=('Open Sans', 9, 'bold'), bg='white', fg='firebrick1')
alreadyaccount.grid(row=11, column=0, sticky='w', padx=25, pady=10)

# LoginButton 

loginButton=Button(frame, text='Log in', font=('Open Sans', 9, 'bold underline'), bg='white', fg='blue', bd=0, cursor='hand2', activebackground='white', 
activeforeground='blue', command=SignIN)
loginButton.grid(row=12, column=0)

# Movie button 

# MovieButton=Button(frame, text='Search Movies', font=('Open Sans',16, 'bold'), bd=0, bg='firebrick1', fg='white',
# activebackground='firebrick1', activeforeground='white', width=17, command=movies_button)
# signUpButton.grid(row=13, column=0, padx=10)

signp_window.mainloop()
