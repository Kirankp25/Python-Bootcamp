#DICTIONARY

#d1={"pune":32,"Jalgaon":45,"satara":65}
# print(d1)
# print(d1["pune"])
# city=input("enter city:")
# temp=input("enter temp:")
# d1[city]=temp                                       #to append the value in dict
# print(d1)

# get(key) #return the associated value
# keys() #return all keys of dict
# values()#return all values of dict
# items()#return all views of dict
######################################################################################
# d2={"kiran":91}
# print("1.lookup")
# print("2.add")
# print("3.edit")
# print("4.delete")
# print("5.print")
# print("6.quite")
# pk=int(input("enter your choice:"))
# if(pk==1):
#     print("Look up a telephone number:",values(d2))
# if(pk==2):
#     name=input("enter the name:")
#     num=input("extension:")
#     d2[name]=num
#     print(d2)
# if(pk==3):
#     kp=input("enter your key:")
#     city=input("enter your city:")
#     d2[city]=kp
#     print(d2)
# if(pk==4):
#     city=input("eneter your city:")
#     del d2[city]
#     print(d2)
# if(pk==5):
#     print(d2)
##########################################################################################################3
#Lucy number

# d3={
#     1:['a','j','s'],
#     2:['b','k','t'],
#     3:['c','l','u'],
#     4:['d','m','v'],
#     5:['e','n','w'],
#     6:['f','o','x'],
#     7:['g','p','y'],
#     8:['h','q','z'],
#     9:['i','r']}
# total=0
# sum=0
# character=input("enter quility:")
# for c in character:
#     for j in d3.keys():
#         if c in d3.get(j):
#             total+=j
# if sum>9:
#     sum=total
#     total=0
#     while(sum>9):
#         sum=sum+total%10
#         total=total//10

# print(sum)
# #################################################################

####### PASSWORD GEERATOR
# import re
# code=input("input code:")
# pattern="[A-Z|a-z]*[0-9]*@"
# if(re.match(pattern,code)):
#     print("valid")
# else:
#     print("invalid")
#############################################################
# WAP TO ACCEPT PASSWORD 8-15 CHARACTER LONG
#PATTERN
# import re
# code=input("input code:")
# pattern="([A-Z]+[a-z]+[0-9]*[#|@|$]*)"
# if(re.match(pattern,code)):
#     print("valid")
# else:
#     print("invalid")
########################################################################
    ############ Password Chekar ############

# "+" AT LEAST ON TIME
# "*" WHAT YOU WANTED 1 TIME OR MORE OR ZERO TIME
# "|" OR
# " " FOR SPACE
# import re
# code=input("input code:")
# pattern="([A-Z]{2}-+[0-9]{2}-+[A-Z]{2} [0-9]+)"
# if(re.match(pattern,code)):print("valid")
# else:print("invalid")
#########################################################################

#WAP TO CHECK VALID MAIL-ID
# import re
# code=input("input code:")
# pattern="([a-z]{3,9}[0-9]{3,9}[@]{1}[a-z]{1,5}[.]+[com]+)"
# if(re.match(pattern,code)):print("valid")#match function
# else:print("invalid")

##########################################################################
###### USER DEFINE FUNCTION #######
#user define
# def fun():
#     print("Hello Friends...!")
#     x=10
#     print("x:",x)
# #main

# print("Welcome to JSPM")
# x=100
# print("x:",x)
# fun()
# print("x:",x)
# print("Thank you")
#####################################################################
# user define
#multiple value can return in python
# def deposite():               #parameter
#     global balance            #global variable
#     amt=int(input("enter amount:"))
#     print("current balance:",balance+amt)
# def withdraw():               #parameter
#     global balance            #global variable
#     wit=int(input("enter amount:"))
#     print("current balance:",balance-wit)
    
# balance=int(input("enter balance:"))
# print("1.deposite\n2.withdraw")
# ch=int(input("what you want:"))
# if ch==1:
#     deposite()                #argument
# else:
#     withdraw()
##################################################################################
#message encryption using user define function
# def encrypt(message):
#     form=""
#     for i in range(0,len(message)):
#         if((i+1)%2==0):
#             form=form+message[i]
#     for i in range(0,len(message)):
#         if((i+1)%2!=0):
#             form=form+message[i]
#     return form
# #main function
# message=input("enter a massage:")
# message=encrypt(message)
# print(message)
# #output-->
# # i/p->enter a massage:hello jo
# # o/p->el ohloj
###############################################################################
# #user define
# def fun(a,n="pune"): #default value
#     print("a:",a)
#     print("name:",n)

# #main
# a=3
# name=""
# fun(a=100,n="jalgaon")
#########################################
#VarArgs parameters
# def fun(s,*n,**t):
#     print("s",s)
#     for i in n:
#         print(i)
#     print(t['veg'])

# fun(1,2,3,4,5,veg=100,fruit=1000)
###################################################
# def t(**n):

#     for i in n:
#         print(i)
    
# t(Mon=41,Tue=45,Wedn=44,Thus=43,Fri=49,Sat=45,Sun=50)