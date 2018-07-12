import backend
from tkinter import *
from tkinter import messagebox
import time
###############################################################################################################################################
from tkinter import *
import sqlite3






#######################################################################################################################################
class Frontendapp(Tk):
    def __init__(self,*args,**kwargs):
         Tk.__init__(self,*args,**kwargs)
         container=Frame(self)

         container.pack(side="top",fill="both",expand=True)
         container.grid_rowconfigure(0,weight=1)
         container.columnconfigure(0,weight=1)

         self.frames={}

         for F in(PageOne,PageTwo,PageThird):

             frame=F(container,self)
             self.frames[F]=frame
             self.title("Book Directory")

             self.geometry("1350x650+0+0")

             frame.grid(row=0,column=0)

         self.show_frame(PageOne)
    def show_frame(self, cont):

        frame=self.frames[cont]
        frame.tkraise()



class PageOne(Frame):

    def __init__(self,parent,controller):

        Frame.__init__(self,parent)

        f1 = Frame(self, width=1400, height=50, bg="powderblue", relief=SUNKEN)
        f1.pack(side=TOP)

        f2 = Frame(self, width=1400, height=700, bg="powderblue", relief=SUNKEN)
        f2.pack(side=TOP)

        f3 = Frame(self)
        f3.place(x=650, y=100)

        Heading = Label(f1, text="Book Directory or Library", font=('arial', 40, 'bold'))
        Heading.grid(row=0, column=0)

        # define labels
        l1 = Label(f2, text="Title", font=('arial', 15, 'bold'), bg='powderblue')
        l1.place(x=10, y=30)

        l2 = Label(f2, text="Author", font=('arial', 15, 'bold'), bg='powderblue')
        l2.place(x=10, y=80)

        l3 = Label(f2, text="Year", font=('arial', 15, 'bold'), bg='powderblue')
        l3.place(x=10, y=130)

        l4 = Label(f2, text="ISBN", font=('arial', 15, 'bold'), bg='powderblue')
        l4.place(x=10, y=180)

        l5 = Label(f2, text="Language", font=('arial', 15, 'bold'), bg='powderblue')
        l5.place(x=10, y=230)

        l6 = Label(f2, text="Placed", font=('arial', 15, 'bold'), bg='powderblue')
        l6.place(x=10, y=280)
        # Entry section
        self.title = StringVar()
        self.e1 = Entry(f2, font=('arial', 15), textvariable=self.title, insertwidth=5, justify=LEFT, bd=5, width=40)
        self.e1.place(x=120, y=30)

        self.author = StringVar()
        self.e2 = Entry(f2, font=('arial', 15), textvariable=self.author, insertwidth=5, justify=LEFT, bd=5, width=40)
        self.e2.place(x=120, y=80)

        self.year = StringVar()
        self.e3 = Entry(f2, font=('arial', 15), textvariable=self.year, insertwidth=5, justify=LEFT, bd=5, width=40)
        self.e3.place(x=120, y=130)

        self.isbn = StringVar()
        self.e4 = Entry(f2, font=('arial', 15), textvariable=self.isbn, insertwidth=5, justify=LEFT, bd=5, width=40)
        self.e4.place(x=120, y=180)

        self.lang = StringVar()
        self.e5 = Entry(f2, font=('arial', 15), textvariable=self.lang, insertwidth=5, justify=LEFT, bd=5, width=40)
        self.e5.place(x=120, y=230)

        self.placed = StringVar()
        self.e6 = Entry(f2, font=('arial', 15), textvariable=self.placed, insertwidth=5, justify=LEFT, bd=5, width=40)
        self.e6.place(x=120, y=280)

        # define button

        self.b1 = Button(f2, text="View All", font=('arial', 10, 'bold'), bd=5, width=15, height=2, bg='#3D6DEE',command=self.view_command)
        self.b1.place(x=120, y=380)

        self.b2 = Button(f2, text="Search Book", font=('arial', 10, 'bold'), bd=5, width=15, height=2, bg='#3D6DEE',command=lambda:controller.show_frame(PageTwo))
        self.b2.place(x=1200, y=150)

        self.b3 = Button(f2, text="Add Book", font=('arial', 10, 'bold'), width=15, bd=5, height=2, bg='#3D6DEE',command=self.add_command)
        self.b3.place(x=430, y=380)

        self.b3 = Button(f2, text="Update", font=('arial', 10, 'bold'), width=15, bd=5, height=2, bg='#3D6DEE',command=self.update_command)
        self.b3.place(x=430, y=490)

        self.s = Scrollbar(f3)
        self.s.pack(side=RIGHT, fill=Y)
        self.l = Listbox(f3, width=80, height=32, yscrollcommand=self.s.set)
        self.l.pack(side=LEFT, fill=BOTH)
        self.l.bind('<<ListboxSelect>>',self.get_selected_rows)
        self.b4 = Button(f2, text="Delete Book", font=('arial', 10, 'bold'), width=15, bd=5, height=2, bg='#3D6DEE',command=self.delete_command)
        self.b4.place(x=1200, y=30)

        self.b5 = Button(f2, text="Exit", font=('arial', 10, 'bold'), width=15, bd=5, height=2, bg='red', command=exit)
        self.b5.place(x=1200, y=500)


        self.b6 = Button(f2, text="Reset", font=('arial', 10, 'bold'), width=15, bd=5, height=2, bg='#3D6DEE', command=self.reset_command)
        self.b6.place(x=120, y=490)

    def reset_command(self):
        self.title.set("")
        self.author.set("")
        self.year.set("")
        self.isbn.set("")
        self.lang.set("")
        self.placed.set("")

    def add_command(self):
        """Insert entry via button."""
        backend.add(self.title.get(), self.author.get(), self.year.get(), self.isbn.get(), self.lang.get(), self.placed.get())
        self.l.delete(0, END)
        self.l.insert(END, (self.title.get(), self.author.get(), self.year.get(), self.isbn.get(), self.lang.get(), self.placed.get()))

    def view_command(self):
        """View entries via button."""
        self.l.delete(0, END)
        for row in backend.view_all():
            self.l.insert(END, row)

    def update_command(self):
        """Update entry via button."""
        backend.update(self.selected_tuple[0], self.title.get(), self.author.get(), self.year.get(), self.isbn.get(), self.lang.get(), self.placed.get())

    def delete_command(self):
        """Delete entry via button."""
        self.result = messagebox.askquestion("Delete", "Are You Sure?", icon='warning')
        if self.result == 'yes':
            backend.delete(self.selected_tuple[0])

    def search_command(self):
        """Search entry via button."""
        self.l.delete(0, END)
        for row in backend.search(self.title.get(), self.lang.get()):
            self.l.insert(END, row)

    def get_selected_rows(self,event):
        """Pre-fill fields for selected entry."""
        global selected_tuple
        self.index = self.l.curselection()[0]
        self.selected_tuple = self.l.get(self.index)

        self.e1.delete(0, END)
        self.e1.insert(END, self.selected_tuple[1])

        self.e2.delete(0, END)
        self.e2.insert(END, self.selected_tuple[2])

        self.e3.delete(0, END)
        self.e3.insert(END, self.selected_tuple[3])

        self.e4.delete(0, END)
        self.e4.insert(END, self.selected_tuple[4])

        self.e5.delete(0, END)
        self.e5.insert(END, self.selected_tuple[5])

        self.e6.delete(0, END)
        self.e6.insert(END, self.selected_tuple[6])
