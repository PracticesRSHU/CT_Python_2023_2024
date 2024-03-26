class Human:
    # атрибути класу:
    infoHuman="You are human!!!"
    countHuman=0
    #properties, fields, attr =>атрибути екземпляра класу в конструкторі => обєкт
    # def __init__(self,name, age):
    def __init__(self,name="Noname", age=0):
        """ Ініціалізація атрибутів екземпляру name, age"""
        self.name=name
        self.age=age
        Human.countHuman+=1
    
    #методи класу => def
    def say_something(self,words):
        print(f"Human {self.name} say: '{words}'")
    
    def print_info(self):
        print(f"Human {self.name} has {self.age} yeas old")
    # рядкове представлення обєкта
    def __str__(self) -> str:
        return f'Human: {self.name}, {self.age} year old'


human1=Human("Olga",18)
human1.say_something("Hello! How are you?")
human1.print_info()
# print(human1.name)
# print(human1.infoHuman)
# print(Human.infoHuman)

print(human1) # без  визначення __str__() => <__main__.Human object at 0x000002472B663680>

human2=Human(name="Dmitro",age=21)
human2.print_info()
# human2.name="Dmitro"
human2.age=25
human2.print_info()
human2.say_something("Hi! I am fine, thanks")
# print(human2.name)
# print(human2.infoHuman)
# print(Human.infoHuman)


print(f"Created object Human: {Human.countHuman}")

