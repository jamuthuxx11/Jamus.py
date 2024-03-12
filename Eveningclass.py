#single line comment
"""
multiline comments
multiline comments
multiline comments
multiline comments
"""
#variables and the different data types
student_name= "Jamu" #string
student_age=19 #integer
student_height=6.4 #float
is_male=True #boolean

print("My students name is:",student_name)
print("My students age is:",student_age)
print(student_height)
#print(student_name,student_age,student_height)

firstname="name of the student"
secondname=150
fullname=firstname+" "+str(secondname)
print(fullname)


price1="300"
price2=700
total=int(price1)+price2
print(total)
#total=float(price1)+float(price2)
#print(total)

#operators
#arithmetic operators
# + - / % ** //
print(2%5)

#checking if a number is odd or even
y=20
#print(y%10)
if y%2==0:
    print("even")
else:
    print("odd")

#Assignment operators
z=6
z+=4 #z=z+4
z%=5
print(z)

#COMPARISON OPERATORS
print(5!=2)
print(5==2)
print(6>7)
print(7<9)

#LOGICAL OPERATORS
# AND , OR
age=32
nationality="Nigerian"
if nationality=="Nigerian" and age==40
    print("you can be MANAGER")
else:
    print("you can't be MANAGER")