class PageTwo(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        f1 = Frame(self, width=1400, height=70, relief=SUNKEN)
        f1.pack(side=TOP)

        f2 = Frame(self, width=1400, height=650, bg="powderblue", relief=SUNKEN)
        f2.pack(side=LEFT)

        f3 = Frame(self)
        f3.place(x=200, y=200)

        Heading = Label(f1, text="Book Search", font=('arial', 40, 'bold'))
        Heading.place(x=500, y=0)

        # define labels
        l1 = Label(f2, text="Book Name", font=('arial', 15, 'bold'), bg='powderblue')
        l1.place(x=10, y=20)

        l5 = Label(f2, text="Language", font=('arial', 15, 'bold'), bg='powderblue')
        l5.place(x=10, y=70)

        # Entry section
        self.book = StringVar()
        self.e1 = Entry(f2, font=('arial', 15), textvariable=self.book, insertwidth=5, justify=LEFT, bd=5, width=48)
        self.e1.place(x=200, y=20)

        self.lang = StringVar()
        self.e2 = Entry(f2, font=('arial', 15), textvariable=self.lang, insertwidth=5, justify=LEFT, bd=5, width=48)
        self.e2.place(x=200, y=70)

        # define button

        self.b1 = Button(f2, text="Search", font=('arial', 10, 'bold'), bd=5, width=15, height=2, bg='#3D6DEE',command=self.search_command)
        self.b1.place(x=800, y=20)

        self.b2 = Button(f2, text="Issue Book", font=('arial', 10, 'bold'), bd=5, width=15, height=2, bg='#3D6DEE',command=lambda:controller.show_frame(PageThird))
        self.b2.place(x=1100, y=20)

        self.s = Scrollbar(f3)
        self.s.pack(side=RIGHT, fill=Y)
        self.l = Listbox(f3, width=86, height=27, yscrollcommand=self.s.set)
        self.l.pack(side=LEFT, fill=BOTH)
        self.l.bind('<<ListboxSelect>>',self.get_selected_rows)

        self.b3 = Button(f2, text="Back", font=('arial', 10, 'bold'), width=15, bd=5, height=2, bg='#3D6DEE',command=lambda:controller.show_frame(PageOne))
        self.b3.place(x=1100, y=405)

        self.b4 = Button(f2, text="Exit", font=('arial', 10, 'bold'), width=15, bd=5, height=2, bg='red',command=exit)
        self.b4.place(x=1100, y=505)


        self.b5 = Button(f2, text="Delete", font=('arial', 10, 'bold'), width=15, bd=5, height=2, bg='#3D6DEE',command=self.delete_command)
        self.b5.place(x=800, y=150)

        self.b6 = Button(f2, text="Reset", font=('arial', 10, 'bold'), width=15, bd=5, height=2, bg='#3D6DEE',command=self.reset_command)
        self.b6.place(x=800, y=300)

    def delete_command(self):
        """Delete entry via button."""
        self.result = messagebox.askquestion("Delete", "Are You Sure?", icon='warning')
        if self.result == 'yes':

             backend.delete(self.selected_tuple[0])

    def search_command(self):
        """Search entry via button."""
        self.l.delete(0, END)
        for row in backend.search(self.book.get(), self.lang.get()):
            self.l.insert(END, row)

    def reset_command(self):
        self.book.set("")
        self.lang.set("")

    def get_selected_rows(self,event):
        """Pre-fill fields for selected entry."""
        global selected_tuple
        self.index = self.l.curselection()[0]
        self.selected_tuple = self.l.get(self.index)

        self.e1.delete(0, END)
        self.e1.insert(END, self.selected_tuple[1])

        self.e2.delete(0, END)
        self.e2.insert(END, self.selected_tuple[2])



class PageThird(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)



        f1 = Frame(self, width=1400, height=50, relief=SUNKEN)
        f1.pack(side=TOP)

        f2 = Frame(self, width=1400, height=650, bg="powderblue", relief=SUNKEN)
        f2.pack(side=LEFT)

        f3 = Frame(self)
        f3.place(x=750, y=200)

        Heading = Label(f1, text="Issue Book", font=('arial', 40, 'bold'))
        Heading.grid(row=0, column=0)

        # define labels
        l1 = Label(f2, text="Name of Student", font=('arial', 15, 'bold'), bg="powderblue")
        l1.place(x=20, y=30)

        l2 = Label(f2, text="Department", font=('arial', 15, 'bold'), bg="powderblue")
        l2.place(x=20, y=80)

        l3 = Label(f2, text="Roll-No", font=('arial', 15, 'bold'), bg="powderblue")
        l3.place(x=20, y=130)

        l4 = Label(f2, text="Mobile-No", font=('arial', 15, 'bold'), bg="powderblue")
        l4.place(x=20, y=180)

        l5 = Label(f2, text="Name of Books", font=('arial', 15, 'bold'), bg="powderblue")
        l5.place(x=20, y=230)

        l7 = Label(f2, text="ISBN", font=('arial', 15, 'bold'), bg="powderblue")
        l7.place(x=20, y=280)

        l6 = Label(f2, text="Issued-Date", font=('arial', 15, 'bold'), bg="powderblue")
        l6.place(x=20, y=330)

        l7 = Label(f2, text="Emai-ID", font=('arial', 15, 'bold'), bg="powderblue")
        l7.place(x=20, y=380)
        # Entry section
        self.name = StringVar()
        self.e1 = Entry(f2, font=('arial', 15), textvariable=self.name, insertwidth=5, justify=LEFT, bd=5, width=40)
        self.e1.place(x=250, y=30)

        self.department = StringVar()
        self.e2 = Entry(f2, font=('arial', 15), textvariable=self.department, insertwidth=5, justify=LEFT, bd=5, width=40)
        self.e2.place(x=250, y=80)

        self.roll_no = StringVar()
        self.e3 = Entry(f2, font=('arial', 15), textvariable=self.roll_no, insertwidth=5, justify=LEFT, bd=5, width=40)
        self.e3.place(x=250, y=130)

        self.mobile = StringVar()
        self.e4 = Entry(f2, font=('arial', 15), textvariable=self.mobile, insertwidth=5, justify=LEFT, bd=5, width=40)
        self.e4.place(x=250, y=180)

        self.books = StringVar()
        self.e5 = Entry(f2, font=('arial', 15), textvariable=self.books, insertwidth=5, justify=LEFT, bd=5, width=40)
        self.e5.place(x=250, y=230)

        self.isbn = StringVar()
        self.e6 = Entry(f2, font=('arial', 15), textvariable=self.isbn, insertwidth=5, justify=LEFT, bd=5, width=40)
        self.e6.place(x=250, y=280)

        self.date = StringVar()
        self.e7 = Entry(f2, font=('arial', 15), textvariable=self.date, insertwidth=5, justify=LEFT, bd=5, width=40)
        self.e7.place(x=250, y=330)

        self.email = StringVar()
        self.e8 = Entry(f2, font=('arial', 15), textvariable=self.email, insertwidth=5, justify=LEFT, bd=5, width=40)
        self.e8.place(x=250, y=380)
        # define button

        self.b1 = Button(f2, text="Issued", font=('arial', 10, 'bold'), bd=5, width=15, height=2, bg='#3D6DEE',command=self.add_command)
        self.b1.place(x=750, y=30)

        self.s = Scrollbar(f3)
        self.s.pack(side=RIGHT, fill=Y)
        self.l = Listbox(f3, width=85, height=26, yscrollcommand=self.s.set)
        self.l.pack(side=LEFT, fill=BOTH)
        self.l.bind('<<ListboxSelect>>', self.get_selected_rows)

        self.b2 = Button(f2, text="Back", font=('arial', 10, 'bold'), width=15, bd=5, height=2, bg='#3D6DEE',command=lambda:controller.show_frame(PageTwo) )
        self.b2.place(x=100, y=500)

        self.b3 = Button(f2, text="Exit", font=('arial', 10, 'bold'), width=15, bd=5, height=2, bg='red',command=exit)
        self.b3.place(x=500, y=500)


        self.b4 = Button(f2, text="Delete", font=('arial', 10, 'bold'), width=15, bd=5, height=2, bg='#3D6DEE',command=self.delete_command)
        self.b4.place(x=1150, y=30)


        self.b5 = Button(f2, text="View All", font=('arial', 10, 'bold'), width=15, bd=5, height=2, bg='#3D6DEE',command=self.view_command)
        self.b5.place(x=950, y=30)


        self.b6 = Button(f2, text="Reset", font=('arial', 10, 'bold'), width=15, bd=5, height=2, bg='#3D6DEE',command=self.reset_command)
        self.b6.place(x=300, y=500)

    def reset_command(self):
        self.name.set("")
        self.department.set("")
        self.roll_no.set("")
        self.mobile.set("")
        self.books.set("")
        self.isbn.set("")
        self.date.set("")
        self.email.set("")

    def add_command(self):
        """Insert entry via button."""
        backend.stu(self.name.get(),self.department.get(), self.roll_no.get(), self.mobile.get(), self.books.get(),self.isbn.get(), self.date.get(), self.email.get())
        self.l.delete(0, END)
        self.l.insert(END, (self.name.get(),self.department.get(), self.roll_no.get(), self.mobile.get(), self.books.get(),self.isbn.get(), self.date.get(), self.email.get()))
        backend.dele(self.isbn.get())

    def delete_command(self):
        """Delete entry via button."""
        self.result = messagebox.askquestion("Delete", "Are You Sure?", icon='warning')
        if self.result == 'yes':
            backend.de(self.selected_tuple[0])



    def view_command(self):
        """View entries via button."""
        self.l.delete(0, END)
        for row in backend.view():
            self.l.insert(END, row)

    def get_selected_rows(self,event):
        """Pre-fill fields for selected entry."""
        global selected_tuple
        self.index = self.l.curselection()[0]
        self.selected_tuple = self.l.get(self.index)

        self.e1.delete(0, END)
        self.e1.insert(END, self.selected_tuple[1])

        self.e2.delete(0, END)
        self.e2.insert(END, self.selected_tuple[2])

        self.e3.delete(0, END)
        self.e3.insert(END, self.selected_tuple[3])

        self.e4.delete(0, END)
        self.e4.insert(END, self.selected_tuple[4])

        self.e5.delete(0, END)
        self.e5.insert(END, self.selected_tuple[5])

        self.e6.delete(0, END)
        self.e6.insert(END, self.selected_tuple[6])

        self.e7.delete(0, END)
        self.e7.insert(END, self.selected_tuple[7])

        self.e8.delete(0, END)
        self.e8.insert(END, self.selected_tuple[8])

#####################################################################################################################

# ==============================METHODS========================================
def Database():
    global conn, cursor
    conn = sqlite3.connect("my.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER  PRIMARY KEY , username TEXT, password TEXT)")
    cursor.execute("SELECT * FROM `member` WHERE `username` = 'Bhuvnesh ' AND `password` = '2527'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `member` (username, password) VALUES('Bhuvnesh', '2527')")
        conn.commit()


def Login(event=None):
    Database()
    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_text.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ? AND `password` = ?",
                       (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            root.withdraw()
            app = Frontendapp()
            app.mainloop()
            USERNAME.set("")
            PASSWORD.set("")
            lbl_text.config(text="")
        else:
            lbl_text.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
    cursor.close()
    conn.close()


root = Tk()
root.title("Book Directory App")
width = 400
height = 280
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

# ==============================VARIABLES======================================
USERNAME = StringVar()
PASSWORD = StringVar()

# ==============================FRAMES=========================================
Top = Frame(root, bd=2, relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=200)
Form.pack(side=TOP, pady=20)

# ==============================LABELS=========================================
lbl_title = Label(Top, text="Book Directory Application", font=('arial', 15),bg="powderblue")
lbl_title.pack(fill=X)
lbl_username = Label(Form, text="Username:", font=('arial', 14), bd=15)
lbl_username.grid(row=0, sticky="e")
lbl_password = Label(Form, text="Password:", font=('arial', 14), bd=15)
lbl_password.grid(row=1, sticky="e")
lbl_text = Label(Form)
lbl_text.grid(row=2, columnspan=2)

# ==============================ENTRY WIDGETS==================================
username = Entry(Form, textvariable=USERNAME, font=(14))
username.grid(row=0, column=1)
password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
password.grid(row=1, column=1)

# ==============================BUTTON WIDGETS=================================
btn_login = Button(Form, text="Login", width=45, command=Login,bg="powderblue")
btn_login.grid(pady=25, row=3, columnspan=2)
btn_login.bind('<Return>', Login)


root.mainloop()

