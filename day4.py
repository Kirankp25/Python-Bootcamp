# def test(d):
    
#     temp=[]
#     for i in range(0,len(d)):
#         temp.append(int(input("enter temp:")))
#     print(d)
#     print(temp)
#     maximum=max(temp)
#     i=temp.index(maximum)
#     day=d[i]
#     return day,maximum



# days=["mon","tue","wedn","thus","fri","sat","sun"]
# print(test(days))
# #####################################################
#normal day=100
#
# def pay():
#     hr=[]
#     total=0
#     rate=int(input("rate:"))
#     for i in range(0,7):
#         hr.append(int(input("enter per day work:")))
#         if i<=4:
#             total=total+hr[i]*'r'
#         elif i==5:
#             total=total+hr[i]*'r'/2
#         else:
#             total=total+hr[i]*'r'*2
#     print("name:",n)
#     print("total hour worked:",sum(hr))
#     print("pay:",total)
    

# name=input("enter employee name:")
# pay(name)
##############################################################################

###user define module
# import addTest
# a=10
# b=100
# print(addTest.add(a,b))
# addTest.sub()
##################################################################
    # PYTHON FEATURES
# overloading-same name different parameter
# overriding-same name same parameter
#"this" keyword use to point out particular variable

#class
# class student:
#     total_fees=0
#     def getdata(self):
#         #print("method")
#         self.roll_no=int(input("roll number:"))
#         self.name=input("name:")
#     def putdata(self,fees):
#         print("Name:",self.name)
#         print("roll no:",self.roll_no)
#         student.total_fees=student.total_fees+fees
#     def display(self):
#         print("total fees:",student.total_fees)


# #main
# s=student()
# s.getdata()
# f=int(input("fees:"))
# s.putdata(f)
# s1=student()
# s1.getdata()
# f=int(input("fees:"))
# s1.putdata(f)
# s.display()
################################################################

# class student:
    
#     def student_info(self):
#         marks=[]
#         t=0
#         self.name=input("name:")
#         self.roll_no=input("roll no:")
    
#         for i in range(0,6):
#             marks.append(int(input("marks:")))
#             addTest.add(t,marks[i])
#     def display(self,sub):
#         print("student name:",self.name)
#         print("average marks",self.t/'sub')

# s=student()
# s.student_info()
# mr=int(input("enter no of subject:"))
# s.display(mr)
#TO TAKE AVERAGE OF ALL SUBJECT OF A STUDENT OR WHOLE CLASS
# class student:
#     eng_t=0
#     math_t=0
#     sci_t=0
#     def getdata(self):
#         self.name=input("name:")
#         self.eng=int(input("marks:"))
#         self.math=int(input("marks:"))
#         self.sci=int(input("marks:"))
#         student.eng_t=student.eng_t+self.eng
#         student.eng_t=student.eng_t+self.math
#         student.eng_t=student.eng_t+self.sci
#      def putdata(self):
#         avg=(self.Eng+self.Math+self.Sci)/3
#         print("name:",self.name)
#         print("marks:",avg)

# s=student()
# s.getdata()
# s.putdata()
#########################################################
   