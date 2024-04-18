from turtle import *
class Figure:
    """ Клас Фігура """
    def __init__(self, x, y, color):
        """ Конструктор
        :param x: координата x положення фігури
        :param y: координата y положення фігури
        :param color: колір фігури
        """
        self._x = x # _x - координата x
        self._y = y # _y - координата y
        self._visible = False # _visible - чи є фігура
        # видимою на екрані
        self._color = color # _color - колір фігури

    def _draw(self, color):
        """ Допоміжний метод, що зображує фігуру
        Тут здійснюється лише декларація методу, а конкретна
        реалізація буде здійснюватися у конкретних нащадках
        :param color: колір
        """
        pass

    def show(self):
        """ Зображує фігуру на екрані """
        if not self._visible:
            self._visible = True
            self._draw(self._color)
   
    def hide(self):
        """ Ховає фігуру (робить її невидимою на екрані) """
        if self._visible:
            self._visible = False
            # щоб сховати фігуру, потрібно
            # зобразити її кольором фону.
            self._draw(bgcolor())
   
    def move(self, dx, dy):
        """ Переміщує об'єкт
        :param dx: зміщення у пікселях по осі X
        :param dy: зміщення у пікселях по осі Y
        """
        isVisible = self._visible
        if isVisible:
            self.hide()
            self._x += dx
            self._y += dy
        if isVisible:
            self.show()

class Circle (Figure):
    """ Клас Коло """
    def __init__(self, x, y, r, color):
        """ Конструктор
        Ініціалізує положення кола, його радіус і колір
        :param x: координата x центру кола
        :param y: координата y центру кола
        :param r: радіус кола
        :param color: колір кола
        """
        # Обов’язковий виклик конструктора базового класу
        super().__init__(x, y, color)
        self._r = r # _r - радіус кола
        
    def _draw(self, color):
        """ Допоміжний метод, що зображує коло заданим кольором
        :param color: колір
        """
        pencolor(color)
        up()
        # малює починаючи знизу кола
        setpos(self._x, self._y - self._r)
        down()
        circle(self._r)
        up()
        

class Quadrate(Figure):
    """ Клас Квадрат """
    def __init__(self, x, y, a, color):
        """ Конструктор
        Ініціалізує положення лівого нижнього кута квадрата,
        довжину його сторони і колір.
        :param x: координата x лівого нижнього кута квадрата
        :param y: координата y лівого нижнього кута квадрата
        :param a: довжина сторони квадрата
        :param color: колір квадрата
        """
        # Обов’язковий виклик конструктора базового класу
        super().__init__(x, y, color)
        self._a = a # _a - довжина сторони квадрата

    def _draw(self, color):
        """ Допоміжний метод, що зображує квадрат
        :param color: колір
        """
        pencolor(color)
        up()
        # встановлюємо позицію лівого нижнього кута квадрата
        setpos(self._x, self._y)
        setheading(0)
        down()
        forward(self._a) # перша сторона квадрата,
        left(90)
        forward(self._a) # друга сторона квадрата
        left(90)
        forward(self._a) # третя сторона квадрата
        left(90)
        forward(self._a) # четверта сторона квадрата
        up()

# Перевірка роботи класу Circle 
if __name__ == '__main__':
    home()
    delay(10)
    c = Circle(120, 120, 50, "green")
    c.show()
    c.move(-30, -140)
    c.hide()
    # mainloop()
    
    home()
    delay(30)
    q = Quadrate(0, 0, 150, "blue")
    q.show()
    q.move(0, 140)
    q.hide()
    mainloop()
