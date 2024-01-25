import sqlite3
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
from tkinter import *
import time
import threading
from tkinter import simpledialog

# （2）database info.db
conn = sqlite3.connect("Info.db")
# （3）cursor for connection
cur = conn.cursor()

pageGeo = "1400x600"


def LoginPage():  # enter main
    def goto(num):
        root.destroy()  # destroy main win
        if num == 1:
            Student_Page()  # enter win 1
        elif num == 2:
            Teacher_Page()  # enter win 2
        elif num == 3:
            Administrator_Page()  # enter win 2

    root = Tk()
    root.title('Management System')
    root.geometry("400x250")
    but_main1 = Button(root, text="Student", command=lambda: goto(1))
    # enter win 1
    but_main1.pack(pady=5)
    but_main2 = Button(root, text="Teacher", command=lambda: goto(2))
    # enter win 2
    but_main2.pack(pady=5)
    but_main3 = Button(root, text="Administrator", command=lambda: goto(3))
    # enter win 2
    but_main3.pack(pady=5)

    root.mainloop()


def Student_Page():
    def gotoLogin():
        root1.destroy()  # close win 1
        LoginPage()  # enter main

    def display1():
        table1.pack()
        table2.pack_forget()
        table3.pack_forget()
        table4.pack_forget()

    def display2():
        table2.pack()
        table1.pack_forget()
        table3.pack_forget()
        table4.pack_forget()

    def display3():
        table3.pack()
        table1.pack_forget()
        table2.pack_forget()
        table4.pack_forget()

    def display4():
        table4.pack()
        table1.pack_forget()
        table2.pack_forget()
        table3.pack_forget()

    root1 = Tk()
    root1.geometry(pageGeo)
    root1.title('Management System')
    Label(root1, text='Student.', bg='light green').pack(fill=X)

    table1 = Frame(root1)
    STU = display_data(table1, "Students_information")
    STU.pack(side=RIGHT, fill=Y)
    sb = Scrollbar(table1, orient=VERTICAL)
    sb.pack(side=RIGHT, fill=Y)
    STU.config(yscrollcommand=sb.set)
    sb.config(command=STU.yview)

    table2 = Frame(root1)
    COU = display_data(table2, "Course_information")
    COU.pack(side=RIGHT, fill=Y)
    sb2 = Scrollbar(table1, orient=VERTICAL)
    sb2.pack(side=RIGHT, fill=Y)
    COU.config(yscrollcommand=sb2.set)
    sb2.config(command=COU.yview)

    table3 = Frame(root1)
    TEA = display_data(table3, "Teacher_information")
    TEA.pack(side=RIGHT, fill=Y)
    sb3 = Scrollbar(table1, orient=VERTICAL)
    sb3.pack(side=RIGHT, fill=Y)
    TEA.config(yscrollcommand=sb2.set)
    sb3.config(command=TEA.yview)

    table4 = Frame(root1)
    CHO = display_data(table4, "Choosing_information")
    CHO.pack(side=RIGHT, fill=Y)
    sb4 = Scrollbar(table1, orient=VERTICAL)
    sb4.pack(side=RIGHT, fill=Y)
    CHO.config(yscrollcommand=sb2.set)
    sb4.config(command=CHO.yview)

    btn_Frame = Frame(root1)
    btn_Frame.pack(side=BOTTOM)

    btnSTU = Button(btn_Frame, text="Students_information", command=display1)
    btnSTU.pack(side=LEFT, pady=10)

    btnCou = Button(btn_Frame, text="Course_information", command=display2)
    btnCou.pack(side=LEFT, pady=10)

    btnTea = Button(btn_Frame, text="Teacher_information", command=display3)
    btnTea.pack(side=LEFT, pady=10)

    btnCho = Button(btn_Frame, text="Choosing_information", command=display4)
    btnCho.pack(side=LEFT, pady=10)

    butone1 = Button(btn_Frame, text="Back to Login", command=gotoLogin)
    butone1.pack(side=LEFT, pady=10)

    display1()
    root1.mainloop()


def Teacher_Page():
    def refresh():
        root2.destroy()  # close win 2
        Administrator_Page()  # enter main

    def gotoLogin():
        root2.destroy()  # close win 2
        LoginPage()  # enter main

    def display1():
        table1.pack()
        table2.pack_forget()
        table3.pack_forget()
        table4.pack_forget()

    def display2():
        table2.pack()
        table1.pack_forget()
        table3.pack_forget()
        table4.pack_forget()

    def display3():
        table3.pack()
        table1.pack_forget()
        table2.pack_forget()
        table4.pack_forget()

    def display4():
        table4.pack()
        table1.pack_forget()
        table2.pack_forget()
        table3.pack_forget()

    root2 = Tk()
    root2.geometry(pageGeo)
    root2.title('Management System')
    Label(root2, text='Teacher.', bg='lightblue').pack(fill=X)

    table1 = Frame(root2)
    STU = display_data(table1, "Students_information")
    STU.pack(side=RIGHT, fill=Y)
    sb = Scrollbar(table1, orient=VERTICAL)
    sb.pack(side=RIGHT, fill=Y)
    STU.config(yscrollcommand=sb.set)
    sb.config(command=STU.yview)

    table2 = Frame(root2)
    COU = display_data(table2, "Course_information")
    COU.pack(side=RIGHT, fill=Y)
    sb2 = Scrollbar(table1, orient=VERTICAL)
    sb2.pack(side=RIGHT, fill=Y)
    COU.config(yscrollcommand=sb2.set)
    sb2.config(command=COU.yview)

    table3 = Frame(root2)
    TEA = display_data(table3, "Teacher_information")
    TEA.pack(side=RIGHT, fill=Y)
    sb3 = Scrollbar(table1, orient=VERTICAL)
    sb3.pack(side=RIGHT, fill=Y)
    TEA.config(yscrollcommand=sb2.set)
    sb3.config(command=TEA.yview)

    table4 = Frame(root2)
    CHO = display_data(table4, "Choosing_information")
    CHO.pack(side=RIGHT, fill=Y)
    sb4 = Scrollbar(table1, orient=VERTICAL)
    sb4.pack(side=RIGHT, fill=Y)
    CHO.config(yscrollcommand=sb2.set)
    sb4.config(command=CHO.yview)

    btn_Frame = Frame(root2)
    btn_Frame.pack(side=BOTTOM)

    btnSTU = Button(btn_Frame, text="Students_information", command=display1)
    btnSTU.pack(side=LEFT, pady=10)

    btnCou = Button(btn_Frame, text="Course_information", command=display2)
    btnCou.pack(side=LEFT, pady=10)

    btnTea = Button(btn_Frame, text="Teacher_information", command=display3)
    btnTea.pack(side=LEFT, pady=10)

    btnCho = Button(btn_Frame, text="Choosing_information", command=display4)
    btnCho.pack(side=LEFT, pady=10)

    butModifyScore = Button(btn_Frame, text="Modify Score", command=lambda: Modify_Score(CHO))
    butModifyScore.pack(side=LEFT, pady=10)

    butRE = Button(btn_Frame, text="Reload", command=refresh)
    butRE.pack(side=LEFT, pady=10)

    butone1 = Button(btn_Frame, text="Back to Login", command=gotoLogin)
    butone1.pack(side=LEFT, pady=10)

    display1()
    root2.mainloop()


