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
