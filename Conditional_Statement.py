# IF ElIF and ELIF . Condition wise statement
Name=input("Enter your Name:")
Class=eval(input("Enter Your Class:"))
age=int(input("Enter Your Age: "))

if age>60:
    print("You belongs to Old citizen category" +Name)

elif 20<age<59:
    print(Name+" " "You belong to mid age Category")

else:
    print(Name+ " " "YOu belong to child group")









a=(input("Enter the Name:"))
b=int(input("Enter Student ID:"))
c=int(input("enter marks in Problem Solving and Programming:"))
d=int(input("Enter Marks in Networking:"))
e=int(input("Enter marks in Operating System:"))
f=int(input("Enter marks in information security"))
total_Marks = (c+d+e+f)
percentage=(total_Marks/400*100)
if 80<=percentage <=100:
    print(a+" ""COngratulations You've scored A+")

elif 60<= percentage<=80:
    print(a+ " ""welldone You've scored B+")

elif 40<= percentage <=60:
    print(a+" ""Good You've scored C+ ")

else:
    print("SOrry You're failed")