def Administrator_Page():
    def refresh():
        root3.destroy()  # close win 2
        Administrator_Page()  # enter main

    def gotoLogin():
        root3.destroy()  # close win 2
        LoginPage()  # enter main

    def display1():
        table1.pack()
        cho_btn_Frame.pack_forget()
        tea_btn_Frame.pack_forget()
        cou_btn_Frame.pack_forget()
        std_btn_Frame.pack(side=BOTTOM)
        table2.pack_forget()
        table3.pack_forget()
        table4.pack_forget()

    def display2():
        table2.pack()
        cho_btn_Frame.pack_forget()
        tea_btn_Frame.pack_forget()
        cou_btn_Frame.pack(side=BOTTOM)
        std_btn_Frame.pack_forget()
        table1.pack_forget()
        table3.pack_forget()
        table4.pack_forget()

    def display3():
        table3.pack()
        cho_btn_Frame.pack_forget()
        tea_btn_Frame.pack(side=BOTTOM)
        cou_btn_Frame.pack_forget()
        std_btn_Frame.pack_forget()
        table1.pack_forget()
        table2.pack_forget()
        table4.pack_forget()

    def display4():
        table4.pack()
        cho_btn_Frame.pack(side=BOTTOM)
        tea_btn_Frame.pack_forget()
        cou_btn_Frame.pack_forget()
        std_btn_Frame.pack_forget()
        table1.pack_forget()
        table2.pack_forget()
        table3.pack_forget()

    root3 = Tk()
    root3.geometry(pageGeo)
    root3.title('Management System')
    Label(root3, text='Administrator.', bg='light grey').pack(fill=X)

    # create tables and frames
    table1 = Frame(root3)
    STU = display_data(table1, "Students_information")
    STU.pack(side=RIGHT, fill=Y)
    sb = Scrollbar(table1, orient=VERTICAL)
    sb.pack(side=RIGHT, fill=Y)
    STU.config(yscrollcommand=sb.set)
    sb.config(command=STU.yview)

    table2 = Frame(root3)
    COU = display_data(table2, "Course_information")
    COU.pack(side=RIGHT, fill=Y)
    sb2 = Scrollbar(table1, orient=VERTICAL)
    sb2.pack(side=RIGHT, fill=Y)
    COU.config(yscrollcommand=sb2.set)
    sb2.config(command=COU.yview)

    table3 = Frame(root3)
    TEA = display_data(table3, "Teacher_information")
    TEA.pack(side=RIGHT, fill=Y)
    sb3 = Scrollbar(table1, orient=VERTICAL)
    sb3.pack(side=RIGHT, fill=Y)
    TEA.config(yscrollcommand=sb2.set)
    sb3.config(command=TEA.yview)

    table4 = Frame(root3)
    CHO = display_data(table4, "Choosing_information")
    CHO.pack(side=RIGHT, fill=Y)
    sb4 = Scrollbar(table1, orient=VERTICAL)
    sb4.pack(side=RIGHT, fill=Y)
    CHO.config(yscrollcommand=sb2.set)
    sb4.config(command=CHO.yview)

    std_btn_Frame = Frame(root3)
    cou_btn_Frame = Frame(root3)
    tea_btn_Frame = Frame(root3)
    cho_btn_Frame = Frame(root3)
    table_btn_Frame = Frame(root3)

    table_btn_Frame.pack(side=BOTTOM)

    btnSTU = Button(table_btn_Frame, text="Students_information", command=display1)
    btnSTU.pack(side=LEFT, pady=10)

    btnCou = Button(table_btn_Frame, text="Course_information", command=display2)
    btnCou.pack(side=LEFT, pady=10)

    btnTea = Button(table_btn_Frame, text="Teacher_information", command=display3)
    btnTea.pack(side=LEFT, pady=10)

    btnCho = Button(table_btn_Frame, text="Choosing_information", command=display4)
    btnCho.pack(side=LEFT, pady=10)

    butRE = Button(table_btn_Frame, text="Reload", command=refresh)
    butRE.pack(side=LEFT, pady=10)

    butBack = Button(table_btn_Frame, text="Back to Login", command=gotoLogin)
    butBack.pack(side=LEFT, pady=10)

    butInsertStd = Button(std_btn_Frame, text="Insert Student", command=lambda: Insert_Std(STU))
    butInsertStd.pack(side=LEFT, pady=10)

    butInsertTea = Button(tea_btn_Frame, text="Insert Teacher", command=lambda: Insert_Tea(TEA))
    butInsertTea.pack(side=LEFT, pady=10)

    butInsertCou = Button(cou_btn_Frame, text="Insert Course", command=lambda: Insert_Cou(COU))
    butInsertCou.pack(side=LEFT, pady=10)

    butInsertCho = Button(cho_btn_Frame, text="Insert Choosing", command=lambda: Insert_Cho(CHO))
    butInsertCho.pack(side=LEFT, pady=10)

    butDeleteStd = Button(std_btn_Frame, text="Delete Student", command=lambda: Delete_Stu(STU))
    butDeleteStd.pack(side=LEFT, pady=10)

    butDeleteCou = Button(cou_btn_Frame, text="Delete Course", command=lambda: Delete_Cou(COU))
    butDeleteCou.pack(side=LEFT, pady=10)

    butDeleteTea = Button(tea_btn_Frame, text="Delete Teacher", command=lambda: Delete_Tea(TEA))
    butDeleteTea.pack(side=LEFT, pady=10)

    butDeleteCho = Button(cho_btn_Frame, text="Delete Choosing", command=lambda: Delete_Cho(CHO))
    butDeleteCho.pack(side=LEFT, pady=10)

    butModifyStd = Button(std_btn_Frame, text="Modify Student", command=lambda: Modify_Std(STU))
    butModifyStd.pack(side=LEFT, pady=10)

    butModifyTea = Button(tea_btn_Frame, text="Modify Teacher", command=lambda: Modify_Tea(TEA))
    butModifyTea.pack(side=LEFT, pady=10)

    butModifyCou = Button(cou_btn_Frame, text="Modify Course", command=lambda: Modify_Cou(COU))
    butModifyCou.pack(side=LEFT, pady=10)

    butModifyCho = Button(cho_btn_Frame, text="Modify Choosing", command=lambda: Modify_Cho(CHO))
    butModifyCho.pack(side=LEFT, pady=10)

    butQueryScore = Button(cho_btn_Frame, text="Query Score", command=query_score)
    butQueryScore.pack(side=LEFT, pady=10)

    butQueryCourse = Button(cou_btn_Frame, text="Query Course", command=query_course)
    butQueryCourse.pack(side=LEFT, pady=10)

    butQueryTea = Button(tea_btn_Frame, text="Query Teacher", command=query_teacher)
    butQueryTea.pack(side=LEFT, pady=10)

    butAVGScore = Button(cho_btn_Frame, text="Average Score", command=average)
    butAVGScore.pack(side=LEFT, pady=10)

    display1()
    root3.mainloop()


