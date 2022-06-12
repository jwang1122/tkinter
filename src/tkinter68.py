from tkinter import *
import time
Student_forum=Tk()
Student_forum.title("student form")
Student_forum.geometry('390x400')

Roll_ask = Label(Student_forum,text="Roll Number")
Roll_ask.pack()
Roll = Entry()
Roll.pack()

name_ask = Label(Student_forum,text = "Name")
name_ask.pack()
Name = Entry(Student_forum)
Name.pack()

age_ask = Label(Student_forum,text = "Age")
age_ask.pack()
age = Entry()
age.pack()
def submit():
    if Roll.get() == "":
        error = Label(Student_forum,text = "Please fill Roll section roll section can't remain blank")
        error.pack()
    elif Name.get() == "":
        error2 = Label(Student_forum ,text="Please fill your name in name section it  can't e remain blank")

        error2.pack()
    elif age.get() == "":
        error3 = Label(Student_forum,text="fill age section first")
        error3.pack()
    else:
        get_data = open("student_details.txt","r")
        get_data2 = get_data.read()
        if Roll.get() in get_data2:
            Label2 = Label(Student_forum,text="You are already added in the list")
            Label2.pack()
        else:
            steps = "Your name is " + Name.get() + " and your age is " + age.get()

            submit_out = Label(Student_forum,text = steps)
            submit_out.pack()
            txt_file = open("student_details.txt","a+")
            txt_file.writelines(str(("Roll number="+Roll.get()+" Name= "+Name.get()+" Age="+age.get()+"\n")))
            txt_file.close()
            do = Label(Student_forum,text="Now you are added in the list of students")
            do.pack()
            
def clear():
    Roll.delete(0,"end")
    Name.delete(0,"end")
    age.delete(0,"end")
Button1 = Button(Student_forum,text="Submit Form",command=submit)
Button1.pack()
Button2 = Button(Student_forum,text="Clear",command=clear)
Button2.pack()
    
Student_forum.mainloop()