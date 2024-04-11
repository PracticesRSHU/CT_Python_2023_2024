# Реалізувати клас Vector3D з відповідними атрибутами 
# (координатами вектора у просторі x, y, z) 
# та перевантаженими операторами та арифметичними 
# операціями (__str_(), __add__(), __iadd__(), __mul__(), 
# __imul__(), __neg__(), __sub__(), __isub__(), __abs__(), 
# __truediv__(), __eq__(), __ne__(),  __lt__(), __gt__()
#  та інші, які реалізують всі операції над векторами
class Vector3D:
    def __init__(self,x=0,y=0,z=0):
        """
        Клас роботи з векторами
        :param x
        :param y
        :param z
        """
        self.__x=x
        self.__y=y
        self.__z=z
    
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    @property
    def z(self):
        return self.__z
    
    @x.setter  # =
    def x(self,x):
        self.__x=x

    
    @y.setter  # =
    def y(self,y):
        self.__y=y

    
    @z.setter  # =
    def z(self,z):
        self.__z=z

    def __str__(self):
        return f"({self.x},{self.y},{self.z})"
    # self+vector
    def __add__(self,vector): #Vector3D(3,4,6)+Vector3D(3,4,7)=?
        if isinstance(vector,Vector3D):
            v=Vector3D()
            v.x=self.x+vector.x
            v.y=self.y+vector.y
            v.z=self.z+vector.z
            return v
        if isinstance(vector,(int, float)):
            v=Vector3D()
            v.x=self.x+vector
            v.y=self.y+vector
            v.z=self.z+vector
            return v
        else:
            raise TypeError("Така операція не можлива")
    # imul  *=
    def __imul__(self,vector):
        if isinstance(vector,Vector3D):
            v=Vector3D()
            # правила множення векторів
            #
            v.x=self.y*vector.z-self.z*self.y
            v.y=self.x*vector.z-self.z*self.x
            v.z=self.x*vector.y-self.y*self.x
            return v
        if isinstance(vector,(int, float)):
            v=Vector3D()
            v.x=self.x*vector
            v.y=self.y*vector
            v.z=self.z*vector
            return v
        else:
            raise TypeError("Така операція не можлива")

    def __neg__(self):
        self.x=-self.x
        self.y=-self.y
        self.z=-self.z
        return self
    
a=Vector3D(2,5,8)    
b=Vector3D(1,6,2)
print(a) 

print(b)   
print(a+b) 
# print(a+3) 
# print(3+a)  #потрібно пеевантажити __radd__()
a*=6
print(a)
a*=b
print(a)
a=-a
print(a)