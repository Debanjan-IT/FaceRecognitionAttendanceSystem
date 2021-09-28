from tkinter import *
from tkinter import messagebox

def addMember():
    import AddMember as ad
    name = e1.get()
    if (ad.start(name)):
        messagebox.showinfo("Notification", "Member Face Added.")

def addAttendance():
    import Attendace as at
    name = e1.get()
    if (at.start(name)):
        messagebox.showinfo("Notification", "Attendance Added.")
    else:
        messagebox.showerror("Error", "User not matched. Try Again...")

master = Tk()
master.geometry("400x250")
master.title("Face-Detection Attendance System")
master.config(bg="red")
Label(master, text='Full Name', font=("Arial", 25), bg="red").pack()
e1 = Entry(master, font=("Arial", 20), bg="powderblue", width=300)
e1.pack()
Label(master, text='', bg="red").pack()
button1 = Button(master, text='Attendance', font=("Arial", 15), bg="green", width=20, command=addAttendance)
button1.pack()
Label(master, text='', bg="red").pack()
button2 = Button(master, text='Add Member', font=("Arial", 15), bg="blue", width=20, command=addMember)
button2.pack()
mainloop()