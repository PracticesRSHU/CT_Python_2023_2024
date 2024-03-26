''' x=int(input("input number1  (int):")) y=int(input("input number2
(int):"))
# 4+12=16
print(x,'+',y,'=',x+y)

x=input("input number1  (int):")
y=input("input number2 (int):")
# 4+12=16

print(x,'+\'',y,'=',int(x)+int(y))
print('poema\t"Katerina" \nNew row\nSingle\a')
x=4
y=-6.256
z=4558745
result=f'{x:b}+{y:*^10.2f}={x+y:.1f}'
print(result)
print(f'{z:_d}')
print('{}+{}={}'.format(x,y,x+y))
print('{0}+{1}={2}'.format(x,y,x+y))
print('{1}+{0}={2}'.format(x,y,x+y))
print('rezult suma {0} and {1}=> {0}+{1}={2}'.format(x,y,x+y))
print("%d+(%+f)=%.1f"%(x,y,x+y))
d=0.1234
print(f'{d:.2%}')
'''
#if elif else,  match = > switch
#operations: <,>,>=,<=,!= ;  operators: not,and, or, in
#x Є [2; 7]U[8,12)
# float  NaN
"""
if condition:
    statements1 (expression1)
else:
    statements2(expression2)

Тернарний оператор
expression1 if condition else expression2
   True                         False


"""
energy=17
value_energy=True if energy>0 else False
print(f"Am I energy? = > {value_energy}")
"""
Знайти максимальне серед двох int чисел
"""
"""
number1=int(input("Input n1="))
number2=int(input("Input n2="))
if number1>number2:
    print(f'max={number1}')
    max=number1
    print(f'{max}**2={max**2}')
else:
    print(f'max={number2}!')
    print(f'{number2}**3={(number2**3)}')
"""
"""
90-100 => A
82-89 => B
74-81 => C
64-73 =>D
60-63 => E
35-59 => FX
0-34 =>F
=>error score
Вхідні дані:
91
Вихідні дані:
відмінно "A"
"""
score=input("Введіть кількість балів:")
"""
if score.isdigit():
    score=int(score)
    if score>=90 and score<=100:
        print("відмінно - A")
    else:
        if score>=82 and score<=89:
            print("добре - B")
        else:
            if score>=74 and score<=81:
                print("добре - C")
            else:
                if score>=64 and score<=73:
                    print("задовільно - D")
                else:
                    if score>=60 and score<=63:
                        print("задовільно - E")
                    else:
                        if score>=35 and score<=59:
                            print("незадовільно - FX")
                        else:
                            if score>=0 and score<=34:
                                print("незадовільно - F => ідете на повторний курс")
                            else:
                                print("Score => ERROR!!!")
else:
    print("Score is not number int!!!!")
                

"""
if score.isdigit():
    score=int(score)
    if score>=90 and score<=100:
        print("відмінно - A")
    elif score>=82 and score<=89:
        print("добре - B")
    elif score>=74 and score<=81:
        print("добре - C")
    elif score>=64 and score<=73:
        print("задовільно - D")
    elif score>=60 and score<=63:
        print("задовільно - E")
    elif score>=35 and score<=59:
        print("незадовільно - FX")
    elif score>=0 and score<=34:
        print("незадовільно - F => ідете на повторний курс")
    else:
        print("Score => ERROR!!!")
else:
    print("Score is not number int!!!!")

print("other commands")
if str(score).isdigit():
    score=int(score)
    if score>=90 and score<=100:
        print("відмінно - A")
    elif score>=82:
        print("добре - B")
    elif score>=74:
        print("добре - C")
    elif score>=64:
        print("задовільно - D")
    elif score>=60:
        print("задовільно - E")
    elif score>=35:
        print("незадовільно - FX")
    elif score>=0:
        print("незадовільно - F => ідете на повторний курс")
    else:
        print("Score => ERROR!!!")
else:
    print("Score is not number int!!!!")


"""
switch

match term:
    case pattern-1:
        action-1
    case pattern-2:
        action-2
        ...
    case pattern-n:
        action-n
    case _:
        defaultaction
"""
"""
lang=input("input program lang:")

match lang:
    case "Python":
        print("Python using...")
    case "JavaScript":
        print("JavaScript using...")
    case "Java":
        print("Java using")
    case "C#":
        print("C# using")
    case _:
        print("nothing....")
"""