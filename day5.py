# # NumPy-Numerical python
# import numpy as n
# a=n.array([1,2,3,4,5,6,7])
# prin(a)

# name=input("enter the name : ")
# fees=int(input("Enter the fees: "))
# f=open("jspm.txt","w")
# f.write(name+","+str(fees)+"\n")

# f1=open("jspm.txt","r") #use to only read data
# rec=f1.readline()
# while rec!="":
#     print(rec)
#     field=rec.split(",")
#     stud_name=field[0]
#     fees=field[1]
#     if int(fees)>500:
#         print("name is: ",stud_name)
#     rec=f1.readline()

# ###############################################################
#DATA HANDLING
# class test:
#     def write(self):
#         # n=int(input("Total no of data:"))
#         # for i in range(0,n):
#             fname=input("First-name : ")
#             lname=input("Last-name: ")
#             y=input("Year : ")
#             fees=int(input("Enter the fees: "))
#             f=open("jspm.txt","w")
#             f.write(fname+","+lname+","+y+","+str(fees)+"\n")

#     def display(self):
#         f1=open("jspm.txt","r") #use to only read data
#         rec=f1.read()
#         while rec!="":
#             i=0
#             print(rec)
#             field=rec.split(",")
#             stud_name=field[i]
#             fees=field[i+1]
#             if int(fees)>90000:
#                 print("name is: ",stud_name)
#             rec=f1.readline()
#             i=i+1
# t=test()
# t.write()
# t.display()
#########################################################################
import sqlite3
def create(cur):
    sql='''create table jspm(
        id integer,
        name text,
        address text,
        phone integer,
        primary key (id))'''
    cur.execute(sql)
    print("table created")
def insert():
    selcmd="insert into jspm values(101,'JSPMRSCOE','PUNE',85467)"
    cur.execute(selcmd)
    print("dat inserted successfully")
    conn.commit()

def display():
    sql="select * from jspm"
    rec=cur.execute(sql)
    for i in rec:
        print(i)
def dis2():
    for i in cur.execute("select name,phone from jspm"):
        n,contact=i
        print("name:",n,"\nphone:",contact)

# def update():
#     p=input("enter no:")
#     secmd="UPDATE jspm SET phone = p"
#     cur.execute(secmd)
#     print("data updated successfully")
#     conn.commit()
#     dis2()
# def insert2():
#     li=[]
#     name=input("enter name:")
#     id=int(input("enter id:"))
#     add=input("address:")
#     ph=int(input("phone number:"))
#     li.append(id)
#     li.append(name)
#     li.append(add)
#     li.append(ph)
#     selcmd="insert into jspm values(?,?,?,?)"
#     cur.execute(selcmd)
#     print("data inserted successfully")
#     conn.commit()
#     insert2()

 



# #main
# conn=sqlite3.connect("university.db")
# cur=conn.cursor()
# # create(cur)
# #insert()
# # dis2()
# # update()
# insert2()
# display()
####################################################################
# import pandas as pd
# data={'test':[1,2,3,4],
#       'name':['a','b','c','d'],
#       'fees':[100,200,300,400]}
# df=pd.Dataframe(data)
# print(df)
# pyplot module is used to draw praph
###################################################################################################
# from tkinter import *
# from tkinter import messagebox
# def test():
#     userid=t1.get()
#     password=t2.get()
#     if password=="kp25@123":
#         messagebox.showinfo("login successfully")
#     else:
#         messagebox.showinfo("invalid password")
# def reset_fun():
#     t1.delete(0,END)
#     t2.delete(0,END)
#     t1.insert(0,"insert user id:")



# root=Tk()
# root.title("first GUI")
# root.geometry("500x500")
# l1=Label(text="welcome to jspm API",font=(14))
# l1.grid(row=1,column=2,padx=5,pady=5)
# l2=Label(text="enter name",font=(14))
# l2.grid(row=2,column=1,padx=5,pady=5)

# t1=Entry(font=(14))
# t1.grid(row=2,column=2,padx=5,pady=5)
# l3=Label(text="password:",font=(14))
# l3.grid(row=3,column=1,padx=5,pady=5)
# t2=Entry(font=(14),show="*")
# t2.grid(row=3,column=2,padx=5,pady=5)
# b1=Button(text="Submit:",command=test)
# b1.grid(row=4,column=2,padx=5,pady=5)
# root.mainloop()
#####################################################################################
## CALCULATOR ##
from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("CALCULATOR USING PYTHON")
root.geometry("500x500")
l1=Label(text="CALCULATOR",font=(14))
l1.grid(row=1,column=2,padx=5,pady=5)

b1=Button(text="1")
b1.grid(row=2,column=1,padx=5,pady=5)
b2=Button(text="2")
b2.grid(row=2,column=2,padx=5,pady=5)
b3=Button(text="3")
b3.grid(row=2,column=3,padx=5,pady=5)
b4=Button(text="4")
b4.grid(row=3,column=1,padx=5,pady=5)
b5=Button(text="5")
b5.grid(row=3,column=2,padx=5,pady=5)
b6=Button(text="6")
b6.grid(row=3,column=3,padx=5,pady=5)
b7=Button(text="7")
b7.grid(row=4,column=1,padx=5,pady=5)
b8=Button(text="8")
b8.grid(row=4,column=2,padx=5,pady=5)
b9=Button(text="9")
b9.grid(row=4,column=3,padx=5,pady=5)
root.mainloop()