def Insert_Std(tv):
    root4 = Tk()
    root4.geometry('500x300')
    root4.title('Insert Student')

    l1 = tk.Label(root4, text='Student ID')
    l1.grid(row=1, column=0, padx=5, pady=5)
    id_Entry = tk.Entry(root4, width=40)
    id_Entry.grid(row=1, column=1, padx=5, pady=5)

    l2 = tk.Label(root4, text='Student Name')
    l2.grid(row=2, column=0, padx=5, pady=5)
    NameEntry = tk.Entry(root4, width=40)
    NameEntry.grid(row=2, column=1, padx=5, pady=5)

    l3 = tk.Label(root4, text='Sex')
    l3.grid(row=3, column=0, padx=5, pady=5)

    def male():
        SexEntry.config(text='male')

    def female():
        SexEntry.config(text='female')

    SexEntry = tk.Label(root4, text='male')
    SexEntry.grid(row=3, column=1, padx=5, pady=5)

    male_button = Button(root4, text="male", command=male)
    female_button = Button(root4, text="female", command=female)
    male_button.grid(row=3, column=2, padx=5, pady=5)
    female_button.grid(row=3, column=3, padx=5, pady=5)

    l4 = tk.Label(root4, text='Entrance_Age')
    l4.grid(row=4, column=0, padx=5, pady=5)
    AgeEntry = tk.Entry(root4, width=30)
    AgeEntry.grid(row=4, column=1, padx=5, pady=5)

    l5 = tk.Label(root4, text='Entrance_Year')
    l5.grid(row=5, column=0, padx=5, pady=5)
    YearEntry = tk.Entry(root4, width=30)
    YearEntry.grid(row=5, column=1, padx=5, pady=5)

    l6 = tk.Label(root4, text='Class')
    l6.grid(row=6, column=0, padx=5, pady=5)
    ClassEntry = tk.Entry(root4, width=30)
    ClassEntry.grid(row=6, column=1, padx=5, pady=5)

    def try_insert():
        try:
            if len(str(id_Entry.get())) == 10:
                conn.execute("INSERT INTO " + "Students_information" + " ( " + "s_ID" + ", " +
                             "s_Name" + ", " + "Sex" + ", " + "Entrance_Age" + ", " + "Entrance_Year" + ", " +
                             "Class" + " ) VALUES ( '"
                             + str(id_Entry.get()) + "', '" + str(NameEntry.get()) + "', '" +
                             str(SexEntry.cget("text")) + "', '" + str(AgeEntry.get()) + "', '"
                             + str(YearEntry.get()) + "', '" + str(ClassEntry.get()) + "' ); ")
                conn.commit()
                root4.destroy()
                tk.messagebox.showinfo("Success", "Data Saved Successfully. Please reload.")
            else:
                conn.rollback()
                root4.destroy()
                tk.messagebox.showinfo("Fail", "Invalid Input(Student id 10 digits).")

        except sqlite3.OperationalError as e:
            conn.rollback()
            root4.destroy()
            tk.messagebox.showinfo("Fail", "EX: {}".format(e))

    butone1 = Button(root4, text="Yes", command=try_insert)
    butone1.grid(row=7, column=1, padx=5, pady=5)

    butone2 = Button(root4, text="Close", command=root4.destroy)
    butone2.grid(row=8, column=1, padx=5, pady=5)

    root4.mainloop()


def Insert_Cou(tv):
    root4 = Tk()
    root4.geometry('500x300')
    root4.title('Insert Course')

    l1 = tk.Label(root4, text='Course ID')
    l1.grid(row=1, column=0, padx=5, pady=5)
    id_Entry = tk.Entry(root4, width=40)
    id_Entry.grid(row=1, column=1, padx=5, pady=5)

    l2 = tk.Label(root4, text='Course Name')
    l2.grid(row=2, column=0, padx=5, pady=5)
    NameEntry = tk.Entry(root4, width=40)
    NameEntry.grid(row=2, column=1, padx=5, pady=5)

    l3 = tk.Label(root4, text='Teacher ID')
    l3.grid(row=3, column=0, padx=5, pady=5)
    tIDEntry = tk.Entry(root4, width=30)
    tIDEntry.grid(row=3, column=1, padx=5, pady=5)

    l4 = tk.Label(root4, text='Credit')
    l4.grid(row=4, column=0, padx=5, pady=5)
    CreditEntry = tk.Entry(root4, width=30)
    CreditEntry.grid(row=4, column=1, padx=5, pady=5)

    l5 = tk.Label(root4, text='Grade')
    l5.grid(row=5, column=0, padx=5, pady=5)
    GradeEntry = tk.Entry(root4, width=30)
    GradeEntry.grid(row=5, column=1, padx=5, pady=5)

    l6 = tk.Label(root4, text='Canceled_Year')
    l6.grid(row=6, column=0, padx=5, pady=5)
    YearEntry = tk.Entry(root4, width=30)
    YearEntry.grid(row=6, column=1, padx=5, pady=5)

    def try_insert():
        try:
            if len(str(id_Entry.get())) == 7:
                conn.execute("INSERT INTO " + "Course_information" + " ( " + "c_ID" + ", " +
                             "c_Name" + ", " + "t_ID" + ", " + "Credit" + ", " + "Grade" + ", " +
                             "Canceled_Year" + " ) VALUES ( '"
                             + str(id_Entry.get()) + "', '" + str(NameEntry.get()) + "', '" +
                             str(tIDEntry.get()) + "', '" + str(CreditEntry.get()) + "', '"
                             + str(GradeEntry.get()) + "', '" + str(YearEntry.get()) + "' ); ")
                conn.commit()
                root4.destroy()
                tk.messagebox.showinfo("Success", "Data Saved Successfully. Please reload.")
            else:
                conn.rollback()
                root4.destroy()
                tk.messagebox.showinfo("Fail", "Invalid Input(Course id 7 digits).")

        except sqlite3.OperationalError as e:
            conn.rollback()
            root4.destroy()
            tk.messagebox.showinfo("Fail", "Ex: {}".format(e))

    butone1 = Button(root4, text="Yes", command=try_insert)
    butone1.grid(row=7, column=1, padx=5, pady=5)

    butone2 = Button(root4, text="Close", command=root4.destroy)
    butone2.grid(row=8, column=1, padx=5, pady=5)

    root4.mainloop()


def Insert_Tea(tv):
    root4 = Tk()
    root4.geometry('500x300')
    root4.title('Insert Teacher')

    l1 = tk.Label(root4, text='Teacher ID')
    l1.grid(row=1, column=0, padx=5, pady=5)
    Id_Entry = tk.Entry(root4, width=40)
    Id_Entry.grid(row=1, column=1, padx=5, pady=5)

    l2 = tk.Label(root4, text='Teacher Name')
    l2.grid(row=2, column=0, padx=5, pady=5)
    NameEntry = tk.Entry(root4, width=40)
    NameEntry.grid(row=2, column=1, padx=5, pady=5)

    l3 = tk.Label(root4, text='Courses')
    l3.grid(row=3, column=0, padx=5, pady=5)
    SexEntry = tk.Entry(root4, width=30)
    SexEntry.grid(row=3, column=1, padx=5, pady=5)

    def try_insert():

        try:
            conn.execute("INSERT INTO " + "Teacher_information" + " ( " + "t_ID" + ", " +
                         "Name" + ", " + "c_Name" " ) VALUES ( '"
                         + str(Id_Entry.get()) + "', '" + str(NameEntry.get()) + "', '" +
                         str(SexEntry.get()) + "' ); ")
            conn.commit()
            root4.destroy()
            tk.messagebox.showinfo("Success", "Data Saved Successfully. Please reload.")
        except sqlite3.OperationalError as e:
            conn.rollback()
            tk.messagebox.showinfo("Fail", "Ex: {}".format(e))

    butone1 = Button(root4, text="Yes", command=try_insert)
    butone1.grid(row=7, column=1, padx=5, pady=5)

    butone2 = Button(root4, text="Close", command=root4.destroy)
    butone2.grid(row=8, column=1, padx=5, pady=5)

    root4.mainloop()


