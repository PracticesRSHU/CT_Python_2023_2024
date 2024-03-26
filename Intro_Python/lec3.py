n=int(input("input 3-digits number"))
"""
n=567   => value: 5*6*7
d1=n%10 => 567%10=> 7 =>d1=7
n=n//10 => 567//10=> 56=> n=56
d2=n%10 => 56%10 => 6  =>d2=6
d3=n//10 => 56//10=> 5=> d3=5
"""
input_n=n
d1=n%10 
n=n//10
d2=n%10
d3=n//10
print(f'Number {input_n}: multiply its digits=>{d1*d2*d3}')
print('Number {}: multiply its digits=>{}'.format(input_n,d1*d2*d3))
print('Number {number}: multiply its digits=>{dobutok}'.format(number=input_n,dobutok=d1*d2*d3))
"""
занурив щітку у фарбу
провів вгору по штахеті
провів вниз по штахеті
відступ вправо на одну штахету
я пофапбував 1 штахету
==========
занурив щітку у фарбу
провів вгору по штахеті
провів вниз по штахеті
відступ вправо на одну штахету
я пофапбував 2 штахету
==============

Том соєр циклічно виконує команди до кінця паркану
(поки є штахета в паркані)
while for
range
"""
n=int(input("Введіть кількість штахет в паркані:\n"))

step1="занурив щітку у фарбу\n"
step2="провів вгору по штахеті щіткою\n"
step3="провів вниз по штахеті щіткою\n"
step4="відступів вправо на одну штахету\n"

"""
print(step1,step2,step3,step4,step5)
step5="я пофарбував 2 штахету\n"
print(step1,step2,step3,step4,step5)
"""
"""
while condition:
    statements


while condition:
    statements
else:
    statements

"""
'''
#n=10
count=1
while count<=n:
    step5=f"я пофарбував {count} штахету\n"
    print(step1,step2,step3,step4,step5)
    count=count+1
else:
    print("Finish working!!!")
print("Other statements")
'''
'''
# using statements as continue 
#n=4
count=1
while count<=n:  #1<=4 (true), 2<=4 (true), 3<=4 (true), 4<=4(true),5<=4(false)
    step5=f"я пофарбував {count} штахету\n"
    if count==3: #1==3(false), 2==3 (false), 3==3 (true) ,4==3 (false)
        print(f"Бракована штахета #{count}. Пропускаю\n")
        count+=1  # 3-я ітерація count=4
        continue  #пропускає наступні команди і виконує наступну ітерацію циклу
    print(step1,step2,step3,step4,step5)
    count=count+1 #2, 3, 5 
else: #виконується якщо умова циклу хибна (false)
    print("Finish working!!!")
    
print("Other statements")
'''

# using statements as break 
#n=4
count=1
while count<=n:  
    step5=f"я пофарбував #{count} штахету\n"
    if count==10: 
        print(f"На штахеті #{count} я зупинюся. Я втомився!!!\n")
        break  
    print(step1,step2,step3,step4,step5)
    count=count+1 
else: 
    print("Finish working!!!")
    
print("Other statements")


#підрахувати суму перших 5 непарних цілих чисел, які вводяться з клавіатури
#56, 45, 78,...
number_event=5
count=0 #1,2,3,4
sum_number_event=0
iter=0
while count<number_event:
    iter+=1
    number=int(input("input number:\n"))
    if number%2==1:
        sum_number_event+=number # sum_number_event=sum_number_event+number
        count+=1
else:
    print("Sum=",sum_number_event)

print("Кількість ітерацій=",iter," сума непарних чисел=",sum_number_event)   

#using for
"""
range(start, end, step)
for item in sequence:
    statements
else:
    statements
"""
#n=5
n=int(input("Введіть кількість штахет в паркані:\n"))
count=1
for count in range(1,n+1):   # range(5)=>0,1,2,3,4 range(1,6) => 1,2,3,4,5
    step5=f"я пофарбував #{count} штахету\n"
    if count==10: 
        print(f"На штахеті #{count} я зупинюся. Я втомився!!!\n")
        break  
    print(step1,step2,step3,step4,step5)
else: 
    print("Finish working!!!")
    
print("Other statements")

#Порахувати суму перших 10 натуральних цілих чисел
suma=0
for i in range(1,11):
    suma+=i
print("Suma перших 10 чисел=",suma)

for symbol in "Python": # 'P','y',...
    print(symbol)

