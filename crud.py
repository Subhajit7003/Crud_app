from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import askyesno
import sqlite3

conn = sqlite3.connect("Studentdata.db")
c = conn.cursor()

student = """CREATE TABLE IF NOT EXISTS "students"(
                    "roll" INT(100) NOT NULL,    
                    "name" VARCHAR(255) NOT NULL,
                    "age" INT(200) NOT NULL,
                    "course" VARCHAR(255) NOT NULL,
                    "marks" INT(200) NOT NULL,
                    PRIMARY KEY("roll")
               ); """

c.execute(student)


win = Tk()
win.title("python gui db")
win.minsize(700, 500)
win.maxsize(1366, 768)


def show_data():
    nf = Tk()
    nf.minsize(700, 500)
    nf.maxsize(1000, 800)

    nf.title("Student Records")

    L1 = Label(nf, text="Student Details", font=('Trebuchet ms', 25),
               bg='black', fg='white', padx=400, pady=20)
    L1.grid(row=0, column=0, columnspan=10)

    col_list = ["Roll No", "Name", "Age", "Course", "Marks"]

    a = 0
    for i in col_list:
        p1 = Label(nf, text=i, font=('Trebuchet ms', 20))
        p1.grid(row=1, column=a, padx=10, pady=10)
        a += 1  # a = a+1
    sTab = c.execute("SELECT * FROM students")

    r_indx = 2
    for data in sTab:
        c_indx = 0
        for i in data:
            p6 = Label(nf, text=i, font=('Trebuchet ms', 20))
            p6.grid(row=r_indx, column=c_indx, padx=10, pady=10)

            c_indx += 1
        r_indx += 1


def add_data():
    roll = e1.get()
    name = e2.get()
    age = e3.get()
    course = e4.get()
    marks = e5.get()

    if (len(str(roll)) > 0) and (len(str(name)) > 0) and (len(str(age)) > 0) and (len(str(course)) > 0) and (len(str(marks)) > 0):

        st_tab = c.execute("select * from students")
        for i in st_tab:  # tables row(tuple) = 1
            if (str(i[0]) == roll):
                messagebox.showerror("error", "roll no "+roll+" already exists.\nplease try another roll no.")
                return 

        c.execute("INSERT INTO STUDENTS (roll, name, age, course, marks) VALUES(?, ?, ?, ?, ?)",
                  (roll, name, age, course, marks))
        conn.commit()
        messagebox.showinfo("information", "record inserted successfully")
    else:
        messagebox.showerror("error", "please fill all the data")


def clear_data():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)


def update():
    en_roll = e1.get()
    en_name = e2.get()
    en_age = e3.get()
    en_course = e4.get()
    en_marks = e5.get()

    if (len(str(en_roll)) > 0) and (len(str(en_name)) > 0) and (len(str(en_age)) > 0) and (len(str(en_course)) > 0) and (len(str(en_marks)) > 0):
        c.execute("UPDATE Students set roll=?,name=?,age=?,course=?,marks=? where roll = ?",
                  (en_roll, en_name, en_age, en_course, en_marks, variable.get()))
        messagebox.showinfo("information", "record updated sccessfully")
        conn.commit()
    else:
        messagebox.showerror("error", "please fill all the data")
        return


def find():
    nf = Tk()
    nf.minsize(700, 500)
    nf.maxsize(1000, 800)
    nf.title("Find")

    L1 = Label(nf, text="Find_db : roll = "+str(variable.get()),
               font=('Trebuchet ms', 25), bg='black', fg='white', padx=400, pady=20)
    L1.grid(row=0, column=0, columnspan=50)

    col_list = ["Roll No", "Name", "Age", "Course", "Marks"]

    a = 0
    for i in col_list:
        p1 = Label(nf, text=i, font=('Trebuchet ms', 20))
        p1.grid(row=1, column=a, padx=10, pady=10)
        a += 1  # a = a+1

    x = conn.execute(
        "SELECT * FROM students WHERE roll = (?)", (variable.get(),))
    c_ind = 0
    for i in x:
        for j in i:
            p6 = Label(nf, text=j, font=('Trebuchet ms', 20))
            p6.grid(row=2, column=c_ind, padx=10, pady=10)
            c_ind += 1
        c_ind = 0