def Insert_Cho(tv):
    root4 = Tk()
    root4.geometry('500x300')
    root4.title('Insert Choosing')

    l1 = tk.Label(root4, text='Student ID')
    l1.grid(row=1, column=0, padx=5, pady=5)
    id_Entry = tk.Entry(root4, width=40)
    id_Entry.grid(row=1, column=1, padx=5, pady=5)

    l2 = tk.Label(root4, text='Course ID')
    l2.grid(row=2, column=0, padx=5, pady=5)
    cIDEntry = tk.Entry(root4, width=40)
    cIDEntry.grid(row=2, column=1, padx=5, pady=5)

    l3 = tk.Label(root4, text='Teacher ID')
    l3.grid(row=3, column=0, padx=5, pady=5)
    tIDEntry = tk.Entry(root4, width=30)
    tIDEntry.grid(row=3, column=1, padx=5, pady=5)

    l4 = tk.Label(root4, text='Chosen_year')
    l4.grid(row=4, column=0, padx=5, pady=5)
    ChoYearEntry = tk.Entry(root4, width=30)
    ChoYearEntry.grid(row=4, column=1, padx=5, pady=5)

    def try_insert():
        try:
            if len(str(id_Entry.get())) == 10:
                conn.execute("INSERT INTO " + "Choosing_information" + " ( " + "s_ID" + ", " +
                             "c_ID" + ", " + "t_ID" + ", " + "Chosen_year" + " ) VALUES ( '"
                             + str(id_Entry.get()) + "', '" + str(cIDEntry.get()) + "', '" +
                             str(tIDEntry.get()) + "', '" + str(ChoYearEntry.get()) + "' ); ")
                conn.commit()
                root4.destroy()
                tk.messagebox.showinfo("Success", "Data Saved Successfully. Please reload.")
            else:
                conn.rollback()
                tk.messagebox.showinfo("Fail", "Invalid Input(Student id) .")

        except sqlite3.OperationalError as e:
            conn.rollback()
            tk.messagebox.showinfo("Fail", "Ex: {}".format(e))

    butone1 = Button(root4, text="Yes", command=try_insert)
    butone1.grid(row=7, column=1, padx=5, pady=5)

    butone2 = Button(root4, text="Close", command=root4.destroy)
    butone2.grid(row=8, column=1, padx=5, pady=5)

    root4.mainloop()


def Delete_Stu(tv):
    try:
        selected = tv.focus()
        std = tv.item(selected, 'values')

        sql_delete = "DELETE FROM Students_information WHERE s_ID = " + str(std[0]) + ";"

        cur.execute(sql_delete)
        conn.commit()
        tk.messagebox.showinfo("Success", "Delete Success, please reload.")
    except:
        conn.rollback()
        tk.messagebox.showinfo("Fail", "Please select a Student.")


def Delete_Cou(tv):
    try:
        selected = tv.focus()
        course = tv.item(selected, 'values')

        sql_delete = "DELETE FROM Course_information WHERE c_ID = " + str(course[0]) + ";"

        cur.execute(sql_delete)
        conn.commit()
        tk.messagebox.showinfo("Success", "Delete Success, please reload.")
    except:
        conn.rollback()
        tk.messagebox.showinfo("Fail", "Please select a Course.")


def Delete_Tea(tv):
    try:
        selected = tv.focus()
        teacher = tv.item(selected, 'values')

        sql_delete = "DELETE FROM Teacher_information WHERE t_ID = {0};".format(
            str(teacher[0]))

        cur.execute(sql_delete)
        conn.commit()
        tk.messagebox.showinfo("Success", "Delete Success, please reload.")
    except:
        # sqlite3.OperationalError as e
        conn.rollback()
        tk.messagebox.showinfo("Fail", "Please select a Teacher: {}".format(''))


def Delete_Cho(tv):
    try:
        selected = tv.focus()
        std = tv.item(selected, 'values')

        sql_delete = "DELETE FROM Choosing_information WHERE s_ID = " + str(std[0]) + ";"

        cur.execute(sql_delete)
        conn.commit()
        tk.messagebox.showinfo("Success", "Delete Success, please reload.")
    except:
        conn.rollback()
        tk.messagebox.showinfo("Fail", "Please select a Choosing.")


def Modify_Std(tv):
    try:
        std = tv.item(tv.focus(), 'values')
        print(std[0])

        root4 = Tk()
        root4.geometry('500x300')
        root4.title('Insert Student')

        l1 = tk.Label(root4, text='Student ID')
        l1.grid(row=1, column=0, padx=5, pady=5)
        id_Entry = tk.Label(root4, text=str(std[0]))
        id_Entry.grid(row=1, column=1, padx=5, pady=5)

        l2 = tk.Label(root4, text='Student Name')
        l2.grid(row=2, column=0, padx=5, pady=5)
        NameEntry = tk.Entry(root4, width=40)
        NameEntry.insert(0, str(std[1]))
        NameEntry.grid(row=2, column=1, padx=5, pady=5)

        l3 = tk.Label(root4, text='Sex')
        l3.grid(row=3, column=0, padx=5, pady=5)

        def male():
            SexEntry.config(text='male')

        def female():
            SexEntry.config(text='female')

        print(std[2])
        SexEntry = tk.Label(root4, text=std[2])
        SexEntry.grid(row=3, column=1, padx=5, pady=5)

        male_button = Button(root4, text="male", command=male)
        female_button = Button(root4, text="female", command=female)
        male_button.grid(row=3, column=2, padx=5, pady=5)
        female_button.grid(row=3, column=3, padx=5, pady=5)

        l4 = tk.Label(root4, text='Entrance_Age')
        l4.grid(row=4, column=0, padx=5, pady=5)
        AgeEntry = tk.Entry(root4, width=30)
        AgeEntry.insert(0, str(std[3]))
        AgeEntry.grid(row=4, column=1, padx=5, pady=5)

        l5 = tk.Label(root4, text='Entrance_Year')
        l5.grid(row=5, column=0, padx=5, pady=5)
        YearEntry = tk.Entry(root4, width=30)
        YearEntry.insert(0, str(std[4]))
        YearEntry.grid(row=5, column=1, padx=5, pady=5)

        l6 = tk.Label(root4, text='Class')
        l6.grid(row=6, column=0, padx=5, pady=5)
        ClassEntry = tk.Entry(root4, width=30)
        ClassEntry.insert(0, str(std[5]))
        ClassEntry.grid(row=6, column=1, padx=5, pady=5)

        def try_modify():
            try:
                conn.execute("UPDATE " + "Students_information SET s_Name = '"
                             + str(NameEntry.get()) + "' WHERE s_ID = " + std[0])
                conn.execute("UPDATE " + "Students_information SET Sex = '"
                             + str(SexEntry.cget("text")) + "' WHERE s_ID = " + std[0])
                conn.execute("UPDATE " + "Students_information SET Entrance_Age = '"
                             + str(AgeEntry.get()) + "' WHERE s_ID = " + std[0])
                conn.execute("UPDATE " + "Students_information SET Entrance_Year = '"
                             + str(YearEntry.get()) + "' WHERE s_ID = " + std[0])
                conn.execute("UPDATE " + "Students_information SET Class = '"
                             + str(ClassEntry.get()) + "' WHERE s_ID = " + std[0])
                conn.commit()
                root4.destroy()
                tk.messagebox.showinfo("Success", "Data Saved Successfully. Please reload.")
            except sqlite3.OperationalError as e:
                conn.rollback()
                root4.destroy()
                tk.messagebox.showinfo("Fail", "EX: {}".format(e))

        butone1 = Button(root4, text="Yes", command=try_modify)
        butone1.grid(row=7, column=1, padx=5, pady=5)

        butone2 = Button(root4, text="Close", command=root4.destroy)
        butone2.grid(row=8, column=1, padx=5, pady=5)

        root4.mainloop()
    except:
        conn.rollback()
        tk.messagebox.showinfo("Fail", "Please select a Student.")


