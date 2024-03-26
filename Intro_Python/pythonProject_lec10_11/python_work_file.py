# import fileWork
# from fileWork import fileWR,fileWRwith,fileWRofA
#import fileReader as fr
#import fileWork as fw
from packageFile import fileReader,fileWork
# from packageFile import fileReader as fr
# from packageFile import fileWork as fw
#АБО
from packageFile import fileReader as fr, fileWork as fw

FILENAME="dataWr.txt"
# fileWr=open(FILENAME,"wt")
string="""
    The default mode is 'rt' (open for reading text). For binary random
    access, the mode 'w+b' opens and truncates the file to 0 bytes, while
    'r+b' opens the file without truncation. The 'x' mode implies 'w' and
    raises an `FileExistsError` if the file already exists.
"""
## import fileWork
# fileWr.write(string)
# fileWr.close()
# fileWork.fileWR(FILENAME,string)
## from fileWork import fileWR,fileWRwith,fileWRofA
# fileWR(FILENAME,string)
# fileWRofA(FILENAME,string)
# fileWRofA(FILENAME,string)
# import fileWork as fw
fw.fileWRofPrint("dataPrint.dat",string)

#читання з файлу
# fileRd=open(FILENAME,'rt')
# result_string=fileRd.read().split('\n')
# print(result_string)
# # result_string1=fileRd.readlines()
# # print(result_string1)
# fileRd.close()
#використання модуля fileReader.py
# print(fr.fileReadByRead(FILENAME))
print(fr.fileReadByWhileNumberSymbol(FILENAME,50))
masivByte=bytes(range(0,256))
fileWrite=open('binaryFile','wb')
fileWrite.write(masivByte)
fileWrite.close()
print(masivByte)
print("*"*35)
print("Result read file")
with open('binaryFile','rb') as f:
    print(f.read())
    print(f.tell())

with open('binaryFile','rb') as f:
    print(f.seek(253,1))
    print(f.tell())
    print(f.read())

