from tkinter import *
import webbrowser
from tkinter import font
from PIL import ImageTk

# Function part
#secondary window


def gohome():
    loginwindow.destroy()
    import Movies

def signUp():
    loginwindow.destroy()
    import signUp


def user_enter(event):
    if usernameEntry.get() == "Username":
        usernameEntry.delete(0, END)


def password_enter(event):
    if usernameEntry.get() == "Password":
        usernameEntry.delete(0, END)


def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)


def show():
    openeye.config(file='openeye.png')
    passwordEntry.confing(command=hide)


# GUI Part
loginwindow = Tk()
# Window size
loginwindow.geometry('990x660+50+50')

# Fixing window size
loginwindow.resizable(0, 0)
loginwindow.title('Movie Finder Login Page')
bgImage = ImageTk.PhotoImage(file='bg.jpg')
bgLable = Label(loginwindow, image=bgImage)
bgLable.place(x=0, y=0)
heading = Label(loginwindow, text='USER LOGIN', font=(
    'Microsoft Yahi UI Light', 23, 'bold'), bg='white',  fg='firebrick1')
heading.place(x=605, y=120)

# User Details

usernameEntry = Entry(loginwindow, width=25, font=(
    'Microsoft Yahi UI Light', 11, 'bold'), bd=0, fg='firebrick1')
usernameEntry.place(x=580, y=200)
usernameEntry.insert(0, 'Username')
usernameEntry.bind('<FocusIn>', user_enter)


frame1 = Frame(loginwindow, width=250, height=2, bg='firebrick1')
frame1.place(x=580, y=222)


# Password Details

passwordEntry = Entry(loginwindow, width=25, font=(
    'Microsoft Yahi UI Light', 11, 'bold'), bd=0, fg='firebrick1')
passwordEntry.place(x=580, y=260)
passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>', password_enter)

frame1 = Frame(loginwindow, width=250, height=2, bg='firebrick1')
frame1.place(x=580, y=282)

openeye = PhotoImage(file='openeye.png')
eyeButton = Button(loginwindow, image=openeye, bd=0, bg='white',
                   activebackground='white', cursor='hand2', command=hide)
eyeButton.place(x=800, y=255)



# Forgot Button

forgetButton = Button(loginwindow, text='Forgot Password?', bd=0, bg='white',
                      activebackground='white', cursor='hand2', font=('Microsoft Yahi UI Light', 9, 'bold'), fg='firebrick1', activeforeground='firebrick1')
forgetButton.place(x=715, y=295)

# Login Button

loginButton = Button(loginwindow, text='Login', font=('Open Sans', 16, 'bold'),
                     fg='white', bg='firebrick1', activebackground='white', activeforeground='firebrick1', cursor='hand2', bd=0, width=19, command=gohome)
loginButton.place(x=578, y=350)


orLabel = Label(loginwindow, text='--------------- OR ---------------', font=('Open Sans', 16), fg='firebrick1', bg='white')
orLabel.place(x=583, y=400)

facebook_logo=PhotoImage(file='facebook.png')
fbLabel = Label(loginwindow, image=facebook_logo, bg='white')
fbLabel.place(x=649, y=440)


google_logo=PhotoImage(file='google.png')
googleLabel = Label(loginwindow, image=google_logo, bg='white')
googleLabel.place(x=690, y=440)


twitter_logo=PhotoImage(file='twitter.png')
twitterLabel = Label(loginwindow, image=facebook_logo, bg='white')
twitterLabel.place(x=740, y=440)


signupLabel = Label(loginwindow, text='Dont have an accout?', font=('Open Sans', 9, 'bold'), fg='firebrick1', bg='white')
signupLabel.place(x=570, y=500)


newaccontButton = Button(loginwindow, text='Create New One', font=('Open Sans', 9, 'bold underline'),
                     fg='blue', bg='white', activebackground='blue', activeforeground='white', cursor='hand2', bd=0, command=signUp)
newaccontButton.place(x=727, y=500)


# loginButton = Button(loginwindow, text='Search Movies', font=('Open Sans', 8, 'bold'),
#                      fg='white', bg='firebrick1', activebackground='white', activeforeground='firebrick1', cursor='hand2', bd=0, width=19,command=gohome)
# loginButton.place(x=570, y=500)

loginwindow.mainloop()
