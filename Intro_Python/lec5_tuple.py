tuple1=()
tuple2=(3,)
tuple3=3,
tuple4=tuple([3])
print("tuple1=",tuple1, type(tuple1))
print("tuple2=",tuple2,type(tuple2))
print("tuple3=",tuple3,type(tuple3))
print("tuple4=",tuple4,type(tuple4))

#unmutable
print(tuple3[0])
# tuple3[0]=5
print(tuple3[0])

# Avtor
x=y=z=6
x,y,z="Python","Java","JavaScript"

spisokBook=[
    ["Franko","Kamenyari"],
    ["Shevchenko","Kobzar"],
    ["Lesia Ukrainka","Lisova Pisnya"]
]

for book in spisokBook:
    for item  in book:
        print(item, end=" ")
    print()

spisokBookTyple=(
    ("Franko","Kamenyari"),
    ("Shevchenko","Kobzar"),
    ("Lesia Ukrainka","Lisova Pisnya")
)

for item_tuple in spisokBook:
    avtor, book=item_tuple
    print(avtor,"wrote=>",book)

spisok_avtor=["Франко","Шевченко"]
spisok_book=[["Каменярі","Борислав сміється","Фарбований лис"],["Кобзар","Катерина"]]
spisok_book1=[["Каменярі","Борислав сміється","Фарбований лис"],["Кобзар","Катерина"]]

# print(tuple(zip(spisok_avtor,spisok_book)))
print("*"*15)
list_books=list(zip(spisok_avtor,spisok_book))
print(list_books)
for item_tuple in list_books:
    avtor, books=item_tuple
    print(avtor,"написів =>")
    index=1
    for book in books:
        print(f"{index}. {book}")
        index+=1
a= input("Введіть n")
suma1=int(a)+int(a*2)+int(a*3)+int(a*4)
print(suma1)