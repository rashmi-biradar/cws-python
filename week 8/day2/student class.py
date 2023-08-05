# class Student:
#     # data memebers
#     name = ""
#     age = 0
#     gender = ""

#     # methods
#     def greet(self):
#         print(f"name is {self.name}")
#         print(f"age is {self.age}")
#         print(f"gender is {self.gender}")

#     def getdata(self, n, a, g):
#         self.name = n
#         self.age = a
#         self.gender = g


# s1 = Student()
# s2 = Student()
# s3 = Student()
# # s1.greet()
# name = "rash"
# age = 45
# gender = "female"
# # s1.getdata("rashmi", 25, "female")
# s1.getdata(name, age, gender)
# s1.greet()
class Student:
    def __init__(self, n, a, g, c):
        # self.name = input("enter name = ")
        # self.age = int(input("enter age = "))
        # self.gender = input("enter gender = ")
        # self.city = "terdal"
        self.name = n
        self.age = a
        self.gender = g
        self.city = c

    def greet(self):
        print(f"name is {self.name}")
        print(f"age is {self.age}")
        print(f"gender is {self.gender}")
        print(f"city is {self.city}")


s1 = Student("rashmi", 45, "female", "terdal")
# s2 = Student("rashmi", 45, "female", "terdal")
# s3 = Student("rashmi", 45, "female", "terdal")
# s2 = Student()
# s3 = Student()
s1.greet()
print("--------------")
# s2.greet()
# print("--------------")
# s3.greet()
class Rectangle:
    def __init__(self):
        self.length = int(input("enter the length of the rectangle = "))
        self.width = int(input("enter the width of the rectangle = "))

    def length(self):
        self.area = self.length

    def width(self):
        self.area = self.width

    def area(self):
        newarea = self.length() * self.width()
        return newarea


obj = Rectangle()
obj.length()
obj.width()
x = obj.area()
print(x)

