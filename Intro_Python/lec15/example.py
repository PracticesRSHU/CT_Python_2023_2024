# from turtle import *
# # import turtle             
# my_window = Screen() 
# my_window.bgcolor("blue") 
# my_window.title("Welcome to the turtle-zoo!")      # creates a graphics window
# my_pen = Turtle()      
# my_pen.forward(150)  # my_pen.fd(150)        
# my_pen.left(90)    #lt   
# delay(100)        
# my_pen.forward(75)  
# my_pen.color("white")
# my_pen.pensize(12)

# my_pen.penup()

# my_pen.forward(50)
# my_pen.right(45)
# my_pen.pendown()
# my_pen.forward(150)  # my_pen.fd(150)        
# my_pen.left(90)    #lt  


# my_pen.reset()
# my_pen.width(10)
# my_pen.color("green")
# my_pen.begin_fill()
# my_pen.fd(200)
# my_pen.seth(90)
# my_pen.fd(200)
# my_pen.seth(225)
# my_pen.fd(200)
# my_pen.end_fill()

# exitonclick()

def nsd(a,b):
    if(a==b):
        return a
    if (a<0 or b<0):
        return 1
    if (a>b):
        return nsd(a-b, b)
    else:
        return nsd(a, b-a)

print(nsd(36,12))
print(nsd(24,9))
print(nsd(25,9))