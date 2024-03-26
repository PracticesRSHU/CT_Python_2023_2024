
spisok_avtor=["Франко","Шевченко"]
spisok_book=[["Каменярі","Борислав сміється","Фарбований лис"],["Кобзар","Катерина"]]
spisok_book1=[["Каменярі","Борислав сміється","Фарбований лис"],["Кобзар","Катерина"]]

print(tuple(zip(spisok_avtor,spisok_book)))
library0=dict(zip(spisok_avtor,spisok_book))
print(library0)
library1={}
print(type(library1))
library2=dict()
print(type(library2))
library1["Франко"]=["Каменярі","Борислав сміється","Фарбований лис"]
print(library1)
library1["Шевченко"]=["Кобзар","Катерина"]
print(library1)

list_tuple_books=list(zip(spisok_avtor,spisok_book))
library3=dict(list_tuple_books)
print("library3:\n",library3)

library4=dict(zip(spisok_avtor,spisok_book))
print("library4:\n",library4)
library5={"Українка":"Лісова пісня"}
print("library5:\n",library5)

library4["Українка"]="Лісова пісня"
print(f"library4:{'*'*20}\n",library4)

# print(library4["Українка"])

library6=dict(library4)
print(f"library6:{'*'*20}\n",library4)
library4["Франко"]="Захар Беркут"
print(f"library4:{'*'*20}\n",library4)
# iter_library=iter(library4)
print(".items",library6.items())

for item in library6.items():
    print(item[0])
    print("\t\t",item[1])

print("*"*30)
for author, book in library6.items():
    print(author)
    print("\t\t",book)

print("*"*30)
library6["Українка"]=["Лісова пісня"]
for author, book in library6.items():
    print(author)
    for b in book:
        print("- ",b)


#Додати ще один твір у список творів Лесі Українки
book1="Досвітні вогні"


print(library6["Українка"])

library6["Українка"].append(book1)
for author, book in library6.items():
    print(author)
    for b in book:
        print("- ",b)

author=input("Input author")
book2=input(f"Input book {author}: ")
if author in library6:
    library6[author].append(book2)
else:
    library6[author]=[book2]

print("*"*40)
for author, book in library6.items():
    print(author)
    for b in book:
        print("- ",b)