def Modify_Cou(tv):
    try:
        cou = tv.item(tv.focus(), 'values')
        print(cou[0])

        root4 = Tk()
        root4.geometry('500x300')
        root4.title('Modify Course')

        l1 = tk.Label(root4, text='Course ID')
        l1.grid(row=1, column=0, padx=5, pady=5)
        id_Entry = tk.Label(root4, text=cou[0])
        id_Entry.grid(row=1, column=1, padx=5, pady=5)

        l2 = tk.Label(root4, text='Course Name')
        l2.grid(row=2, column=0, padx=5, pady=5)
        NameEntry = tk.Entry(root4, width=40)
        NameEntry.insert(0, cou[1])
        NameEntry.grid(row=2, column=1, padx=5, pady=5)

        l3 = tk.Label(root4, text='Teacher ID')
        l3.grid(row=3, column=0, padx=5, pady=5)
        tIDEntry = tk.Entry(root4, width=30)
        tIDEntry.insert(0, cou[2])
        tIDEntry.grid(row=3, column=1, padx=5, pady=5)

        l4 = tk.Label(root4, text='Credit')
        l4.grid(row=4, column=0, padx=5, pady=5)
        CreditEntry = tk.Entry(root4, width=30)
        CreditEntry.insert(0, cou[3])
        CreditEntry.grid(row=4, column=1, padx=5, pady=5)

        l5 = tk.Label(root4, text='Grade')
        l5.grid(row=5, column=0, padx=5, pady=5)
        GradeEntry = tk.Entry(root4, width=30)
        GradeEntry.insert(0, cou[4])
        GradeEntry.grid(row=5, column=1, padx=5, pady=5)

        l6 = tk.Label(root4, text='Canceled_Year')
        l6.grid(row=6, column=0, padx=5, pady=5)
        YearEntry = tk.Entry(root4, width=30)
        YearEntry.insert(0, cou[5])
        YearEntry.grid(row=6, column=1, padx=5, pady=5)

        def try_modify():
            sql_create_cou = "create table if not exists Course_information" \
                             "(c_ID int(7) primary key," \
                             "c_Name text," \
                             "t_ID int," \
                             "Credit int," \
                             "Grade int," \
                             "Canceled_Year int)"
            try:
                conn.execute("UPDATE " + "Course_information SET c_Name = '"
                             + str(NameEntry.get()) + "' WHERE c_ID = " + cou[0])
                conn.execute("UPDATE " + "Course_information SET t_ID = '"
                             + str(tIDEntry.get()) + "' WHERE c_ID = " + cou[0])
                conn.execute("UPDATE " + "Course_information SET Credit = '"
                             + str(CreditEntry.get()) + "' WHERE c_ID = " + cou[0])
                conn.execute("UPDATE " + "Course_information SET Grade = '"
                             + str(GradeEntry.get()) + "' WHERE c_ID = " + cou[0])
                conn.execute("UPDATE " + "Course_information SET Canceled_Year = '"
                             + str(YearEntry.get()) + "' WHERE c_ID = " + cou[0])
                conn.commit()
                root4.destroy()
                tk.messagebox.showinfo("Success", "Data Saved Successfully. Please reload.")
            except sqlite3.OperationalError as e:
                conn.rollback()
                root4.destroy()
                tk.messagebox.showinfo("Fail", "EX:{}".format(e))

        butone1 = Button(root4, text="Yes", command=try_modify)
        butone1.grid(row=7, column=1, padx=5, pady=5)

        butone2 = Button(root4, text="Close", command=root4.destroy)
        butone2.grid(row=8, column=1, padx=5, pady=5)

        root4.mainloop()
    except:
        conn.rollback()
        tk.messagebox.showinfo("Fail", "Please select a Course.")


def Modify_Tea(tv):
    try:
        tea = tv.item(tv.focus(), 'values')
        print(tea[0])
        root4 = Tk()
        root4.geometry('500x300')
        root4.title('Insert Teacher')

        l1 = tk.Label(root4, text='Teacher ID')
        l1.grid(row=1, column=0, padx=5, pady=5)
        Id_Entry = tk.Label(root4, text=tea[0])
        Id_Entry.grid(row=1, column=1, padx=5, pady=5)

        l2 = tk.Label(root4, text='Teacher Name')
        l2.grid(row=2, column=0, padx=5, pady=5)
        NameEntry = tk.Entry(root4, width=40)
        NameEntry.insert(0, tea[1])
        NameEntry.grid(row=2, column=1, padx=5, pady=5)

        l3 = tk.Label(root4, text='Courses')
        l3.grid(row=3, column=0, padx=5, pady=5)
        CourseEntry = tk.Entry(root4, width=30)
        CourseEntry.insert(0, tea[2])
        CourseEntry.grid(row=3, column=1, padx=5, pady=5)

        def try_insert():
            try:
                conn.execute("UPDATE " + "Teacher_information SET Name = '"
                             + str(NameEntry.get()) + "' WHERE t_ID = " + tea[0])
                conn.execute("UPDATE " + "Teacher_information SET c_Name = '"
                             + str(CourseEntry.get()) + "' WHERE t_ID = " + tea[0])

                conn.commit()
                root4.destroy()
                tk.messagebox.showinfo("Success", "Data Saved Successfully. Please reload.")
            except sqlite3.OperationalError as e:
                conn.rollback()
                tk.messagebox.showinfo("Fail", "Ex: {}".format(e))

        butone1 = Button(root4, text="Yes", command=try_insert)
        butone1.grid(row=7, column=1, padx=5, pady=5)

        butone2 = Button(root4, text="Close", command=root4.destroy)
        butone2.grid(row=8, column=1, padx=5, pady=5)

        root4.mainloop()
    except:
        conn.rollback()
        tk.messagebox.showinfo("Fail", "Please select a Teacher.")


