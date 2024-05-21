# реалізація класу для додавання числа до екземпляра клау
class Adder:
    def __init__(self,number):
        self.number=number

    def __str__(self):
        return f"Значення поля number={self.number}"
    # added number (int) to obj (Adder) 
    def __add__(self,x):
        number=self.number+x
        return Adder(number)

    def __radd__(self,x):
        number=x+self.number
        return Adder(number)

a=Adder(20)
print(a)
b=a+5
print(b)
c=10+a
print(c)
# print(a+b)
