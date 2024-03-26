# #list
# digits=[0,1,2,3,4,5,6,7,8,9]
# print(digits)
# print(type(digits))
# print(id(digits))

# list1=[23,"Python",'a',45.5]
# #       0     1     2   3 
# print(f'2-q елемент списку {list1} => {list1[1]}')

# list2=[] # => []
# #сформувати список чисел, що є квадратами чисел від 1 до 10
# for item in range(11):
#     list2.append(item**2)

# print("list2=",list2)    

# list2_v2=[item for item in range(11)]
# print("list2_v2=",list2)    

# #random
# import random

list3=list()  # =>[]
# print(list2,"\n",list3)



# list_generate_numbers=list(range(0,11,2))
# print(list_generate_numbers)
# list_symbols=list("We are learning Python!")
# print(list_symbols)
# list_words="We are learning Python!".split(sep=" ") # ==
# list_words="We are learning Python!".split()        # ==
# print(list_words)

# #create list with number where number%3==0 and number%7==0 by [1,100]

# list_div_3_and_7=[value for value in range(1,101) if value%3==0  and value%7]
# print(list_div_3_and_7)

# #using methods and function to list
# list_random=[]
# for item in range(11):
#     # randint (a,b) => Return random integer in range [a, b], including both end points.
#     list_random.append(random.randint(1,100))

# print("list_random=",list_random)

# #insert 55 in index 5
# list_random.insert(4,55)
# print("insert 55 in list: ",list_random)
# #return index number 55 from list_random
# print("index number 55 => ", list_random.index(55))
# #remove 55
# list_random.remove(55)
# print("remove 55 from list: ",list_random)

# #delete last element of list
# print("list before delete: ",list_random)
# list_random.pop()
# print("list after delete last element => ", list_random)

# # take last elemnts of list
# print("last elements of list",list_random.pop())

# print("*"*15,"\nlist before reverse: ",list_random)
# list_random.reverse()
# print("reverse=>",list_random)

# # list_random.sort()
# # print("sort=>",list_random)

# print("len=>",len(list_random) )
# print("min=>",min(list_random) )
# print("max=>",max(list_random) )
# print("sorted=>",sorted(list_random) )

# #copy deepcopy!!!!!!!!
import random
list_first=[4,55,74,63,75]
list_second=list_first
list_third=list_first.copy()
print("list_first=",list_first,"id=",id(list_first))
print("list_second=",list_second,"id=",id(list_second))
print("list_third=",list_third,"id=",id(list_third))

list_second[0]=44
print("After change first elemnt======")
print("list_first=",list_first)
print("list_second=",list_second)
print("list_third=",list_third)

list_third[0]=[45,333,66]
print("After change third elemnt======")
print("list_third=",list_third)
print("#"*30)
# list4=list_third.copy() #неглибоке копіювання
list4=list_third[:] 
#глибоке копіювання
import copy
list5=copy.deepcopy(list_third)

print("list_third=",list_third)
print("list4=",list4)
print("list5=",list5)

print("After change  element======")
list_third[1]=555
list4[1]=5555
print("list_third=",list_third)
print("list4=",list4) 
print("list5=",list5)
# accessed to number 333 in list_third
print(list_third[0][1])
list_third[0][1]=3333
print("After change inner list element======")
print("list_third=",list_third)
print("list4=",list4)
print("list5=",list5) 
#j
# 1 2 3   i
# 4 5 6
# 7 8 9 

matrix_3x3=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix_3x3)

suma=0
#n_row=len(matrix_3x3)
for row in matrix_3x3:
    #print(i)
    #n_col=len(row)
    for col in row:
        suma+=col # suma=suma+col
        print(col,end=" ")
    print()

print("Suma=",suma)


#j
# 1 2 3   i
# 5
# 7 9 
print("рваний масив: ")
matrix_ex=[[1,2,3],5,[7,9]]
print(matrix_3x3)

for row in matrix_ex:
    if type(row)==int:
        print(row)
        continue
    for col in row:
        print(col,end=" ")
    print()