def Modify_Cho(tv):
    try:
        cho = tv.item(tv.focus(), 'values')
        print(cho[0])

        root4 = Tk()
        root4.geometry('500x300')
        root4.title('Insert Choosing')

        l1 = tk.Label(root4, text='Student ID')
        l1.grid(row=1, column=0, padx=5, pady=5)
        id_Entry = tk.Label(root4, text=cho[0])
        id_Entry.grid(row=1, column=1, padx=5, pady=5)

        l2 = tk.Label(root4, text='Course ID')
        l2.grid(row=2, column=0, padx=5, pady=5)
        cIDEntry = tk.Entry(root4, width=40)
        cIDEntry.insert(0, cho[1])
        cIDEntry.grid(row=2, column=1, padx=5, pady=5)

        l3 = tk.Label(root4, text='Teacher ID')
        l3.grid(row=3, column=0, padx=5, pady=5)
        tIDEntry = tk.Entry(root4, width=30)
        tIDEntry.insert(0, cho[2])
        tIDEntry.grid(row=3, column=1, padx=5, pady=5)

        l4 = tk.Label(root4, text='Chosen_year')
        l4.grid(row=4, column=0, padx=5, pady=5)
        ChoYearEntry = tk.Entry(root4, width=30)
        ChoYearEntry.insert(0, cho[3])
        ChoYearEntry.grid(row=4, column=1, padx=5, pady=5)

        def try_insert():
            try:
                conn.execute("UPDATE " + "Choosing_information SET c_ID = '"
                             + str(cIDEntry.get()) + "' WHERE s_ID = " + cho[0])
                conn.execute("UPDATE " + "Choosing_information SET t_ID = '"
                             + str(tIDEntry.get()) + "' WHERE s_ID = " + cho[0])
                conn.execute("UPDATE " + "Choosing_information SET Chosen_year = '"
                             + str(ChoYearEntry.get()) + "' WHERE s_ID = " + cho[0])

                conn.commit()
                root4.destroy()
                tk.messagebox.showinfo("Success", "Data Saved Successfully. Please reload.")

            except sqlite3.OperationalError as e:
                conn.rollback()
                tk.messagebox.showinfo("Fail", "Ex: {}".format(e))

        butone1 = Button(root4, text="Yes", command=try_insert)
        butone1.grid(row=7, column=1, padx=5, pady=5)

        butone2 = Button(root4, text="Close", command=root4.destroy)
        butone2.grid(row=8, column=1, padx=5, pady=5)

        root4.mainloop()
    except:
        conn.rollback()
        tk.messagebox.showinfo("Fail", "Please select a Choosing.")


def Modify_Score(tv):
    try:
        cho = tv.item(tv.focus(), 'values')
        print(cho[0])

        root4 = Tk()
        root4.geometry('500x300')
        root4.title('Insert Choosing')

        l1 = tk.Label(root4, text='Student ID')
        l1.grid(row=1, column=0, padx=5, pady=5)
        id_Entry = tk.Label(root4, text=cho[0])
        id_Entry.grid(row=1, column=1, padx=5, pady=5)

        l2 = tk.Label(root4, text='Course ID')
        l2.grid(row=2, column=0, padx=5, pady=5)
        cIDEntry = tk.Label(root4, text=cho[1])
        cIDEntry.grid(row=2, column=1, padx=5, pady=5)

        l3 = tk.Label(root4, text='Teacher ID')
        l3.grid(row=3, column=0, padx=5, pady=5)
        tIDEntry = tk.Label(root4, text=cho[2])
        tIDEntry.grid(row=3, column=1, padx=5, pady=5)

        l4 = tk.Label(root4, text='Chosen_year')
        l4.grid(row=4, column=0, padx=5, pady=5)
        ChoYearEntry = tk.Label(root4, text=cho[3])
        ChoYearEntry.grid(row=4, column=1, padx=5, pady=5)

        l4 = tk.Label(root4, text='Score')
        l4.grid(row=5, column=0, padx=5, pady=5)
        ScoreEntry = tk.Entry(root4, width=30)
        ScoreEntry.insert(0, cho[4])
        ScoreEntry.grid(row=5, column=1, padx=5, pady=5)

        def try_insert():
            try:
                conn.execute("UPDATE " + "Choosing_information SET Score = '"
                             + str(ScoreEntry.get()) + "' WHERE s_ID = " + cho[0])

                conn.commit()
                root4.destroy()
                tk.messagebox.showinfo("Success", "Data Saved Successfully. Please reload.")

            except sqlite3.OperationalError as e:
                conn.rollback()
                tk.messagebox.showinfo("Fail", "Ex: {}".format(e))

        butone1 = Button(root4, text="Yes", command=try_insert)
        butone1.grid(row=7, column=1, padx=5, pady=5)

        butone2 = Button(root4, text="Close", command=root4.destroy)
        butone2.grid(row=8, column=1, padx=5, pady=5)

        root4.mainloop()
    except:
        conn.rollback()
        tk.messagebox.showinfo("Fail", "Please select a Choosing.")


def query_score():
    root4 = Tk()
    root4.geometry('500x300')
    root4.title('query score')

    l2 = tk.Label(root4, text='Student ID')
    l2.grid(row=2, column=0, padx=5, pady=5)
    cIDEntry = tk.Entry(root4, width=40)
    cIDEntry.grid(row=2, column=1, padx=5, pady=5)

    l3 = tk.Label(root4, text='Student Name')
    l3.grid(row=3, column=0, padx=5, pady=5)
    tIDEntry = tk.Entry(root4, width=30)
    tIDEntry.grid(row=3, column=1, padx=5, pady=5)

    def try_search(info1=cIDEntry.get(), info2=tIDEntry.get()):

        l2.grid_forget()
        l3.grid_forget()
        cIDEntry.grid_forget()
        tIDEntry.grid_forget()
        butone1.grid_forget()
        butone2.grid_forget()
        root4.geometry(pageGeo)
        tree = ttk.Treeview(root4, height=20)

        tree["columns"] = ("one", "two", "three", "four", "five")
        tree.heading("one", text="Student ID")
        tree.heading("two", text="Course ID")
        tree.heading("three", text="Teacher ID")
        tree.heading("four", text="Chosen_year")
        tree.heading("five", text="Score")

        print(len(cIDEntry.get()))

        try:
            info = ""
            if len(cIDEntry.get()) >= 9:
                info = cIDEntry.get()
                cursor = conn.execute("SELECT * "
                                      "FROM Choosing_information "
                                      "WHERE s_ID = " + info + " ;")
                i = 0
                for row in cursor:
                    tree.insert('', i, text="Choosing " + str(i + 1),
                                values=(row[0], row[1], row[2],
                                        row[3], row[4]))
                    i = i + 1
            else:
                info = tIDEntry.get()
                cursor = conn.execute("SELECT c.s_ID, c.c_ID, c.t_ID, c.Chosen_year, c.Score "
                                      "FROM Choosing_information as c, Student_information as s,"
                                      "WHERE s.s_Name = " + info + " AND c.s_ID = c.s_ID;")
                i = 0
                for row in cursor:
                    tree.insert('', i, text="Choosing " + str(i + 1),
                                values=(row[0], row[1], row[2],
                                        row[3], row[4]))
                    i = i + 1

            conn.commit()
            tree.grid()
        except sqlite3.OperationalError as e:
            conn.rollback()
            tk.messagebox.showinfo("Fail", "Ex: {}".format(e))

    butone1 = Button(root4, text="Yes", command=try_search)
    butone1.grid(row=7, column=1, padx=5, pady=5)

    butone2 = Button(root4, text="Close", command=root4.destroy)
    butone2.grid(row=8, column=1, padx=5, pady=5)

    root4.mainloop()


