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
