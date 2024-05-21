# in terminal:  pip install matplotlib
import matplotlib.pyplot as plt
# in terminal:  pip install numpy
import numpy
# from numpy import *
# plt.plot([4,7,8,10,16])
# plt.savefig("1.png",dpi=100)
# plt.show()

def f(x):
    return x**3+x**2
# plt.plot([f(i) for i in range(-20,20,2)])
# plt.show()

# #using function

# x=numpy.linspace(-1,2,30)
# y=f(x)
# plt.plot(x,y, label='y=x**3+x**2')
# # xmin, xmax, ymin, ymax
# plt.axis([-1,2,-1, 15])
# plt.xlabel('value x')
# plt.ylabel('value y')
# plt.title('My first plot y(x)')
# plt.legend() #insert legend
# plt.show()

#added attr 
x=numpy.linspace(-1,2,30)
y1=f(x)
y2=x**2*numpy.exp(x)
y3=x**2
plt.plot(x,y1,label='y(x)=x**3+x**2',color='g', linestyle='-',linewidth=2, marker='D',markerfacecolor="yellow",markeredgecolor="blue", markeredgewidth=2)
plt.plot(x,y2,label='y(x)=x**2+exp(x)',marker='^',color='b')
# plt.plot(x,y3,label='y(x)=x**2+exp(x)',marker='s', linestyle='--')
plt.plot(x,y3,'rs--',label='y(x)=x**2+exp(x)')
# plt.plot(x,y1,label='y(x)=x**3+x**2',marker='o')
# plt.plot(x,y2,label='y(x)=x**2+exp(x)',marker='^')
plt.legend() #insert legend
# plt.xticks(range(-1,2,1))
# plt.yticks(range(1,8))
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
plt.show()


# histogram

y=numpy.random.rand(500) #гаусовий розподіл
plt.hist(y,20)
plt.show()


#масив поппулярності мов прогармування
x=["Python", "Java", "C#","Ruby","JavaScript"]
y=[26,20,26,12,30]
# plt.barh(x, y)
plt.pie(y,labels=x,shadow=True, explode=[0,0,0.2,0,0.4],autopct='%.1f%%')
plt.show()


alpha=numpy.arange(0.0,2.0,1/180)*numpy.pi # 380 
plt.polar(alpha,numpy.sin(5*alpha))
plt.show()