def remove():
    answer = askyesno("confirmation", "are you sure?")
    if answer:
        c.execute("DELETE FROM students WHERE roll=?", (variable.get(),))
        messagebox.showinfo("Information", "row no:" +
                            str(variable.get())+" deleted....")
        conn.commit()


def exit():
    win.destroy()


l = Label(win, text="Crud_app",
          font=('trebuchet ms', 25), fg="blue")
l.pack()

l1 = Label(win, text="Roll No.", font=('trebuchet ms', 12, 'bold'), fg="black")
l1.place(x=25, y=80)

e1 = Entry(win, font=('trebuchet ms', 12), highlightthickness=4)
e1.config(highlightbackground='black', highlightcolor="black")
e1.place(x=100, y=80, width=100, height="30")

l2 = Label(win, text="Name :", font=('trebuchet ms', 12, 'bold'), fg="black")
l2.place(x=25, y=125)

e2 = Entry(win, font=('trebuchet ms', 12), highlightthickness=4)

e2.config(highlightbackground='black', highlightcolor="black")
e2.place(x=100, y=125, width=200, height="30")

l3 = Label(win, text="Age", font=('trebuchet ms', 12, 'bold'), fg="black")
l3.place(x=25, y=165)

e3 = Entry(win, font=('trebuchet ms', 12), highlightthickness=4)
e3.config(highlightbackground='black', highlightcolor="black")
e3.place(x=100, y=165, width=80, height="30")

l4 = Label(win, text="Course", font=('trebuchet ms', 12, 'bold'), fg="black")
l4.place(x=25, y=210)

e4 = Entry(win, font=('trebuchet ms', 12), highlightthickness=4)
e4.config(highlightbackground='black', highlightcolor="black")
e4.place(x=100, y=210, width=100, height="30")

l5 = Label(win, text="Marks", font=('trebuchet ms', 12, 'bold'), fg="black")
l5.place(x=25, y=255)

e5 = Entry(win, font=('trebuchet ms', 12), highlightthickness=4)
e5.config(highlightbackground='black', highlightcolor="black")
e5.place(x=100, y=255, width=100, height="30")

l6 = Label(win, text="Select Roll No. to\n Update/Find/Delete",
           font=('trebuchet ms', 12, 'bold'), fg="black")
l6.place(x=25, y=310)


x = c.execute("SELECT * FROM students")

if len(x.fetchall()) > 0:
    variable = StringVar()
    options = []

    a = c.execute("SELECT * FROM students")

    for row in a:
        options.append(row[0])  # i[0] rows 0th column

    # print(options)
    variable.set(options[0])

    drop = OptionMenu(win, variable, *options)
    drop.place(x=25, y=370)

b1 = Button(win, text="Show Db", font=('trebuchet ms',
            12, 'bold'), command=lambda: show_data())
b1.place(x=550, y=60)

b2 = Button(win, text="Add Data", font=(
    'trebuchet ms', 12, 'bold'), command=lambda: add_data())
b2.place(x=550, y=120)

b3 = Button(win, text="Clear", font=('trebuchet ms',
            12, 'bold'), command=lambda: clear_data())
b3.place(x=550, y=180)

b4 = Button(win, text="Update", font=(
    'trebuchet ms', 12, 'bold'), command=lambda: update())
b4.place(x=200, y=365)

b5 = Button(win, text="Find", font=(
    'trebuchet ms', 12, 'bold'), command=lambda: find())
b5.place(x=280, y=365)

b6 = Button(win, text="Remove", font=(
    'trebuchet ms', 12, 'bold'), command=lambda: remove())
b6.place(x=360, y=365)

b7 = Button(win, text="Exit", font=(
    'trebuchet ms', 12, 'bold'), command=lambda: exit())
b7.place(x=270, y=420)

win.mainloop()
