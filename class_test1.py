import class_test

help(class_test.Enos)


docs = class_test.Enos.__doc__()
print(docs)

name = input("Enter Name : ")
name = name.capitalize()
age = input("Enter Age : ")
gender = input("Enter Gender : ")

point = class_test.Enos(name, age, gender)
#name = point.__init__

print(point.skills())

print(point.name)
print(point.age)
print(point.gender)

location = input("Enter Year to Know Where he lived : ")
print(point.place(location))
