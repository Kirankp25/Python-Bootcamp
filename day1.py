#perform arithematic operators

# a=10
# b=20


# print("addition=      ",a+b)
# print("substraction=  ",a-b)
# print("division=      ",a/b) #for integer value use "//"
# print("division=      ",a//b) #for integer value use "//"kiran

# print("multiplication=",a*b)
# print("modulus=       ",a%b)

#############################################################################
#input from user

# name=input("enter your same")
# age=eval(input("enter your age")) #eval can take any type of input from user dynamically
# if age>18:
#     print("age is max")
#############################################################################
#relational operators

# > , <, ==, <=, >=. !=
# wap to for multiples 3==fizz
#5==buzz

# while(0):
#     print("kiran")


# if two dice are thrown the what will happen
# import random
# d1=random.randint(1,6)
# d2=random.randint(1,6)
# print("d1:",d1)
# print("d2:",d2)
# if(d1!=d2):
#     print("score:",d1+d2)
# else:
#     print("score:",2*d1)

#########################################################################
#  condition 1)if male and age 25-30 height >160cm
# condition 2) if female age 20-25 height >155cm

# cadidate_gender= input("gender(M/F):")
# cadidate_age= eval(input("age:"))
# cadidate_height= eval(input("height:"))

# if(cadidate_gender == "M"):
#     if(cadidate_age>=25 and cadidate_age<=30 and cadidate_height>160):
#         print("Male is recruited")
#     else:
#         print("Not recruite")
# else:
#     if(cadidate_age>=20 and cadidate_age<=25 and cadidate_height>155):
#         print("Female is recruited")
#     else:
#         print("Not Recruite")
# print("Recruitement completed Go home")

#############################################################################
#take random element from list

# import random
# list=["cpp","java",'python',"sql","c","html","css"]
# print(list)
# print(random.choice(list))

###############################################################################
 #function used to display real clock time using "ctime()"
#Mon Nov 21 12:07:22 2022


# basics of time module in python

# import time
# print(time.ctime())
# print(time.time())

# n=float(input("Total hr of session:"))
# print(n)
# exp=time.time()+(n*3600)
# print("end time is:",time.ctime(exp))

#####################################################################################

# math module

# import math
# a=5.4
# print(round(a)) #round figure
# print(math.ceil(a)) #max value
# print(math.floor(a)) #min value

#switch is not present in python

##########################################################################################
# Kalpath problem
# upto 2hr - 35rs
# upto 4hr - 50rs
# upto 12hr -100rs
# print 
# current time
# expiry time
# total prize

# import time
# hr=eval(input("Enter required time:"))
# print(hr)
# print("current time is: ",time.ctime())
# exp=time.time()+(hr*3600)
# print("end time is:     ",time.ctime(exp))
# if(hr<=2):
#     print("charges:  35/-")
# elif(hr<=4):
#     print("charges:  50/-")
# else:
#     print("charges:  100/-")

######################################################################################################

#looping statement in python

# for i in range(0,6):
#     print(i)

#while loop if end is not confirmed the use it
# i=0
# sum=0
# while i>=0:
#     sum=+i
#     i=int(input("ener number press -1 to exit"))
# print("sum is :",sum)
#############################################################################################

#ARMSTRONG NUMBERS
# n=int(input("enter element:"))
# tm=n
# sum=0
# while(n):
#     i=n%10             #it gives reminder of given number
#     sum+=(i*i*i)
#     n//=10            #"//" it gives integer value

# if(sum==tm):
#     print("armstrong number")
# else:
#     print("not armstrong number")

#################################################################################################

#take password from user for 3 attempts

# password="kiran"
# print("defualt password",password)
# i=0
# while (i<3):
    
#     n=input("enter password:")
#     if(password==n):
#         print("you log in successfully")
#         break
#     else:
#         print("Invalid password")
        
#         i+=1
# if(i>=3):
#     print("account is locked")

#######################################################################################
#output of your code
i=1
while 1<=10:
    print(i)
    if i==5:
        continue
    i+=1



