def find_value(f, x):
    print("x=", x, "->f(x)", f(x))


def my_func(x):
    print("worked my_func")
    return 1 / (1 + x ** 2)

def my_func1(x):
    print("worked my_func1")
    return 1 / (1 + x ** 3)


#використанні внутрішньої функції

def suma_number_flag(flag=True,*nums):
    """
    Повертає суму парних чисел, якщо flag=True;
    повертає суму непарних чисел, якщо flag=False;
    """
    print(flag,nums)
    suma_num=0
    #обчислення суми парних чисел
    def suma_even():
        s=0
        for item in nums:
            if item%2==0:
                s+=item
        return s

    def suma_odd():
        s=0
        for item in nums:
            if item%2==1:
                s+=item
        return s
    
    if flag==True:
        return suma_even()
    else:
        return suma_odd()
    


#функція як результат функції
def suma_number_flag_1(flag=True):
    """
    Повертає суму парних чисел, якщо flag=True;
    повертає суму непарних чисел, якщо flag=False;
    """
   # print(flag,nums)
    #suma_num=0
    #обчислення суми парних чисел
    def suma_even(*nums):
        s=0
        for item in nums:
            if item%2==0:
                s+=item
        return s

    def suma_odd(*nums):
        s=0
        for item in nums:
            if item%2==1:
                s+=item
        return s
    
    if flag==True:
        return suma_even
    else:
        return suma_odd
    



#функція як результат функції
def suma_number_flag_2(flag=True,*nums):
    """
    Повертає суму парних чисел, якщо flag=True;
    повертає суму непарних чисел, якщо flag=False;
    """
   # print(flag,nums)
    #suma_num=0
    #обчислення суми парних чисел
    def suma_even():
        s=0
        for item in nums:
            if item%2==0:
                s+=item
        return s

    def suma_odd():
        s=0
        for item in nums:
            if item%2==1:
                s+=item
        return s
    
    if flag==True:
        return suma_even
    else:
        return suma_odd
    

if __name__=="__main__":
    print(__name__)  
    find_value(my_func,2)
    find_value(my_func1,2)

    print("Сума парних чисел:=",suma_number_flag(True,*[1,2,3,4,5,6,7,8,9]))
    print("Сума непарних чисел:=",suma_number_flag(False,*[1,2,3,4,5,6,7,8,9]))

    print("Сума парних чисел:=",suma_number_flag_1(True)(*[1,2,3,4,5,6,7,8,9]))
    print("Сума непарних чисел:=",suma_number_flag_1(False)(*[1,2,3,4,5,6,7,8,9]))

    print("Сума парних чисел:=",suma_number_flag_2(True,*[1,2,3,4,5,6,7,8,9])())
    print("Сума непарних чисел:=",suma_number_flag_2(False,*[1,2,3,4,5,6,7,8,9])())