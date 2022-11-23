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
d2={"kiran":91}
print("1.lookup")
print("2.add")
print("3.edit")
print("4.delete")
print("5.print")
print("6.quite")
pk=int(input("enter your choice:"))
if(pk==1):
    print("Look up a telephone number:",values(d2))
if(pk==2):
    name=input("enter the name:")
    num=input("extension:")
    d2[name]=num
    print(d2)
if(pk==3):
    kp=input("enter your key:")
    city=input("enter your city:")
    d2[city]=kp
    print(d2)
if(pk==4):
    city=input("eneter your city:")
    del d2[city]
    print(d2)
if(pk==5):
    print(d2)


    
   


