# 1. Інкапсуляція, Поліморфізм, Наслідування
# Наслідування
"""
class Parent:
    classmethods and attrs

class Child(Parent):
    classmethods and attrs
"""
class Human:
    height=170

class Student(Human):
    exp_profession=0 #досвід в професії
    satiety=0 #ситість


class Worker(Human):
    exp_profession=100
    satiety=80

# using class
human=Human()
dmitro=Student()
dmitro1=Student()
alina=Worker()
print(dmitro.height)
print(dmitro.satiety)
print(dmitro1.height)
print(dmitro1.satiety)
print(alina.height)
print(alina.satiety)
print(human.height)


class Grandparent:
    height=170
    satiety=90
    age=60
    def __init__(self,gender="male") -> None:
        self.__gender=gender
    
    def get_gender(self):
        return self.__gender

class Parent(Grandparent):
    age=40

class Child(Parent):
    height=100
    _height=40 #protected
    __height=0 #private
    __age=0
    def __init__(self,age=1):
        self.__age=age #private
        print("Child height in init: ",self.height)
        print("Child satiety in init: ",self.satiety)
        print("Child age in init: ",self.age)
    
    def get_age(self):
        return self.__age
    
    def get_height(self):
        return self.__height
    
    def set_age(self,age):
        self.__age=age

    def set_height(self,height):
        self.__height=height

    def get_gender(self):
        return   super.get_gender()

igor=Child()
ivan=Child()
print("Child Ihor after init: ",igor.height)
print("Child Ivan after init: ",ivan.height)
print("Igor _height->",igor._height)
print("Ivan _height->",ivan._height)
igor._height=50
#igor.height=180
Child.height=180
Child._height=150
print("Child Ihor after init: ",igor.height)
print("Child Ivan after init: ",ivan.height)
print("Igor _height->",igor._height)
print("Ivan _height->",ivan._height)
# print(igor.__height)
print(igor.get_age())
print(igor.get_height())
igor.set_age(12)
igor.set_height(120)
print(igor.get_age())
print(igor.get_height())
print("Gender: ", igor.get_gender())