#break statement used to stop the loop
#continue used to skip the statement

#while statement is used to endless condition of given situation
#for loop used when we know the end of given condition

# for i in range(10,0,-1):
#     print(i,end=" ")       # end=" " is used to print in horizontal line of given output
# name="kiran"
# print(name)
# for k in range(0,5):
#     print(name[k],end=" ")

# for k in name:
#     print(k)

############################################kiran###################################################################3

# ASCII VALUE 

# print(ord('A'))  # ord function used to find out ASCII value of given input by user

# print(chr(105))

#WAP TO CONVERT STIRNG TO LOWER CASE WITHOUT USING BUILTIN FUNCTION LOWERCASE FUNCTION

# kp=(input("Enter your string:"))
# for n in kp:
#     print(chr(ord(n)+32),end=" ")
#     #kp[n]=chr(ord(n)+32)

# name=input("enter your name:")
# for n in name:
#     if ord(n)>=65 or ord(i)<=122:
#         print(chr(ord(i)+32))


# ###########################################################################################################################

# #   EXERCISE Q NO 01
# import random
# sum=0
# for i in range(0,10):
#     print(random.randint(1,10),end=" ")
#     sum+=random.randint(1,10)
# print(sum)
#  AB AS 00
####################################################################################################################
# ab=0
# ab0=0
# n=1
# while(n<=5):
#     n=n+1
#     code=input("enter your string:")
#     if code[0]=='A' and code[1]=='B':
#         ab=ab+1
#     if code[3]=='0' and code[4]=='0' :
#         ab0=ab0+1
# print(ab," ",ab0)
############################################################################################################################

# PATTERN PRINTING

# for i in range(1,10):
#     for j in range(1,i):
#         print("*",end="")
#     print()

# >>>>output

# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
###########################################################################
# for i in range(1,10):
#     for j in range(1,i):
#         print(j%2,end=" ")
#     print()

#     output
#     1
# 10
# 101
# 1010
# 10101
# 101010
# 1010101
# 10101010

#############################################################
# 1 2 3 4 17 18 19 20
#   5 6 7 14 15 16
#     8 9 12 13 
#       10 11

# for i in range(1,4):
#     for i in range(1,4):
#         for j in range(1,i):
#             print(j,end=" ")
#     for j in range(1,i):
#         print(" ",end=" ")
#     print()

# for i in range(1,4):
#     for j in range(1,j):
#         print()
    
        
####################################################################################
 # SLICING IN PYTHON
# name=input("enter name:")
# l=len(name)
# print(l)

# name=input("enter your name:")
# for i in range(0,len(name)):
#     if name[i]=="e" or name[i]=="E":
#         print(i+1)
#         break

############################################################################################
#
######## DATA STRUCTURE IN PYTHON  ######


# list[]
# dict{}
# tuple()
# list=[1,2,3,4,5,6,7,8,9]
# for i in list:
#     print(i,end=" ")

#####################################################################
#  DEFINE  A LIST CONTAINING NAMESOF STUDENT IN CLASS ASK THE USER TO 
#  INPUT EXAM RESULT OF EACH SSSTUDENT AND PRINT A DATA EACH OD DATA OF HIGHEST MARK
# n=5
# li=[]
# while n:
#     name=input("Enter a name:")
#     marks=input("Enter a marks")
#     n=n-1
#     li.append(name)
#     li.append(marks)
# n=li[2]
# for i in range(1,len(li),2):
#     if n<=li[i] :
#         continue
#     else:
#         n=li[i] 
# print(n)

# li=['Kiran', '23', 'raj', '34', 'ankit', '24', 'suyog', '34', 'rahul', '95']
# n=5
# while(n):
#     name=input("enter name:")
#     marks=input("Marks:")
#     li.append(name)
#     li.append(marks)
#     print(li)
#     n=n-1


# for i in range(0,10,2):
#     index=1
#     k=li[1]
#     if k<=li[i]:
#         continue
#     else:
#         k=li[i]
#         index=index+2
# print(k," ",li[index]," ",index)
####################################################################################
# li=[1,2,3,4,5,6,7,8,9]
# print(max(li)) #max function
# print(min(li)) 

# li=[121,3,4,2,3,4,65,7,8,64,4,2,43]
# n=input()
# mx=max(li)
# for i in range(0,len(li)):
#     jk=li[i]
#     for j in range(0,len(li)):
#         if li[j]+jk==mx:
#             print("true")
#             break

###################################################################################3
# l=int(input("length:"))

# t=input("target:")
# li=[]
# for i in range(0,l):
#     inp=input()
#     li.append(inp)
#     # print(li)
# print(li)
# print("max element:",max(li))
# for i in range(0,l):
#     k=li[i]
#     for j in range(i+1,l):
#         if (k+li[j])==t:
#             print("true")
#             break
#         else:
#             continue
###################################################################
# l=int(input("length:"))
# kp=0
# t=input("target:")
# li=[]
# for i in range(0,l):
#     inp=input()
#     li.append(inp)
#     # print(li)
# print(li)
# print("max element:",max(li))
# for i in range(0,l):
  
#     for j in range(i+1,l):
#         if(li[i]+li[j])==t:
#             kp=1 
# if kp==1:
#     print("true")
# else:
#     print("false")

##################################################
#2D list



# month=["jan","feb","march","april","may","june","july","aug","sept","oct","nov","dec"]
# aveg=[]
# li=[]

# # n=int(input("enter limit:"))
# for i in range(0,12):
#     l=[]
#     np=input("min:")
#     mp=input("max:")
    
#     l.append(month[i])
#     l.append((np+mp)/2)
#     li.append(l)
# print(li)
# #########################################################################
# 1 2 3 4 17 18 19 20
#   5 6 7 14 15 16
#     8 9 12 13 
#       10 11

    
rows = 5
i = 0
while i <= rows - 1:
    j = 0
    while j < i:
        # display space
        print('', end=' ')
        j += 1
    k = i
    while k <= rows - 1:
        print('*', end=' ')
        k += 1
    print()
    i += 1

# i = rows - 1
# while i >= 0:
#     j = 0
#     while j < i:
#         print('', end=' ')
#         j += 1
#     k = i
#     while k <= rows - 1:
#         print('*', end=' ')
#         k += 1
#     print('')
#     i -= 1
