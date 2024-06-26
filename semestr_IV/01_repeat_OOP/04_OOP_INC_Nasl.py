import random
# Інкапсуляція
class User:
    def __init__(self,login,email,age=18):
        self.__login=login
        self.__email=email
        self.age=age

    def __del__(self):
        print(f"Del {self}")
    #relisation incapsulation with properties
    #властивість getter
    @property
    def login(self):
        return self.__login

    #властивість setter
    @login.setter
    def login(self,login):
        self.__login=login

    @property
    def email(self):
        return self.__email

    #властивість setter
    @email.setter
    def email(self,email):
        if "@" in email:
            if email.split("@")[-1] in ["ukr.net","gmail.com","rshu.edu.ua"]:
                self.__email=email
            else:
                print("Not using email-client")
        else:
            print("Incorrect email")

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if age>=14 and age<=110:
            self.__age=age
        else:
            self.__age=18

    def __str__(self): #for druo function print()
        return f" Info user:{self.login}, {self.email}, {self.age} years"
    
    def __repr__(self): # convert type OBJECT =>TO str()
        return f"User({self.login},{self.email},{self.age})"
    
    def info(self):
        print(f"Unsing method 'info':{self.login}, {self.email}, {self.age} years")

class Admin(User):
    privileges=["дозволено додавати повідомлення",
                        "дозволено видаляти користувачів", 
                        "дозволено банити користувачів"]
class Employee:
    def __init__(self,company="SoftServe"):
        self.company=company

class Manager(User,Employee):
    def __init__(self,login, email, age,company="SoftServe"):
        User.__init__(self,login, email, age)
        # super().__init__(login, email, age)
        Employee.__init__(self,company)
        self.__privileges=random.choice(list(Privilege.privileges))  
    
    def info(self):
        super().info()
        print(f"{self}\n privileges: {self.__privileges}. {self.company}")

class Privilege:
    privileges=["дозволено додавати повідомлення",
                "дозволено видаляти користувачів", 
                "дозволено банити користувачів"]

# ========================================================================
chornozhukov=User("chornozhukov","chornozhukov@rshu.edu.ua",10)
chornozhukov.info()
students=list(["Doronin","Chernova"])
print(students)
print(chornozhukov)
chernova=User("chernova","chernova@rshu.edu.ua",18)
print(chornozhukov.login)
print(chernova.login)
chernova.login="chernova_2024"
print(chornozhukov.login)
print(chernova.login)
chornozhukov.email="hornozhukov#rshu.edu.ua"
chornozhukov.age=112

admin1=Admin("Dantes","dantes@gmail.com",21)
print(admin1.login)
print(admin1.age)
print(admin1.email)
print(admin1.privileges)
# del admin1
manager1=Manager("diana","daiana@gmail.com",18)
print(manager1)
manager2=Manager("oksana","okasana@gmail.com",18)
print(manager2)
manager2.info()
user_anonym=str(chornozhukov) #using repr
print("Using repr for init object user_amomym: ",user_anonym)
manager1.info()
# manager1._Manager__info()
print("List base class: ",Manager.__base__)
print("List multiply nasliduvannya: ",Manager.__mro__)
print("Name clas: ",Manager.__name__)
print("Name clas: ",Manager.__qualname__)


