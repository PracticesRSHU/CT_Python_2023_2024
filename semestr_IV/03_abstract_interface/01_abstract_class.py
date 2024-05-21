from abc import ABCMeta, abstractmethod
class Pet(metaclass = ABCMeta):
    def __init__(self, name):
        """ Конструктор
        :param name: Кличка тварини
        """
        self._name = name # приватне поле - кличка тварини
    
    @abstractmethod
    def voice(self): # абстрактний метод
        pass # порожня реалізація


class Cat(Pet):
    def __init__(self, name):
        """ Конструктор
        :param name: Кличка тварини
        """
        self._name = name # приватне поле - кличка тварини
    
    def voice(self): # 
        print("may")
   
    def __voice(self): # 
        print("may")
      
class Dog(Pet):
    def __init__(self, name):
        """ Конструктор
        :param name: Кличка тварини
        """
        self._name = name # приватне поле - кличка тварини
    
    def voice(self): # 
        print("Gav-gav")
   
    def __voice(self): # 
        print("may")
   
# pet= Pet("Rokky")
cat=Cat("Tom")
cat.voice()
