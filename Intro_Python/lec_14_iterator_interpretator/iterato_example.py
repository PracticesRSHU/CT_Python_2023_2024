list1=[1,2,3]

for item in list1:
    print(item)


#for елемент in щось  => iter(щось)  => next(щось)
#create object iterator

iterator=iter([11,22,33]) 

print(iterator)
print(next(iterator))
print(next(iterator))
print(next(iterator))
try:
    print(next(iterator))
except Exception as err:
    print(err.__class__)


iterator=iter(["hello",22,33]) 

iter1=["Python","Java","C#"].__iter__()
print(iter1.__next__())
print(iter1.__next__())
print(iter1.__next__())

#create class iterator
#pow(2,n) 2^1, 2^2...


class PowToTwo:
    def __init__(self,n=0) -> None:
        self.n=n

    def __iter__(self):
        self.start=0
        return self
    
    def __next__(self):
        if self.start<=self.n:
            result=2**self.start
            self.start+=1
            return result
        else:
            raise StopIteration
        

numbers=PowToTwo(5)

iter2=iter(numbers) #1,2,4,...
print(next(iter2))
print(next(iter2))
print(next(iter2))

for number in numbers:
    print(number)

#MyRange(1,6)
class MyRange:
    def __init__(self,start=0,end=0, step=1) -> None:   
        self.start=start
        self.end=end
        self.step=step

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start<=self.end:
            result=self.start
            self.start+=self.step
            return result
        else:
            raise StopIteration
        
myrange=MyRange(1,5)

for i in myrange:
    print(i, end="; ")

print()

myrange.start=6
myrange.end=10
myrange.step=2

for i in myrange:
    print(i, end="; ")

print()




#Фібоначі: 1,1,2,3,5,8,13

class Fibonachi:
    def __init__(self, n) -> None:
        self.n=n
        self.count=1 #номер генерованого числа
        self.prev=1 #генероване  число
        self.next=1 #наступне число

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count>self.n:
            self.count=1
            self.prev=1 #генероване  число
            self.next=1 #наступне число
            raise StopIteration
        result=self.prev
        #new number  a,b=b,a
        # c=self.prev
        # self.prev=self.next
        # self.next=c+self.next
        self.prev, self.next=self.next, self.prev+self.next

        self.count+=1
        return result

fib=Fibonachi(15)

for i in fib:
    print(i, end="; ")
print()


