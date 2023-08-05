"""
classe and objects

student
        name
        age
        gender

"""


class Student:
    # data memebers
    name = ""
    age = 0
    gender = ""

    # methods
    def greet(self):
        print(f"name is {self.name}")
        print(f"age is {self.age}")
        print(f"gender is {self.gender}")
        print(f"city is {self.city}")

    def getdata(self):
        self.name = input("enter name = ")
        self.age = int(input("enter age = "))
        self.gender = input("enter gender = ")
        self.city = "terdal"


s1 = Student()
s2 = Student()
s3 = Student()
# s1.greet()
s1.getdata()
s1.greet()
# s1.name = "rashmi"
# s1.age = 25
# s1.gender = "female"
# s1.greet()
# s2.greet()
# (s2.gender) = "female"
# (s2.age) = 27
# (s2.name) = "biradar"
# s2.getdata()
# s2.greet()
# s3.getdata()
# s3.greet()


# print(s1.name, s1.age, s1.gender)
# print(s2.name, s2.age, s2.gender)
# print(s2.name)