def query_course():
    root4 = Tk()
    root4.geometry('500x300')
    root4.title('query course')

    l2 = tk.Label(root4, text='Student ID')
    l2.grid(row=2, column=0, padx=5, pady=5)
    sIDEntry = tk.Entry(root4, width=40)
    sIDEntry.grid(row=2, column=1, padx=5, pady=5)

    l3 = tk.Label(root4, text='Student Name')
    l3.grid(row=3, column=0, padx=5, pady=5)
    tIDEntry = tk.Entry(root4, width=30)
    tIDEntry.grid(row=3, column=1, padx=5, pady=5)

    def try_search(info1=sIDEntry.get(), info2=tIDEntry.get()):

        l2.grid_forget()
        l3.grid_forget()
        sIDEntry.grid_forget()
        tIDEntry.grid_forget()
        butone1.grid_forget()
        butone2.grid_forget()
        root4.geometry(pageGeo)
        tree = ttk.Treeview(root4, height=20)

        tree["columns"] = ("one", "two", "three", "four", "five", "six")
        tree.heading("one", text="Course ID")
        tree.heading("two", text="Course Name")
        tree.heading("three", text="Teacher ID")
        tree.heading("four", text="Credit")
        tree.heading("five", text="Grade")
        tree.heading("six", text="Canceled_Year")

        print(len(sIDEntry.get()))
        try:
            info = ""
            if len(sIDEntry.get()) >= 9:
                info = sIDEntry.get()
                cursor = conn.execute("SELECT c.c_ID, c.c_Name, c.t_ID, c.Credit, c.Grade, c.Canceled_Year "
                                      "FROM Course_information as c, Students_information as s, Choosing_information "
                                      "as ch "
                                      "WHERE s.s_ID = " + info + " AND ch.s_ID = s.s_ID AND c.c_ID = ch.c_ID;")
                i = 0
                for row in cursor:
                    tree.insert('', i, text="Course " + str(i + 1),
                                values=(row[0], row[1], row[2],
                                        row[3], row[4], row[5]))
                    i = i + 1
            else:
                info = tIDEntry.get()
                cursor = conn.execute("SELECT c.c_ID, c.c_Name, c.t_ID, c.Credit, c.Grade, c.Canceled_Year "
                                      "FROM Course_information as c, Students_information as s, Choosing_information "
                                      "as ch "
                                      "WHERE s.s_Name = " + info + " AND ch.s_ID = s.s_ID AND c.c_ID = ch.c_ID;")
                i = 0
                for row in cursor:
                    tree.insert('', i, text="Course " + str(i + 1),
                                values=(row[0], row[1], row[2],
                                        row[3], row[4], row[5]))
                    i = i + 1

            conn.commit()
            tree.grid()
        except sqlite3.OperationalError as e:
            conn.rollback()
            tk.messagebox.showinfo("Fail", "Ex: {}".format(e))

    butone1 = Button(root4, text="Yes", command=try_search)
    butone1.grid(row=7, column=1, padx=5, pady=5)

    butone2 = Button(root4, text="Close", command=root4.destroy)
    butone2.grid(row=8, column=1, padx=5, pady=5)

    root4.mainloop()


def query_teacher():
    root4 = Tk()
    root4.geometry('500x300')
    root4.title('query teacher')

    l2 = tk.Label(root4, text='Teacher ID')
    l2.grid(row=2, column=0, padx=5, pady=5)
    sIDEntry = tk.Entry(root4, width=40)
    sIDEntry.grid(row=2, column=1, padx=5, pady=5)

    l3 = tk.Label(root4, text='Teacher Name')
    l3.grid(row=3, column=0, padx=5, pady=5)
    tIDEntry = tk.Entry(root4, width=30)
    tIDEntry.grid(row=3, column=1, padx=5, pady=5)

    def try_search(info1=sIDEntry.get(), info2=tIDEntry.get()):

        l2.grid_forget()
        l3.grid_forget()
        sIDEntry.grid_forget()
        tIDEntry.grid_forget()
        butone1.grid_forget()
        butone2.grid_forget()
        root4.geometry(pageGeo)
        tree = ttk.Treeview(root4, height=20)

        tree["columns"] = ("one", "two", "three")
        tree.heading("one", text="Teacher ID")
        tree.heading("two", text="Teacher Name")
        tree.heading("three", text="Classes name")
        print(len(sIDEntry.get()))

        try:
            info = ""
            if len(sIDEntry.get()) >= 5:
                info = sIDEntry.get()
                cursor = conn.execute("SELECT * "
                                      "FROM Teacher_information "
                                      "WHERE t_ID = " + info + " ")
                i = 0
                for row in cursor:
                    tree.insert('', i, text=" result " + str(i + 1),
                                values=(row[0], row[1], row[2]))
                    i = i + 1
            else:
                info = tIDEntry.get()
                cursor = conn.execute("SELECT * "
                                      "FROM Teacher_information "
                                      "WHERE Name = " + info + " ")
                i = 0
                for row in cursor:
                    tree.insert('', i, text=" result " + str(i + 1),
                                values=(row[0], row[1], row[2]))
                    i = i + 1

            conn.commit()
            tree.grid()
        except sqlite3.OperationalError as e:
            conn.rollback()
            tk.messagebox.showinfo("Fail", "Ex: {}".format(e))

    butone1 = Button(root4, text="Yes", command=try_search)
    butone1.grid(row=7, column=1, padx=5, pady=5)

    butone2 = Button(root4, text="Close", command=root4.destroy)
    butone2.grid(row=8, column=1, padx=5, pady=5)

    root4.mainloop()


