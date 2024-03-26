# Реалізація принципів ООП: 
# інкапсуляція (приховування даних (атрибутів, полів) екземпляоа класу), 
# наслідування
# поліморфізм (перевизначення методів класу),


#================Інкапсуляція===================
class Human:
    # атрибути класу:
    infoHuman="You are human!!!"
    countHuman=0
    #properties, fields, attr =>атрибути екземпляра класу в конструкторі => обєкт
    # def __init__(self,name, age):
    def __init__(self,name="Noname"):
        """ Ініціалізація атрибутів екземпляру name, age"""
        # доступний => public  => доступний за межами класу
        self.name=name
        # приховани => private => доступний в класі
        self.__age=1
        Human.countHuman+=1
    
    # getter, setter
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if 1<age<120:
            self.__age=age
        else:
            print("Error AGE (1;120)")

    #методи класу => def
    def say_something(self,words):
        print(f"Human {self.name} say: '{words}'")
    
    def print_info(self):
        print(f"Human {self.name} has {self.__age} yeas old")
   
    # рядкове представлення обєкта
    def __str__(self) -> str:
        return f'Human: {self.name}, {self.__age} year old'


human1=Human("Olga")
human1.set_age(-3)
human1.set_age(21)
human1.say_something("Hello! How are you?")
human1.print_info()
print("Human1",human1.get_age(),"yeas old")
# human1.surname="Gala" #новий атрибут екземпляра, який створюється динамічно
# print(human1.surname)
# print(human1.__age) #error
# print(human1.infoHuman)
# print(Human.infoHuman)

print("human obj=>",human1) # без  визначення __str__() => <__main__.Human object at 0x000002472B663680>

human2=Human(name="Dmitro")
human2.print_info()
# human2.name="Dmitro"
# human2.age=21
human2.print_info()
human2.say_something("Hi! I am fine, thanks")
# print(human2.name)
# print(human2.infoHuman)
# print(Human.infoHuman)


print(f"Created object Human: {Human.countHuman}")
listHuman=[human1, human2]
print("Working list of humans:")
for human in listHuman:
    print(human)
