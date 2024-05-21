# coding unicode
print(ord('♥'))
print(chr(0x10ffFf)) #0 <= i <= 0x10ffff
print(chr(9829)) #0 <= i <= 0x10ffff
# \uXXXX (16-a)  XX - 00  => FF XX => 
print("\u0024")
import unicodedata


# name_unicode=unicodedata.name("A")
name_unicode=unicodedata.name("\u00a2")
value1=unicodedata.lookup("LATIN CAPITAL LETTER A")
value2=unicodedata.lookup(name_unicode)
print(name_unicode)    
print(value1)    
print(value2)    

#unicode = > UTF-8 => 1байт=8біт ASCII
#                  => 2 байти (не для кирилиці)
#                  => 3 байти ()
#                  => 4 байти (азіаткські мови і символи)


c="\u2612"
c="#"
result=c.encode('utf-8')  # latin-1, cp1251, unicode-escape  ,ascii
print(len(result))
print(result)

c="\u2612"
result=c.encode('ascii','ignore')  # latin-1, cp1251, unicode-escape  ,ascii
print(len(result))
print(result)
