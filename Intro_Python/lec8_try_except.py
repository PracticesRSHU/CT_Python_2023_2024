# print(dir(locals()['__builtins__'])) #повернення вюудованих винятків, функцій, атрибутів
try:
    n=input("Input number:")
    print(5/n)
except TypeError:
    print("Ви ввели не число")
except ZeroDivisionError:
    print("Ділення на нуль")


print("Next statement...")


try:
    n=int(input("Input number:"))
    print(5/n)
    if n%2!=0:
        raise Exception(f"{n}=>не парне число")
except TypeError:
    print("Ви ввели не число")
except ZeroDivisionError as zero:
    print("Ділення на нуль", zero)
except Exception as exp:
    print(exp)
else: 
    print("Помилок нема...")
finally:
    print("Кінець блоку try - except!")