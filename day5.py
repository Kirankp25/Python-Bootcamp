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
#main
conn=sqlite3.connect("university.db")
cur=conn.cursor()
# create(cur)
#insert()
dis2()