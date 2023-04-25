from tkinter import *
import webbrowser
from tkinter import font
from PIL import ImageTk

# MoviesSection 

def gohome():
     root = Toplevel(loginwindow)
     root.geometry("1000x600")
     root.minsize(1000, 600)
     root.maxsize(1000, 900)
     root.title("Movie Catalogue")
     root.configure(bg="#ECF2FF")
     # opening trailer
     def tr1():
         url = "https://youtu.be/TcMBFSGVi1c"
         webbrowser.open(url)
     def tr2():
         url = "https://youtu.be/wMrMKnoYWwA"
         webbrowser.open(url)
     def tr3():
         url = "https://youtu.be/vKQi3bBA1y8"
         webbrowser.open(url) 
     def tr4():
         url = "https://youtu.be/NmzuHjWmXOc"
         webbrowser.open(url)       
     def tr5():
         url = "https://youtu.be/XHhAG-YLdk8"
         webbrowser.open(url)    
        


     

     # NEED ENTER THE IMAGE HERE FOR LOGO
     # frame 2 horizontal frame starting
     f2 = Frame(root, relief=RIDGE, padx="10", bg="#EF4166", borderwidth=2, highlightcolor="brown")
     f2.pack(side="top", anchor="nw", fill="x")

     img = PhotoImage(file="reel.png")
     l1 = Label(f2, image=img, background="#EF4166")
     l1.pack(side="left")

     l2 = Label(f2, text="Movie Catalogue!", font="MERRIWEATHER 24 bold", bg="#EF4166", fg="#ffffff", padx=10, pady=10)
     l2.pack(side="left")

     ##Drop down menu wala list, horizontal
     f2 = Frame(root, borderwidth="7", bg="#ef4166", relief=FLAT, cursor="circle")
     f2.pack(side="top", anchor="nw", fill="x")

     # tv show drop down menu
     tvsh = StringVar()
     tvsh.set(" TV Show ")
     popupMenu = OptionMenu(f2, tvsh, "Latest", "Popular", "Most Trending")
     popupMenu.pack(side="left", fill=Y, ipadx="16")

     # genre drop down menu
     genre = StringVar()
     genre.set(" GENRE ")
     popupMenu = OptionMenu(f2, genre, "Comedy", "Horror", "Rom-Com", "Documentary", "Thriller", "Kids movies")
     popupMenu.pack(side="left", fill=Y, ipadx="16")

     # watchlist drop down menu
     wl = StringVar()
     wl.set(" Watchlist ")
     popupMenu = OptionMenu(f2, wl, "Recently Added", "View List")
     popupMenu.pack(side="left", fill=Y, ipadx="16")

     frame3 = Frame(root)
     frame3.pack(side="top")
     img11 = PhotoImage(file="4.png")
     l222 = Label(frame3, image=img11, )
     l222.pack(side="left")

     # horizontal movie suggestions(at the moment given by us )
     im1 = PhotoImage(file="6.png")
     im2 = ImageTk.PhotoImage(file ="sairat.jpg")
     im3 = ImageTk.PhotoImage(file ="matrix.jpg")
     im4 = ImageTk.PhotoImage(file ="shawshank.jpg")
     im5 = ImageTk.PhotoImage(file ="gump.jpg")

     bu1 = Button(root,image=im1, command=tr1)
     bu1.place(x=30, y=130)

     bu2 = Button(root,image=im2,command = tr2)
     bu2.place(x=220, y=130)

     bu3 = Button(root,image=im3,command = tr3)
     bu3.place(x=410, y=130)

     bu4 = Button(root,image=im4,command = tr4)
     bu4.place(x=600, y=130)

     bu5 = Button(root,image=im5,command = tr5)
     bu5.place(x=790, y=130)

     l1 = Label(root, text="..Didn't find anything you like? ", font="Merriweather 20 italic", bg="#eeffdc")
     l1.place(x="100", y="450")

     name = StringVar()
     mvname = Entry(root, textvariable=name, width="50", borderwidth="2",font="Roboto 14 italic", foreground="black")
     mvname.place(x=100, y=500)

     bu6 = Button(root, text="Search for movie",command = get_movie)
     bu6.place(x=670, y=500)

     ch1 = Checkbutton(root, text="Netflix")
     ch1.place(x=200, y=540)

     ch2 = Checkbutton(root, text="Prime")
     ch2.place(x=270, y=540)

     ch3 = Checkbutton(root, text="Hotstar")
     ch3.place(x=340, y=540)

     ch4 = Checkbutton(root, text="Youtube")
     ch4.place(x=415, y=540)

     ch5 = Checkbutton(root, text="Other")
     ch5.place(x=490, y=540)
     
     bu6.config(command = get_movie('The Matrix'))
     root.mainloop()