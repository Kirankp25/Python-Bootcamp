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

name=input("enter your name:")
for i in range(0,len(name)):
    if name[i]=="e" or name[i]=="E":
        print(i+1)
        break





