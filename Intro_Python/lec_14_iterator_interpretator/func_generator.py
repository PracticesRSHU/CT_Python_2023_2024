def fibonachi_generator(n):
    prev=1 #first element of siquence
    next=1 #second element of siquence
    for i in range(n):
        result=prev
        prev, next=next, prev+next
        yield result

print(fibonachi_generator(4))

for i in fibonachi_generator(15):
    print(i,end="; ")

print()


def colors():
    yield "green"
    yield "yellow"
    yield "red"

color_List=list(colors())
print(colo_List)

for color in colors():
    print(color)




