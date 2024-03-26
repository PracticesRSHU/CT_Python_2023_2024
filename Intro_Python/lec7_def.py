text="We are learning function in Python"
len_text=len(text)
result_print=print(f'len_text={len_text}')

print(result_print)

"""
#procedure
def name_func(param1, param2,...paramN):
    statements

#function
def name_func(param1, param2,..., paramN):
    statements
    return Anything

 # call function
name_func(arg1,arg2, ..., argN)

arg1,    arg2, ..., argN  
param1, param2,...,paramN

"""
#Оголошення (декларування) без параметрів і без повернення результату
def my_print():
    print("Давай познайомимся))")
    userName=input("Як тебе звати?\n")
    print(f'Привіт, {userName}. Раді знайомству:)')

# my_print()
# my_print()
# my_print()


#Оголошення (декларування) без параметрів із поверненням результату
def get_name():
    print("Давай познайомимся))")
    userName=input("Як тебе звати?\n") #userName =>локальна змінна, що видима лише в межах функції
    return userName

#Оголошення (декларування) з параметом без повернення результату, а з виконанням маніпуляцій з параметром
def hello(user):
    print(f'Привіт, {user}. Раді знайомству:)')
    user="Eva"
    global userName  # перевизначення області видимості функції з local => global
    userName="Eva"


# print(type(get_name))

userName=get_name()  #глобальна (global) змінна, що доступна в межах  всіє програми, виклик функції без аргументів
hello(userName) #Tetiana
print(userName) #Eva

privitannya=hello #присвоєння другого імені функції

privitannya(userName) #Eva

def task1():
    pass
