# Реалізація принципів ООП: 
# інкапсуляція (приховування даних (атрибутів, полів) екземпляоа класу), 
# наслідування
# поліморфізм (перевизначення методів класу),


#================НАСЛІДУВАННЯ===================
# defination
class Human():
    # атрибути класу:
    infoHuman="You are human!!!"
    countHuman=0
    #properties, fields, attr =>атрибути екземпляра класу в конструкторі => обєкт
    # def __init__(self,name, age):
    def __init__(self,name="Noname",age=1):
        """ Ініціалізація атрибутів екземпляру name, age"""
        # приховані атрибути => private => доступний в класі
        self.__name=name
        self.__age=age
        Human.countHuman+=1
    
    # getter, setter
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if 1<age<120:
            self.__age=age
        else:
            print("Error AGE (1;120)")

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name=name
    
    #методи класу => def
    def say_something(self,words):
        print(f"Human {self.__name} say: '{words}'")
    
    def print_info(self)->None:
        print(f"Human {self.__name} has {self.__age} yeas old")
   
    # рядкове представлення обєкта Human
    def __str__(self) -> str:
        return f'Human: {self.__name}, {self.__age} year old'



class Student(Human):
    """Клас Student"""
    def __init__(self, name, age, number_gradebook, group):
        super().__init__(name,age)
        # Human.__init__(name, age)
        self.__number_gradebook=number_gradebook
        self.__group=group

    def get_number_gradebook(self):
        return self.__number_gradebook
    
    def set_number_gradebook(self,number_gradebook):
        self.__number_gradebook=number_gradebook
    
    def get_group(self):
        return self.__group
    
    def set_group(self,group):
        self.__group=group

    def print_info(self)->None:
        # print(f"Human {super().get_name()} has {super().get_age()} yeas old")
        super().print_info()
        print(f"Group: {self.__group}. GradeBook # {self.__number_gradebook}")
    
    def __str__(self) -> str:
        return super().__str__()+f" (Group: {self.__group}. GradeBook #{self.__number_gradebook})"

# ===============using class===============
# human1=Human()
# human2=Human("Olga")
# human2=Human("Olga",18)

student1=Student("Роман",18,"123/23-01","ЦТ-21")
student2=Student("Аліна",18,"123/23-02","ЦТ-21")
student3=Student("Дмитро",19,"123/23-03","ЦТ-11(3р.н.)")
# student1.__name="gggg"
# print(student1.get_name())
# print(student1.name)
student1.print_info()
print(student1)
print(student2)
print(student3)