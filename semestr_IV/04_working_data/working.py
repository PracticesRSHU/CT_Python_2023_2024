import string
import random
from string import Formatter
from string import Template
import re
print("a" in  "JavaScript")
print("5" in  "JavaScript")
#порахувати кількість цифр в рядку
print(string.punctuation)
print(string.whitespace)
str1="Python 3.12 is released on 20/12/2023 Python"
count_number=0
count_punctuation=0
for symbol in str1:
    # if symbol.isdigit():
    # if symbol in "1234567890":
    if symbol in string.digits:
        count_number+=1
    if symbol in string.punctuation:
        count_punctuation+=1

print("count=",count_number)
print("count punctuation=",count_punctuation)


#згенерувати о=логін і пароль еористувача
userLogin="".join(random.sample(string.ascii_lowercase,6))
userPassword="".join(random.sample((string.ascii_lowercase+string.digits),8))
print("Login=",userLogin)
print("Password=",userPassword)
print(string.capwords(str1))

# using classes Formatter (format()) and Template
formatter=Formatter()
print(formatter.format('{userlogin}',userlogin=userLogin))
print(formatter.format('{} {userlogin}. Your password {password}','Welcome, ',userlogin=userLogin,password=userPassword))

template=Template('$userLogin has cool password: $userPassword')

new_str= template.substitute(userLogin='admin', userPassword="Qwerty-1")
print(new_str)
print(str1.find("Python"))
match=re.search(r"Python", str1)
print(match.group())
print(match.group(0))
match=re.search(r'\w{2}',str1) #
print(match.group())
print(match.group(0))
match=re.search(r'\d{2}',str1) #
print(match.group())

row1="My phone +38(097)3456789 and +38(097)3456799"


match1=re.search(r"\+38\(097\)(\d\d\d\d\d\d\d)",row1)



import re
userStr="abcd abc efgh"
match = re.search(r'\w{4}', userStr)
# group() — повертає підрядок, який збігся з усім шаблоном або з виразом у групі шаблону (розглянуто далі)
print(match.group()) # abcd
print(match.group(0)) # abcd


# # знайти перше входження в рядок послідовності (фрагменту) завдовжки в три символи, який складається лише з цифр.
# # Шаблон: ‘\d{3}’
userStr="abcd abc 123 efgh 456"
match = re.search(r'\d{3}', userStr)
print(match.group()) # 123


# # необхідно проаналізувати рядок на наявність у ньому номерів мобільних телефонів
# # двох операторів (відомо код оператора).
userStr="My cell phone numbers: Lifecell +38(063)1234567; Kyivstar +38(067)9875612"
match1 = re.search(r'Lifecell \+38\(063\)(\d\d\d\d\d\d\d); Kyivstar \+38\(067\)(\d\d\d\d\d\d\d)', userStr)

print(match1)   # Lifecell +38(063)1234567;
print(match1.group())   # Lifecell +38(063)1234567;
#                         # Kyivstar +38(067)9875612
print(match1.group(0))  # Lifecell +38(063)1234567;
                        # Kyivstar +38(067)9875612
print(match1.group(1)) # 1234567
print(match1.group(2)) # 9875612
print(match1.group(1,2)) # ('1234567', '9875612')
print(match1.start(), match1.end()) #23 73
print(match1.start(0), match1.end(0)) #23 73
print(match1.start(1), match1.end(1)) #40 47
print(match1.start(2), match1.end(2)) #66 73
# # метод span(), який повертає кортеж, що складається з індексу початку та індексу кінця, збігається з шаблоном фрагмента
print(match1.span()) #(23, 73)
print(match1.span(0)) #(23, 73)
print(match1.span(1)) #(40, 47)
print(match1.span(2)) #(66, 73)


# # знайти усі збіги можна використовуючи функцію re.findall(pattern, strObj).

userStr="2021-2022 Competition Calendar:30.11.2021 —  2021 Grand Prix Series; 14.01.2022 —  Grand Pemio D'Italia"
match2=re.findall(r'\d{2}\.\d{2}\.202\d{1}', userStr)
match2=re.findall(r'\d{2}\.\d{2}\.\d{4}', userStr)
print(match2) # ['30.11.2021', '14.01.2022']


# # У ситуації, коли нам необхідно перевірити, що початок рядка відповідає заданому шаблону, підійде функція
# # re.match(pattern, strObj), яка аналогічно до функції search()
# # повертає об'єкт Match при збігу і None — навпаки

userStr1="My cell phone numbers: Lifecell +38(063)1234567; Kiyvstar +38(067)9875612";
userStr2="Lifecell +38(063)1234567; Kiyvstar +38(067)9875612 — my cell phone numbers";
match3 = re.match(r'Lifecell \+38\(063\)(\d\d\d\d\d\d\d); Kiyvstar \+38\(067\)(\d\d\d\d\d\d\d)', userStr1)
match4 = re.match(r'Lifecell \+38\(063\)(\d\d\d\d\d\d\d); Kiyvstar \+38\(067\)(\d\d\d\d\d\d\d)', userStr2)
print(match3) #None
print(match4.group()) # Lifecell +38(063)1234567; Kiyvstar +38(067)9875612

# # re.sub(pattern, strRepl,strObj) замінює знайдені у рядку strObj збіги із шаблоном pattern на новий фрагмент strRepl.

userStr="2021-2022 Competition Calendar: 30.11.2021 - 2021 Grand Prix Series; 14.12.2021 - Grand Pemio D'Italia"
newStr=re.sub(r'[-;\s]', '/',userStr)
print(newStr) #2021/2022 Competition  Calendar:30.11.2021 / 2021 Grand Prix Series/ 14.12.2021 / Grand Pemio D'Italia

# #  функція split, яка працює подібно, але дозволяє виконувати розбиття на підставі більш складних умов. 
# Отриманий результат, — набір (список)рядків.
userStr="30.11.2021 — 2021 Grand Prix Series,  14.12.2021 — Grand Pemio D'Italia; 27.12.2021 — Cup of Austria by IceChallenge"
strList=re.split(r'[,;]+', userStr)
print(strList)