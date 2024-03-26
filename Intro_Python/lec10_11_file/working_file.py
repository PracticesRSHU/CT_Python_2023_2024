import shelve
import os

# file_wr=""
# D:\Tetyana\CT_Python_2023_2024\Intro_Python\lec_file\working_file.py
# Intro_Python\lec_file => relative path
# D:\Tetyana\CT_Python_2023_2024\Intro_Python\lec_file\record.txt  => absolute path
file_wr=None
try:
    # file_wr=open('Intro_Python\\lec_file\\record.txt','at')
    file_wr=open('Intro_Python/lec_file/record.txt','xt')
    print(f'type=> {type(file_wr)}')
    text="""Write to an Existing File
    To write to an existing file, you must add a parameter to the open() function:
    "a" - Append - will append to the end of the file
    "w" - Write - will overwrite any existing content"""
    print(text, file=file_wr)
    file_wr.write(text+"\n")
except FileExistsError:
    print("record.txt already exists!")
else:
    file_wr.close()

# read, readline(), readlines()
file_r=open("Intro_Python/lec_file/record.txt","rt")
text=file_r.read()
# text=file_r.readlines()
# text=""
# while True:
#     line=file_r.readline()
#     if not line:
#         break
#     text+=line
words=file_r.split()
file_r.close()
print(text)
# print(len(text))


# #======================================
# file_r=open("Intro_Python\\lec_file\\record.txt","rt")
# count_symbol=50
# text1=''

# while True:
#     fragment=file_r.read(count_symbol)
#     if not fragment:
#         break
#     text1+=fragment
#     print(len(fragment))

# print("row=",file_r.read())
# # print("row=",file_r.read())
# file_r.close()
# print(text1)
#
# print("*"*30)
# file_r=open("record.txt","rt")
# text2=""
# line=file_r.readline()
# while line:
#     text2 += line
#     line = file_r.readline()
# file_r.close()
# print(text2)
#
#
# text3=""
# file_r=open("Intro_Python\\lec_file\\record.txt","rt")
# for line in file_r:
#     text3+=line

# file_r.close()
# print(text3)
#
#
# text4=""
# file_r=open("Intro_Python\\lec_file\\record.txt","rt")
# lines=file_r.readlines()
# print(lines)
# file_r.close()
# text5="".join(lines)
# print(text5)

# for line in lines:
#     text4+=line
# print(text4)
#
# # ===================binary files==========================
#

bindata=bytes(range(0,256))
# print(bindata)
# file_b_w=open("Intro_Python\\lec_file\\binary.dat","wb")
# file_b_w.write(bindata)
# text="""Write to an Existing File
#     To write to an existing file, you must add a parameter to the open() function:
#     "a" - Append - will append to the end of the file
#     "w" - Write - will overwrite any existing content"""
# # file_b_w.write(bytes(text,encoding="UTF-8"))
# file_b_w.close()
#
#
file_b_w=open("Intro_Python\\lec_file\\binary.dat","wb")
len_data=len(bindata)
setByte=0
step=50
while setByte<len_data:
    rez=file_b_w.write(bindata[setByte:setByte+step])
    print(rez)
    setByte+=step
file_b_w.close()
#
# file_b_r=open("Intro_Python\\lec_file\\binary.dat","rb")
# print(file_b_r.read())
# file_b_r.close()
#

print("====using tell()  and seek()")
# # # tell seek
# file_b_r=open("Intro_Python\\lec_file\\binary.dat","rb")
# # print(file_b_r.tell())
# # print(file_b_r.seek(90))
# # print(file_b_r.tell())

# # print(chr(97))
# print(file_b_r.seek(97,0))
# # print(file_b_r.seek(-148,2))
# print(file_b_r.tell())
# # print(file_b_r.seek(4,1))
# # print(file_b_r.tell())
# # print(chr(165))
# bdata=file_b_r.read(26)
# print(bdata)
# file_b_r.close()
#
with open("Intro_Python\\lec_file\\binary.dat","rb") as file_b_r:
    print(file_b_r.seek(97,0))
    # # print(file_b_r.seek(-148,2))
    # print(file_b_r.tell())
    # # print(file_b_r.seek(4,1))
    # # print(file_b_r.tell())
    # # print(chr(165))
    bdata=file_b_r.read(26)
    print(bdata)
#
# with open("binary.dat","rb") as fread:
#     text=fread.read()
#     print(text)

# """
#    ['Python', 'Guido van Rossum'],
#     ['Scala', 'Martin Odersky'],
#     ['PHP', 'Rasmus Lerdorf'],
#     ['Ruby', 'Yukihiro Matsumoto'],
#     ['C', 'Dennis Ritchie'],
# """

# filename = "shelve_ex"

# with shelve.open(filename, 'c') as shelve_wr:
#     shelve_wr['Python'] = 'Guido van Rossum'
#     shelve_wr['Scala'] = 'Martin Odersky'
#     shelve_wr['C'] = 'Dennis Ritchie'

# with shelve.open(filename, 'r') as shelve_r:
#     key="Scala"
#     if key in shelve_r:
#         print(shelve_r[key])
    # print(shelve_r['Python'])
    # print(shelve_r['Scala'])

# with shelve.open(filename, 'r') as shelve_r:
#     value=shelve_r.get("C","None")
#     print(value)

# with shelve.open(filename, 'r') as shelve_r:
#     for key in shelve_r:
#         print(key," ",shelve_r[key])


# with shelve.open(filename, 'r') as shelve_r:
#     for avtor in shelve_r.values():
#         print(avtor)

# with shelve.open(filename, 'c') as shelve_wandr:
#     shelve_wandr["C"]="Ritchie"


# with shelve.open(filename, 'r') as shelve_r:
#     for avtor in shelve_r.values():
#         print(avtor)


# # os.mkdir("example1")
# # os.mkdir("D://Example1")
# # os.mkdir("D://Example1/exam")
# if os.path.exists("D://Example1/exam/f2.txt"):
#     os.rename("D://Example1/exam/f2.txt","D://Example1/exam/f1.txt")
# else:
#     print("ERROR")


# # filename="D://Example1/exam/f1.txt"
# with open("listSt.txt",'rt') as fileR:
#     # rez=fileR.read()
#     rez=fileR.readlines()

# print(rez)
# with open("listSt.txt",'wt') as fileW:
#     for row in rez:
#         print(row.rstrip("\n"))
#         listInfo=row.rstrip("\n").split()
#         print(listInfo)
#         if int(listInfo[1])>7:
#             listInfo[0]=listInfo[0].upper()
#         print(listInfo)
#         fileW.write(f"{listInfo[0]} {listInfo[1]} \n")

# print(rez)
