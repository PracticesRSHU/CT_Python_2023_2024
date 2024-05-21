from abc import ABCMeta, abstractmethod


class Pet(metaclass=ABCMeta):
    """ Абстрактний клас Домашня тварина """
    def __init__(self, name) -> None:
        self.name = name # ім'я домашньої тварини
        self.isHealthy = True # чи здорова тварина
        self.isHungry = False # чи голодна тварина
        self.isHappy = True # чи щаслива тварина

    @abstractmethod
    def accept(self, visitor):
        """ Абстрактний метод, що використовується для реалізації
        шаблону проектування Відвідувач
        :param visitor: відмідувач
        """
        pass
    
    def __str__(self):
        return ("Name: " + self.name + ";\nHappy = " + str(self.isHappy) +
        ";\nHungry = " + str(self.isHungry) +
        ";\nHealthy = " + str(self.isHealthy))
    
    def treat(self):
        """ Лікувати тварину """
        self.isHealthy = True
    def hurt(self):
        """ Ображати тварину """
        self.isHealthy = False
        self.isHappy = False

class Cat(Pet):
    """ Клас Кіт """
    def __str__(self):
        return "== Cat ==\n" + super().__str__()
    
    def accept(self, visitor):
        visitor.visitCat(self)

    def feed(self):
        """ Годувати кота """
        self.isHungry = False
    def play(self):
        """ Пограти з котом """
        self.isHappy = True
        self.isHungry = True

class Dog(Pet):
    """ Клас Собака """
    def __init__(self, name) -> None:
        super().__init__(name)
        self.skills = 0
        
    def __str__(self):
        return ("== Dog ==\n" + super().__str__() +
                ";\nSkills = " + str(self.skills))
    
    def accept(self, visitor):
        visitor.visitDog(self)
    
    def getBone(self):
        """ Отримати кістку """
        self.isHungry = False
    def walk(self):
        """ Вигуляти собаку """
        self.isHappy = True
        self.isHungry = True
    def training(self):
        """ Тренувати собаку """
        self.skills += 10
        self.isHappy = False



#=====================================================================================
class Visitor(metaclass=ABCMeta):
    """ Базовий клас Відвідувач """
    
    @abstractmethod
    def visitCat(self, pet):
        """ Абстрактний метод відвідати Кота """
        pass

    @abstractmethod
    def visitDog(self, pet):
        """ Абстрактний метод відвідати Собаку """
        pass

class Veterinarian(Visitor):
    """ Клас лікар - вміє лікувати людей """
    def visitDog(self, pet):
        pet.treat()

    def visitCat(self, pet):
        pet.treat()
        
    def __str__(self):
        return "Visitor = Veterinarian"
    
class Scoundrel(Visitor):
    """ Клас Негідник - ображає тварин """
    def visitDog(self, pet):
        pet.hurt()

    def visitCat(self, pet):
        pet.hurt()

    def __str__(self):
        return "Visitor = Scoundrel"

class DogTrainer(Visitor):
    """ Клас Дресирувальник домашніх тварин """
    def visitDog(self, pet):
        pet.training()
        
    def visitCat(self, pet):
        print("I can train only dogs")

    def __str__(self):
        return "Visitor = DogTrainer"

class Master(Visitor):
    """ Клас Господар - вміє годувати тварину """
    # def visit(self, pet):
    #     if isinstance(pet, Cat):
    #         pet.feed()
    #     elif isinstance(pet, Dog):
    #         pet.getBone()
            
  
    def visitCat(self, pet):
        pet.feed()
    
    def visitDog(self, pet):
        pet.getBone()
    
    def __str__(self):
        return "Visitor = Master"

class Child(Visitor):
    """ Клас Дитина - вміє розважати тварин """
    # def visit(self, pet):
    #     if isinstance(pet, Cat):
    #         pet.play()
    #     elif isinstance(pet, Dog):
    #         pet.walk()
            
    def visitCat(self, pet):
        pet.play()
    
    def visitDog(self, pet):
        pet.walk()

    def __str__(self):
        return "Visitor = Child"

#========================================================================
dog = Dog("Rex")
cat = Cat("Kuzya")
visitors = [DogTrainer(), Master(), Child()]
for visitor in visitors:
    print(visitor)
    cat.accept(visitor)
    print(cat)
    print()
    
for visitor in visitors:
    print(visitor)
    dog.accept(visitor)
    print(dog)