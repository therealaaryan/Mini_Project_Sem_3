from tkinter import *
import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="mysql",database="project")
cursor=mycon.cursor()
root=Tk()

def save1():
    cursor.execute("insert into record values(\""+un_id_entry.get()+"\",\""+name_entry.get()+"\",\""+gender_entry.get()+"\",\""+address_entry.get()+"\",\""+height_entry.get()+"\",\""+weight_entry.get()+"\",\""+bloodgrp_entry.get()+"\",\""+allergies_entry.get()+"\",\""+ongmed_entry.get()+"\"")

def save2():
    cursor.execute("Delete from record where unique_id={}".format(uid_enter.get()))

def display():
    pot=Toplevel()
    pot.title("Display")
    global unique_id_enter
    unique_id_label=Label(pot,text="Unique ID: ").grid(row=0,column=0)
    unique_id_enter=Entry(pot,width=10).grid(row=1,column=0)
    check_button=Button(pot,text="Check in Records",command=check).grid(row=2,column=0)
    exit_b=Button(pot,text="Exit",command=pot.quit).grid(row=2,column=1)

def check():
    cursor.execute("select * from record where unique_id={};".format(unique_id_enter.get()))

def add():
    top=Toplevel()
    top.title("Add")
    global un_id_entry
    global name_entry
    global age_entry
    global gender_entry
    global address_entry
    global height_entry
    global weight_entry
    global bloodgrp_entry
    global allergies_entry
    global ongmed_entry

    un_id_label=Label(top,text="Unique ID: ").grid(row=0,column=0)
    un_id_entry=Entry(top,width=10).grid(row=0,column=1)

    name_label=Label(top,text="Name: ").grid(row=1,column=0)
    name_entry=Entry(top,width=50).grid(row=1,column=1)

    age_label=Label(top,text="Age: ").grid(row=2,column=0)
    age_entry=Entry(top,width=10).grid(row=2,column=1)

    gender_label=Label(top,text="Gender: ").grid(row=3,column=0)
    gender_entry=Entry(top,width=10).grid(row=3,column=1)

    address_label=Label(top,text="Address: ").grid(row=4,column=0)
    address_entry=Entry(top,width=50).grid(row=4,column=1)

    height_label=Label(top,text="Height: ").grid(row=5,column=0)
    height_entry=Entry(top,width=10).grid(row=5,column=1)

    weight_label=Label(top,text="Weight: ").grid(row=6,column=0)
    weight_entry=Entry(top,width=10).grid(row=6,column=1)

    bloodgrp_label=Label(top,text="Blood Group: ").grid(row=7,column=0)
    bloodgrp_entry=Entry(top,width=10).grid(row=7,column=1)

    allergies_label=Label(top,text="Allergies: ").grid(row=8,column=0)
    allergies_entry=Entry(top,width=30).grid(row=8,column=1)

    ongmed_label=Label(top,text="Ongoing Medications: ").grid(row=9,column=0)
    ongmed_entry=Entry(top,width=30).grid(row=9,column=1)

    save_button=Button(top,text="Save",command=save1).grid(row=10,column=0)
    exit_but=Button(top,text="Exit",command=top.quit).grid(row=10,column=1)

    
def delete():
    global uid_enter
    got=Toplevel()
    got.title("Delete")
    uid_label=Label(got,text="Unique ID: ").grid(row=0,column=0)
    uid_enter=Entry(got,width=10).grid(row=1,column=1)
    delete_but=Button(got,text="Delete",command=save2).grid(row=2,column=0)
    exit_bu=Button(got,text="Exit",command=got.quit).grid(row=2,column=1)
    
    
display_button=Button(root,text="Display My Record",command=display).grid(row=0,column=0)
add_button=Button(root,text="Add Record",command=add).grid(row=0,column=1)
delete_button=Button(root,text="Delete record",command=delete).grid(row=0,column=2)



root.title("Medical Record")

exit_button=Button(root,text="Exit",command=root.quit).grid(row=11,column=10)
root.mainloop()