def average():
    root4 = Tk()
    root4.geometry('500x300')
    root4.title('Average Score')

    l2 = tk.Label(root4, text='A student (id)')
    l2.grid(row=2, column=0, padx=5, pady=5)
    sIDEntry = tk.Entry(root4, width=40)
    sIDEntry.grid(row=2, column=1, padx=5, pady=5)

    l3 = tk.Label(root4, text='A class')
    l3.grid(row=3, column=0, padx=5, pady=5)
    tIDEntry = tk.Entry(root4, width=30)
    tIDEntry.grid(row=3, column=1, padx=5, pady=5)

    l4 = tk.Label(root4, text='A Course (id)')
    l4.grid(row=4, column=0, padx=5, pady=5)
    cIDEntry = tk.Entry(root4, width=30)
    cIDEntry.grid(row=4, column=1, padx=5, pady=5)

    def try_search(info1=sIDEntry.get(), info2=tIDEntry.get()):

        sIDEntry.grid_forget()
        tIDEntry.grid_forget()
        cIDEntry.grid_forget()
        butone1.grid_forget()
        butone2.grid_forget()

        try:
            info = ""
            if len(sIDEntry.get()) == 10:
                l4.grid_forget()
                l3.grid_forget()
                info = sIDEntry.get()
                cursor = conn.execute("SELECT AVG(ch.Score) "
                                      "FROM Choosing_information as ch "
                                      "WHERE ch.s_ID = " + info + " ;")

                l5 = tk.Label(root4, text="")
                for row in cursor:
                    l5 = tk.Label(root4, text=row[0])
                l5.grid(row=3, column=0, padx=5, pady=5)

            elif len(cIDEntry.get()) == 7:
                l2.grid_forget()
                l4.grid_forget()
                info = sIDEntry.get()
                cursor = conn.execute("SELECT AVG(ch.Score) "
                                      "FROM Choosing_information as ch "
                                      "WHERE ch.c_ID = " + info + " ;")

                l5 = tk.Label(root4, text="")
                for row in cursor:
                    l5 = tk.Label(root4, text=row[0])
                l5.grid(row=3, column=0, padx=5, pady=5)

            else:
                l2.grid_forget()
                l3.grid_forget()
                info = tIDEntry.get()
                cursor = conn.execute("SELECT AVG(ch.Score) "
                                      "FROM Choosing_information as ch "
                                      "WHERE ch.s_ID = " + info + " ;")

                l5 = tk.Label(root4, text="")
                for row in cursor:
                    l5 = tk.Label(root4, text=row[0])
                l5.grid(row=3, column=0, padx=5, pady=5)

            conn.commit()
        except sqlite3.OperationalError as e:
            conn.rollback()
            tk.messagebox.showinfo("Fail", "Ex: {}".format(e))

    butone1 = Button(root4, text="Yes", command=try_search)
    butone1.grid(row=7, column=1, padx=5, pady=5)

    butone2 = Button(root4, text="Close", command=root4.destroy)
    butone2.grid(row=8, column=1, padx=5, pady=5)

    root4.mainloop()


def display_data(root, table):
    tree = ttk.Treeview(root, height=20)

    if table == "Students_information":
        tree["columns"] = ("one", "two", "three", "four", "five", "six")
        tree.heading("one", text="Student ID")
        tree.heading("two", text="Student Name")
        tree.heading("three", text="Sex")
        tree.heading("four", text="Entrance_Age")
        tree.heading("five", text="Entrance_Year")
        tree.heading("six", text="Class")

        cursor = conn.execute("SELECT * FROM " + table + " ;")
        i = 0
        for row in cursor:
            tree.insert('', i, text="Student " + str(i + 1),
                        values=(row[0], row[1], row[2],
                                row[3], row[4],
                                row[5]))
            i = i + 1

    if table == "Course_information":
        tree["columns"] = ("one", "two", "three", "four", "five", "six")
        tree.heading("one", text="Course ID")
        tree.heading("two", text="Course Name")
        tree.heading("three", text="Teacher ID")
        tree.heading("four", text="Credit")
        tree.heading("five", text="Grade")
        tree.heading("six", text="Canceled_Year")

        cursor = conn.execute("SELECT * FROM " + table + " ;")
        i = 0
        for row in cursor:
            tree.insert('', i, text="Course " + str(i + 1),
                        values=(row[0], row[1], row[2],
                                row[3], row[4],
                                row[5]))
            i = i + 1

    if table == "Teacher_information":
        tree["columns"] = ("one", "two", "three")
        tree.heading("one", text="Teacher ID")
        tree.heading("two", text="Teacher Name")
        tree.heading("three", text="Classes name")

        cursor = conn.execute("SELECT * FROM " + table + " ;")
        i = 0
        for row in cursor:
            tree.insert('', i, text="Teacher " + str(i + 1),
                        values=(row[0], row[1], row[2]))
            i = i + 1

    if table == "Choosing_information":
        tree["columns"] = ("one", "two", "three", "four", "five")
        tree.heading("one", text="Student ID")
        tree.heading("two", text="Course ID")
        tree.heading("three", text="Teacher ID")
        tree.heading("four", text="Chosen_year")
        tree.heading("five", text="Score")

        cursor = conn.execute("SELECT * FROM " + table + " ;")
        i = 0
        for row in cursor:
            tree.insert('', i, text="Choosing " + str(i + 1),
                        values=(row[0], row[1], row[2],
                                row[3], row[4]))
            i = i + 1

    return tree


def create_Student_table():
    sql_create_std = "create table if not exists Students_information" \
                     "(s_ID int(10)  NOT NULL," \
                     "s_Name text NOT NULL," \
                     "Sex text NOT NULL," \
                     "Entrance_Age int NOT NULL," \
                     "Entrance_Year int NOT NULL," \
                     "Class text NOT NULL," \
                     "primary key (s_ID))"
    conn.execute(sql_create_std)


def create_Course_table():
    sql_create_cou = "create table if not exists Course_information" \
                     "(c_ID int(7)  NOT NULL," \
                     "c_Name text NOT NULL," \
                     "t_ID int NOT NULL," \
                     "Credit int NOT NULL," \
                     "Grade int NOT NULL," \
                     "Canceled_Year int NOT NULL," \
                     "primary key(c_ID)" \
                     "foreign key(t_ID) references Teacher_information)"
    conn.execute(sql_create_cou)


def create_Teacher_table():
    sql_create_tea = "create table if not exists Teacher_information" \
                     "(t_ID int(5)  NOT NULL," \
                     "Name text NOT NULL," \
                     "c_Name text NOT NULL)"
    conn.execute(sql_create_tea)


def create_Choosing_table():
    sql_create_cho = "create table if not exists Choosing_information" \
                     "(s_ID int(10)  NOT NULL," \
                     "c_ID int(7) NOT NULL," \
                     "t_ID int(5) NOT NULL," \
                     "Chosen_year int NOT NULL," \
                     "Score int," \
                     "foreign key (s_ID) references Students_information," \
                     "foreign key (c_ID) references Course_information," \
                     "foreign key (t_ID) references Teacher_information)"
    conn.execute(sql_create_cho)


def GetTables():
    try:
        cur.execute("select name from sqlite_master where type='table' order by name")
        print(cur.fetchall())
    except:
        print(sqlite3.Error())


if __name__ == '__main__':
    # 建立表格
    # cur.execute("DROP TABLE Course_information;")

    create_Choosing_table()
    create_Teacher_table()
    create_Course_table()
    create_Student_table()

    GetTables()

    sql_select2 = "select * from Students_information"
    cur.execute(sql_select2)
    lst = cur.fetchall()
    print(f"共{len(lst)}条记录")
    print(lst)

    # （7）从sqlite_master表中查询数据表的名称和创建时的sql语句，查询结果赋值给列表，并输出列表内容
    cur.execute("select name,sql from sqlite_master ")

    LoginPage()

    # （8）关闭连接
    conn.commit()
    cur.close()
    conn.close()
